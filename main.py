from env import Environment
from brain import Brain

"""
Q-learning application.
"""


class Runner(object):

    def __init__(self, env, brain):
        self.env = env
        self.brain = brain
        self.n_states = 6
        self.actions = ["left", "right"]
        self.max_episodes = 10
        self.fresh_time = 0.3
        self.alpha = 0.1
        self.gamma = 0.9

    def start(self):

        q_table = self.brain.build_q_table(self.n_states, self.actions)

        for episode in range(self.max_episodes):

            step_counter = 0
            S = 0
            is_terminated = False
            self.env.update_env(S, episode, step_counter, self.n_states, self.fresh_time)

            while not is_terminated:

                A = self.brain.choose_action(S, q_table, self.actions)
                S_, R = self.brain.get_env_feedback(S, A, self.n_states)
                q_predict = q_table.loc[S, A]
                if S_ != 'terminal':
                    q_target = R + self.gamma * q_table.iloc[S_, :].max()
                else:
                    q_target = R
                    is_terminated = True

                q_table.loc[S, A] += self.alpha * (q_target - q_predict)
                S = S_

                self.env.update_env(S, episode, step_counter + 1, self.n_states, self.fresh_time)
                step_counter += 1

        print('\r\nQ-table:\n')
        print(q_table)


if __name__ == "__main__":
    runner = Runner(Environment(), Brain())
    print("\r\n1-D Treasure Hunting Adventure Using Q-Learning:\n")
    runner.start()
