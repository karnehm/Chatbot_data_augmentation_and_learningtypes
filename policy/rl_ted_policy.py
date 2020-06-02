import logging
import random

import numpy as np
from collections import deque
from typing import List, Any, Optional

from progressbar import progressbar
from rasa.core.domain import Domain
from rasa.core.featurizers import MaxHistoryTrackerFeaturizer
from rasa.core.policies.ted_policy import TEDPolicy, TED, LABEL_IDS, DIALOGUE_FEATURES, LABEL_FEATURES
from rasa.core.trackers import DialogueStateTracker
from rasa.utils import train_utils
from rasa.utils.tensorflow.constants import EPOCHS, BATCH_SIZES, EVAL_NUM_EXAMPLES, EVAL_NUM_EPOCHS, BATCH_STRATEGY, \
    LOSS_TYPE, SOFTMAX, RANKING_LENGTH
from rasa.utils.tensorflow.model_data import RasaModelData
from rasa.utils.tensorflow.models import RasaModel

logger = logging.getLogger(__name__)
logger.setLevel(30)

SAVE_MODEL_FILE_NAME = "rlted_policy"

class RLTEDPolicy(TEDPolicy):
    def train(
            self,
            training_trackers: List[DialogueStateTracker],
            domain: Domain,
            **kwargs: Any,
    ) -> None:
        """Train the policy on given training trackers."""

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
            1,
            32,
            self.config[EVAL_NUM_EXAMPLES],
            self.config[EVAL_NUM_EPOCHS],
            batch_strategy=self.config[BATCH_STRATEGY],
        )

        self.agent.target_network.fit(
            model_data,
            1,
            32,
            self.config[EVAL_NUM_EXAMPLES],
            self.config[EVAL_NUM_EPOCHS],
            batch_strategy=self.config[BATCH_STRATEGY],
        )

        batch_size = 8
        num_of_episodes = 20
        timesteps_per_episode = 1000

        for e in range(0, num_of_episodes):
            # Reset the enviroment
            state = self.enviroment.get_current_state()
            model_state = self._create_model_data(data_X=np.array([state]))
            # state.data['dialogue_features'] = np.array([state.data['dialogue_features']])

            # Initialize variables
            last_reward = 1
            terminated = False
            print('number of Episodes: ' + str(e))
            for timestep in range(timesteps_per_episode):
                # Run Action
                action = self.agent.act(model_state, last_reward)

                # Take action
                next_state, reward, terminated = self.enviroment.step(action)
                if reward > 0:
                    self.store(state, action, reward, next_state, terminated)
                last_reward = reward

                state = next_state
                model_state = self._create_model_data(data_X=np.array([next_state]))


                #if terminated:
                #    self.agent.alighn_target_model()
                #    break

                if len(self.expirience_replay) >= batch_size:
                    minibatch = random.sample(self.expirience_replay, batch_size)
                    self.agent.retrain(minibatch=minibatch, create_model_data=self._create_model_data)
                    self.expirience_replay.clear()

        self.model = self.agent.q_network

    def store(self, state, action, reward, next_state, terminated):
        self.expirience_replay.append((state, action, reward, next_state, terminated))


class TEDAgent:
    """

    """

    def __init__(self, enviroment, model_data, config, featurizer, label_data):
        self.config = config
        self.enviroment = enviroment
        # Initialize discount and exploration rate
        self.gamma = 0.6
        self.epsilon = 0.1

        # Build networks
        self.q_network = self._build_model(model_data, config, featurizer, label_data)
        self.target_network = self._build_model(model_data, config, featurizer, label_data)
        self.alighn_target_model()

    def alighn_target_model(self):
        self.target_network.set_weights(self.q_network.get_weights())

    def act(self, state, last_reward):
        if np.random.rand() <= self.epsilon or last_reward == 0:
            return self.enviroment.get_random_action()
        else:
            output = self.q_network.predict(state)
            return np.argmax(output["action_scores"])

    def retrain(self, minibatch, create_model_data):
        states = np.array([[]])
        targets = np.array([[]])
        for state, action, reward, next_state, terminated in minibatch:

            if(reward > 0):
                model_state = create_model_data(data_X=np.array([state]))
                target = self.q_network.predict(model_state)['action_scores'].numpy()
                # V2
                target[0][0] = np.full((len(target[0][0])), 0)
                target[0][0][action] = reward
                if states.all():
                    states = np.array([state])
                    targets = target[0]
                else:
                    states = np.concatenate((states, [state]))
                    targets = np.concatenate((targets, target[0]))
        if not states.all():
            print(len(states))
            model_data = create_model_data(data_X=states, data_Y=targets)
            self.q_network.fit(model_data,
                               1,
                               32,
                               self.config[EVAL_NUM_EXAMPLES],
                               self.config[EVAL_NUM_EPOCHS],
                               batch_strategy=self.config[BATCH_STRATEGY],
                               )

    def _build_model(self, model_data, config, featurizer, label_data):
        return TED(
            model_data.get_signature(),
            config,
            isinstance(featurizer, MaxHistoryTrackerFeaturizer),
            label_data,
        )


class TEDEnviroment:
    def __init__(self, model_data, training_y, training_trackers):
        self.model_data = model_data
        self.training_y = training_y
        self.training_trackers = training_trackers
        self.possible_states_indexes = range(len(self.get_states()) - 1)
        self.current_state_index = self._get_next_state_index()
        self.following_correct_steps = 0

    def step(self, action):
        x = self.training_y[self.current_state_index]
        predicted_action = np.argmax(self.training_y[self.current_state_index])
        reward = 0
        terminated = True
        if predicted_action == action:
            self.following_correct_steps += 1
            reward = 1/self.following_correct_steps
            terminated = False

            if self.current_state_index >= len(self.possible_states_indexes):
                self.current_state_index = 0
            else:
                self.current_state_index += 1
        else:
            self.following_correct_steps = 0

        next_state = self.get_current_state()
        return next_state, reward, terminated

    def get_current_state(self):
        return self.get_states()[self.current_state_index]

    def get_actions(self):
        return self.model_data.data['label_features'][0]

    def get_random_action(self):
        return random.choice(range(len(self.training_y[0])))

    def get_states(self):
        return self.model_data.data['dialogue_features'][0]

    def _get_next_state_index(self):
        return random.choice(self.possible_states_indexes)
