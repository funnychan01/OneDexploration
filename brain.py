import numpy as np
import pandas as pd

np.random.seed(2)

class Brain:

    def __init__(self):
        self.n_states = 6
        self.actions = ["left", "right"]
        self.epsilon = 0.9
        self.alpha = 0.1
        self.gamma = 0.9
        self.max_episode = 13
        self.fresh_time = 0.3
        self.q_table = pd.DataFrame()
        self.action_name = None
        self.S_ = None
        self.R = None


    def build_q_table(self):
        self.q_table = pd.DataFrame(
            np.zeros((self.n_states, len(self.actions))),
            columns=self.actions
        )
        return self.q_table


    def choose_action(self):
        state_actions = self.q_table.iloc[self.state, :]
        if (np.random.uniform() > self.epsilon) or (state_actions.all() == 0):
            self.action_name = np.random.choice(self.actions)
        else:
            self.action_name = state_actions.argmax()
        return self.action_name


    def get_env_feedback(self, S):
        if self.action_name == "right":
            if S == self.n_states - 2:
                self.S_ = "terminal"
                self.R = 1
            else:
                self.S_ = S + 1
                self.R = 0
        else:
            self.R = 0
            if S == 0:
                self.S_ = S
            else:
                self.S_ = S - 1
        return self.S_, self.R