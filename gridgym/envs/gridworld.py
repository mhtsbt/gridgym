from gym.spaces import Discrete
import math
import numpy as np
from gridgym.envs.envbase import BaseEnv


class GridworldEnv(BaseEnv):

    metadata = {'render.modes': ['human']}

    def __init__(self):

        self.grid_size = 10
        self.states_count = 0
        self.grid = None
        self.state_visitation = None

        # action-space
        self._action_set = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        self._action_meaning = ["^", "<", "v", ">"]
        self.action_space = Discrete(len(self._action_set))

        self.set_grid_size(self.grid_size)

        self.start_state = None
        self.goal_state = None
        self.position = [1, 1]
        self.reset()

    def get_goal(self, v='bottom', h='right'):
        # return interesting goal positions
        # for now return bottom right, TODO: other goals
        return self.states_count-1

    def set_grid_size(self, grid_size):
        self.grid_size = grid_size
        self.states_count = self.grid_size ** 2
        self.observation_space = Discrete(self.states_count)

        self.grid = np.zeros(shape=(self.grid_size, self.grid_size))
        self.reset_visitation()

    def reset_visitation(self):
        self.state_visitation = np.zeros(shape=self.states_count, dtype=int)

    def get_visitation_map(self):
        return np.reshape(self.state_visitation, newshape=(self.grid_size, self.grid_size))

    def render(self, mode='human'):
        pass

    def reset(self, start_state=None, goal_state=None):

        self.goal_state = goal_state

        if start_state is None:
            start_state = self._position_to_state([1, 1])

        self.position = self._state_to_position(start_state)

        # keep track of the start state
        self.start_state = start_state

        if self.grid[self.position[0]][self.position[1]] == self.WALL_TILE:
            raise ValueError('starting position is a non-valid position')

        return self._position_to_state(self.position)

    def step(self, action):

        action_pos = self._action_set[action]
        new_position = np.add(self.position, action_pos)

        reward = 0
        done = False

        try:
            if self.grid[new_position[0]][new_position[1]] is self.FREE_TILE:
                self.position = new_position
        except:
            # position out or range
            self.position = self.position

        result_state = self._position_to_state(self.position)

        # give reward to agent (sparse, only on reaching the goal)
        if result_state == self.goal_state:
            done = True
            reward = 1

        # keep track of visit
        self.state_visitation[result_state] += 1

        return result_state, reward, done, {}
