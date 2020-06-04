import random
import numpy as np

class TEDEnviroment:
    def __init__(self, model_data, training_y, training_trackers):
        self.model_data = model_data
        self.training_y = training_y
        self.training_trackers = training_trackers
        self.possible_states_indexes = range(len(self.get_states()) - 1)
        self.current_state_index = 0
        self.following_correct_steps = 0

    def reset(self):
        self.current_state_index = 0
        self.following_correct_steps = 0


    def step(self, action):
        x = self.training_y[self.current_state_index]
        predicted_action = np.argmax(self.training_y[self.current_state_index])
        reward = 0
        terminated = True
        if predicted_action == action:
            self.following_correct_steps += 1
            reward = self.calc_harmonic(self.following_correct_steps)
            #reward = self.calc_euler(self.following_correct_steps)
            terminated = False
        else:
            self.following_correct_steps = 0

        if self.current_state_index >= len(self.possible_states_indexes):
            self.current_state_index = 0
        else:
            self.current_state_index += 1
        next_state = self.get_current_state()
        return next_state, reward, terminated

    def calc_harmonic(self, n):
        x = 0
        for i in range(1, n + 1):
            x += 1/i
        return x

    def calc_euler(self, n):
        x = 0
        for i in range(1, n+1):
            x += 1/(i ** 2)
        return x

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
