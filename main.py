from env import Environment
from brain import Brain

"""
A simple example for Reinforcement Learning using table lookup Q-learning method.
An agent "o" is on the left of a 1 dimensional world, the treasure is on the rightmost location.
Run this program and to see how the agent will improve its strategy of finding the treasure.

Q-learning application.
"""


class Runner:

    def __init__(self, env, brain):
        self.env = env
        self.brain = brain

    def start(self):
        q_table = self.brain.build_q_table()

        for episode in range(self.brain.max_episode):
            step_counter = 0
            S = 0
            is_terminated = False
            self.env.update_env()

            while not is_terminated:
                A = self.brain.choose_action(S, self.brain.q_table)
                self.brain.S_, self.brain.R = self.brain.get_env_feedback(S, A)
                q_predict = q_table.loc[S, A]
                if self.brain.S_ != "terminal":
                    q_target = self.brain.R + self.brain.gamma * self.brain.q_table.iloc[self.brain.S_, :].max()
                else:
                    q_target = self.brain.R
                    is_terminated = True

                q_table.loc[S, A] += self.brain.alpha * (q_target - q_predict)
                S = self.brain.S_

                self.env.update_env(S, self.evn.episode, step_counter + 1, self.brain.n_states)

                step_counter += 1

            print(q_table)


if __name__ == "__main__":
    Brain = Brain()
    Env = Environment(0, 0, 0, 0)
    runner = Runner(Env, Brain)
    print("\r\nQ-table:\n")
    runner.start()
