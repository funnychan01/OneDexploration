import numpy as np
import pandas as pd
import env.Environment as environment

"""
A simple example for Reinforcement Learning using table lookup Q-learning method.
An agent "o" is on the left of a 1 dimensional world, the treasure is on the rightmost location.
Run this program and to see how the agent will improve its strategy of finding the treasure.

Q-learning application.
"""

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
