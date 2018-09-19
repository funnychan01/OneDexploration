import numpy as np
import pandas as pd
import time

"""
A simple example for Reinforcement Learning using table lookup Q-learning method.
An agent "o" is on the left of a 1 dimensional world, the treasure is on the rightmost location.
Run this program and to see how the agent will improve its strategy of finding the treasure.

Q-learning application.
"""

np.random.seed(2)

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


def get_env_feedback(S, A):
    if A == "right":
        if S == n_states - 2:
            S_ = "terminal"
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


def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-'] * (n_states - 1) + ['T']  # '---------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode + 1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(fresh_time)


def rl():
    q_table = build_q_table(n_states, actions)

    for episode in range(max_episode):
        step_counter = 0
        S = 0
        is_terminated = False
        update_env(S, episode, step_counter)

        while not is_terminated:
            A = choose_action(S, q_table)
            S_, R = get_env_feedback(S, A)
            q_predict = q_table.loc[S, A]
            if S_ != "terminal":
                q_target = R + gamma * q_table.iloc[S_, :].max()
            else:
                q_target = R
                is_terminated = True

            q_table.loc[S, A] += alpha * (q_target - q_predict)
            S = S_

            update_env(S, episode, step_counter + 1)

            step_counter += 1

        print(q_table)


if __name__ == "__main__":
    q_table = rl()
    print("\r\nQ-table:\n")
    print(q_table)
