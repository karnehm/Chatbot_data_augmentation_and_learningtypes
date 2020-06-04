from rasa.core.featurizers import MaxHistoryTrackerFeaturizer
from rasa.core.policies.ted_policy import TED
from rasa.utils.tensorflow.constants import EVAL_NUM_EXAMPLES, EVAL_NUM_EPOCHS, BATCH_STRATEGY
import numpy as np

DISCOUNT = 0.99
UPDATE_TARGET_EVERY = 5


class TEDAgent:
    """

    """

    def __init__(self, enviroment, model_data, config, featurizer, label_data):
        self.config = config
        self.enviroment = enviroment
        # Initialize discount and exploration rate
        self.gamma = 0.6
        self.epsilon = 0.05
        self.target_update_counter = 0

        # Build networks
        self.q_network = self._build_model(model_data, config, featurizer, label_data)
        self.target_network = self._build_model(model_data, config, featurizer, label_data)
        self.alighn_target_model()

    def alighn_target_model(self):
        self.q_network.set_weights(self.target_network.get_weights())

    def act(self, state, last_reward):
        if np.random.rand() <= self.epsilon: # or last_reward <= 0:
            return self.enviroment.get_random_action()
        else:
            output = self.q_network.predict(state)
            return np.argmax(output["action_scores"])

    def retrain(self, minibatch, terminal_state, create_model_data ):

        X = np.array([])
        y = np.array([])

        for index, (state, action, reward, next_state, terminated) in enumerate(minibatch):

            # Get current states from minibatch, then query NN model for Q values
            current_states = np.array([state])
            current_states = create_model_data(data_X=current_states)
            current_qs_list = self.q_network.predict(current_states)

            new_current_states = np.array([next_state])
            new_current_states = create_model_data(data_X=new_current_states)
            future_qs_list = self.target_network.predict(new_current_states)

            if not terminated:
                max_future_q = np.max(future_qs_list['action_scores'][0][0][index])
                new_q = reward + DISCOUNT * max_future_q
            else:
                new_q = reward

            # Update Q value for given state
            current_qs = current_qs_list['action_scores'][0][0].numpy()
            current_qs[action] = new_q
            if X.all():
                X = current_states.data['dialogue_features'][0]
                y = [current_qs]
            else:
                X = np.concatenate((X, current_states.data['dialogue_features'][0]))
                y = np.concatenate((y, [current_qs]))


        model_data = create_model_data(X, y)
        self.q_network.fit(model_data,
                                1,
                                32,
                                self.config[EVAL_NUM_EXAMPLES],
                                self.config[EVAL_NUM_EPOCHS],
                                batch_strategy=self.config[BATCH_STRATEGY],
                                )

        if terminal_state:
            self.target_update_counter += 1

        if self.target_update_counter > UPDATE_TARGET_EVERY:
                self.target_network.set_weights(self.q_network.get_weights())
                self.target_update_counter = 0



    def _build_model(self, model_data, config, featurizer, label_data):
        return TED(
            model_data.get_signature(),
            config,
            isinstance(featurizer, MaxHistoryTrackerFeaturizer),
            label_data,
        )


