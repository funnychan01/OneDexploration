import numpy as np
import pandas as pd

np.random.seed(2)


class Brain:

    def __init__(self):
        self.epsilon = 0.9

    def build_q_table(self, n_states, actions):
        q_table = pd.DataFrame(
            np.zeros((n_states, len(actions))),
            columns=actions,
        )
        return q_table

    def choose_action(self, state, q_table, actions):

        state_actions = q_table.iloc[state, :]
        if (np.random.uniform() > self.epsilon) or ((state_actions == 0).all()):
            action_name = np.random.choice(actions)
        else:
            action_name = state_actions.idxmax()
        return action_name

    def get_env_feedback(self, S, A, n_states):

        if A == 'right':
            if S == n_states - 2:
                S_ = 'terminal'
                R = 1
            else:
                S_ = S + 1
                R = 0
        else:
            R = 0
            if S == 0:
                S_ = S
            else:
                S_ = S - 1
        return S_, R
