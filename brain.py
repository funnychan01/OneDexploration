import numpy as np
import pandas as pd
import time

n_states = 6
actions = ["left", "right"]
epsilon = 0.9
alpha = 0.1
gamma = 0.9
max_episode = 13
fresh_time = 0.3

def build_q_table(n_states, actions):
    q_table = pd.DataFrame(
        np.zeros((n_states, len(actions))),
        columns=actions
    )
    return q_table

def choose_action(state, q_table):
    state_actions = q_table.iloc[state, :]
    if (np.random.uniform() > epsilon) or (state_actions.all() == 0):
        action_name = np.random.choice(actions)
    else:
        action_name = state_actions.argmax()
    return action_name

