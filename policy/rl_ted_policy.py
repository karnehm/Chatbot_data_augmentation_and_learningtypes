import logging
import random

import pandas as pd
import numpy as np
from collections import deque
from typing import List, Any

from rasa.core.domain import Domain
from rasa.core.policies.ted_policy import TEDPolicy
from rasa.core.trackers import DialogueStateTracker
from rasa.core.training.dsl import StoryFileReader
from rasa.utils.tensorflow.constants import EVAL_NUM_EXAMPLES, EVAL_NUM_EPOCHS, BATCH_STRATEGY

from importer.helper import get_graph
from policy.TEDAgent import TEDAgent
from policy.TEDEnviroment import TEDEnviroment

logger = logging.getLogger(__name__)
logger.setLevel(30)

SAVE_MODEL_FILE_NAME = "rlted_policy"
MIN_REPLAY_MEMORY_SIZE = 100
BATCH_SIZE = 32
'''
First Commit:

    batch_size = 8
    num_of_episodes = 20
    timesteps_per_episode = 1000

    precision: 0.6080
    f1: 0.6131
    accuracy: 0.6387


Second Commit: Harmonic-Calculation sum 1/n Batch 8
    precision: 0.5852
    f1: 0.5772
    accuracy: 0.6295

3th Commit: Hamonic-Calculation Batch 32:
    precision: 0.5738
    f1: 0.5570
    accuracy: 0.5896 

4th Commit: Hamonic-Calculation Batch 32 reward without changing reward
    precision: 0.6637
    f1: 0.6342
    accuracy: 0.6520

5th: Reward by 1/n
    precision: 0.5931
    f1: 0.5836
    accuracy: 0.6172

6th: Reward by euler_calc sum 1/(n^2)
    precision: 0.5568
    f1: 0.5508
    accuracy: 0.5680

7th: Agent act without last_reward
    precision: 0.6560
    f1: 0.6383
    accuracy: 0.6837

8th: Agent with last reward and 100 episodes
    precision: 0.7388
    f1: 0.7012
    accuracy: 0.7011
                    micro avg       0.74      0.70      0.72       977
                    macro avg       0.49      0.48      0.46       977
                 weighted avg       0.74      0.70      0.70       977

9th:
    precision: 0.9386
    f1: 0.8926
    accuracy: 0.8926
                    micro avg       0.90      0.89      0.90       977
                    macro avg       0.95      0.85      0.87       977
                 weighted avg       0.94      0.89      0.89       977
 10th:
    precision: 0.5766
    f1: 0.5941
    accuracy: 0.6448                                  

11th: Reward = \sum^n_{i=1} 1/(n+1) 
    precision: 0.9192
    f1: 0.9037
    accuracy: 0.8997
                        micro avg       0.91      0.90      0.90       977
                    macro avg       0.92      0.88      0.89       977
                 weighted avg       0.92      0.90      0.90       977

'''


class RLTEDPolicy(TEDPolicy):
    def train(
            self,
            training_trackers: List[DialogueStateTracker],
            domain: Domain,
            **kwargs: Any,
    ) -> None:
        """Train the policy on given training trackers."""

        # domain = await self.get_domain()
        # story_steps = await StoryFileReader.read_from_files(
        #    self._story_files,
        #    domain
        # )

        self.expirience_replay = deque(maxlen=2000)

        # dealing with training data
        training_data = self.featurize_for_training(training_trackers, domain, **kwargs)

        self._label_data = self._create_label_data(domain)

        # extract actual training data to feed to model
        model_data = self._create_model_data(training_data.X, training_data.y)
        if model_data.is_empty():
            logger.error(
                f"Can not train '{self.__class__.__name__}'. No data was provided. "
                f"Skipping training of the policy."
            )
            return

        # keep one example for persisting and loading
        self.data_example = model_data.first_data_example()

        self.enviroment = TEDEnviroment(model_data=model_data, training_trackers=training_trackers,
                                        training_y=training_data.y)
        self.agent = TEDAgent(enviroment=self.enviroment, model_data=model_data,
                              config=self.config, featurizer=self.featurizer,
                              label_data=self._label_data)

        self.agent.q_network.fit(
            model_data,
            5,
            32,
            self.config[EVAL_NUM_EXAMPLES],
            self.config[EVAL_NUM_EPOCHS],
            batch_strategy=self.config[BATCH_STRATEGY],
        )
        self.agent.target_network.fit(
            model_data,
            5,
            32,
            self.config[EVAL_NUM_EXAMPLES],
            self.config[EVAL_NUM_EPOCHS],
            batch_strategy=self.config[BATCH_STRATEGY],
        )

        num_of_episodes = int(model_data.num_examples / 5)
        print("EPISODEN: " + str(num_of_episodes))

        for e in range(0, num_of_episodes):
            # Reset the enviroment
            state = self.enviroment.get_current_state()
            model_state = self._create_model_data(data_X=np.array([state]))
            # state.data['dialogue_features'] = np.array([state.data['dialogue_features']])

            # Initialize variables
            terminated = False
            print('number of Episodes: ' + str(e))
            number_of_terminated = 0
            while number_of_terminated < 5:
                # for timestep in range(timesteps_per_episode):
                # Run Action
                action = self.agent.act(model_state)

                # Take action
                next_state, reward, terminated = self.enviroment.step(action)

                self.store(state, action, reward, next_state, terminated)

                state = next_state
                model_state = self._create_model_data(data_X=np.array([next_state]))
                print(len(self.expirience_replay))
                if len(self.expirience_replay) >= BATCH_SIZE and len(self.expirience_replay) >= MIN_REPLAY_MEMORY_SIZE:
                    minibatch = random.sample(self.expirience_replay, BATCH_SIZE)
                    self.agent.retrain(minibatch=minibatch, create_model_data=self._create_model_data,
                                       terminal_state=terminated)
                # self.expirience_replay.clear()
                if terminated:
                    self.agent.alighn_target_model()
                    # self.enviroment.reset()
                    break
        self.model = self.agent.target_network

    def store(self, state, action, reward, next_state, terminated):
        self.expirience_replay.append((state, action, reward, next_state, terminated))
