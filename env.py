import time


class Environment:

    def __init__(self):
        pass

    def update_env(self, S, episode, step_counter, n_states, fresh_time):

        env_list = ['-'] * (n_states - 1) + ['T']
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
