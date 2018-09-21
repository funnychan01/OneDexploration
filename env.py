import time


class Environment:

    def __init__(self, S, episode, step_counter, n_states, fresh_time):
        self.S = S
        self.episode = episode
        self.step_counter = step_counter
        self.n_states = n_states
        self.fresh_time = fresh_time

    def update_env(self):
        # This is how environment be updated
        env_list = ['-'] * (self.n_states - 1) + ['T']  # '---------T' our environment
        if self.S == 'terminal':
            interaction = 'Episode %s: total_steps = %s' % (self.episode + 1, self.step_counter)
            print('\r{}'.format(interaction), end='')
            time.sleep(2)
            print('\r                                ', end='')
        else:
            env_list[self.S] = 'o'
            interaction = ''.join(env_list)
            print('\r{}'.format(interaction), end='')
            time.sleep(self.fresh_time)