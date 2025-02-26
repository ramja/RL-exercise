import numpy as np
import random

# Grid World (4x4)
GRID_SIZE = 4
GOAL = (3, 2)
ACTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]  # King + NOP

# Learning parameters
ALPHA = 0.1  # Learning rate
GAMMA = 0.9  # Discount factor
EPSILON = 0.2  # Exploration probability
EPISODES = 100

# Reward matrix
REWARD_GRID = np.array([
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, -0.04, 0],
    [0, 0, 1, -0.1]
])

# Initialize Q-table (4x4 grid with 9 possible actions)
Q = np.zeros((GRID_SIZE, GRID_SIZE, len(ACTIONS)))

# Check if move is within bounds
def valid_move(x, y):
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE

# Q-learning algorithm
for episode in range(EPISODES):
    # Start at random position
    x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)

    # Choose action (ε-greedy)
    if random.uniform(0, 1) < EPSILON:
        action_index = random.randint(0, len(ACTIONS) - 1)  # Explore
    else:
        action_index = np.argmax(Q[x, y])  # Exploit

    # Apply action
    dx, dy = ACTIONS[action_index]
    new_x, new_y = (x + dx, y + dy) if valid_move(x + dx, y + dy) else (x, y)

    # Observe reward from REWARD_GRID
    r = REWARD_GRID[new_x, new_y]

    # Q-learning update
    Q[x, y, action_index] += ALPHA * (r + GAMMA * np.max(Q[new_x, new_y]) - Q[x, y, action_index])

    # Move agent
    x, y = new_x, new_y

# Extract optimal policy
optimal_policy = np.array([[np.argmax(Q[i, j]) for j in range(GRID_SIZE)] for i in range(GRID_SIZE)])


print("Optimal Policy:")
optimal_policy
