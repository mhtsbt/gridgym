import copy
import matplotlib.pyplot as plt
import numpy as np


def visualize_policy(q, env):

    grid = copy.deepcopy(env.grid)
    action_meaning = env._action_meaning

    plt.figure(figsize=(env.grid_size/2, env.grid_size/2))

    policy = np.zeros(shape=(env.grid_size, env.grid_size), dtype=int)

    # get the index of the highest action-value for each state
    for state, action_values in enumerate(q):
        position = env._state_to_position(state)
        policy[position[0]][position[1]] = np.argmax(action_values)
        grid[position[0]][position[1]] = action_values[0]

    for row in range(len(policy)):
        for col in range(len(policy[0])):

            if env.grid[row][col] != env.WALL_TILE:
                plt.text(y=row, x=col, s=action_meaning[policy[row][col]], color='w', ha="center", va="center")

    # give the goal state a color on the map
    goal_position = env._state_to_position(env.goal_state)
    #grid[goal_position[0]][goal_position[1]] = 3
    plt.text(y=goal_position[0], x=goal_position[1], s="G", color='w', ha="center", va="center")

    # give the starting state also a color
    if env.start_state is not None:
        start_position = env._state_to_position(env.start_state)
        #grid[start_position[0]][start_position[1]] = 5

    plt.imshow(grid)

    return plt