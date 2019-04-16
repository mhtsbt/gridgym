from gym.envs.registration import register

# register the environments as OpenAI gym environments
register(id='FourRoom-v0', entry_point='gridgym.envs.fourroom:FourRoomEnv')
register(id='Maze-v0', entry_point='gridgym.envs.maze:MazeEnv')

