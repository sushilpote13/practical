
from collections import deque

# Grid: 0 = Free cell, 1 = Obstacle
grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

# Starting and goal positions
start = (0, 0)
goal = (3, 3)

# Movement directions: Right, Down, Left, Up
directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]


def bfs():

    queue = deque([start])

    visited = {start}

    parent = {start: None}

    explored = []

    while queue:

        current = queue.popleft()

        explored.append(current)

        # Check whether goal is reached
        if current == goal:
            break

        row, col = current

        # Generate neighbouring states
        for dr, dc in directions:

            new_row = row + dr
            new_col = col + dc

            new_state = (new_row, new_col)

            # Check grid boundaries
            if (0 <= new_row < len(grid) and
                0 <= new_col < len(grid[0])):

                # Check obstacle and visited state
                if (grid[new_row][new_col] == 0 and
                    new_state not in visited):

                    visited.add(new_state)

                    parent[new_state] = current

                    queue.append(new_state)

    # Reconstruct shortest path
    path = []

    if goal not in parent:
        return None, explored

    current = goal

    while current is not None:

        path.append(current)

        current = parent[current]

    path.reverse()

    return path, explored


# Execute BFS
path, explored = bfs()

print("Robot Path Planning using BFS")

print("\nExplored States:")

for step, state in enumerate(explored, 1):
    print(f"State {step}: {state}")

print("\nShortest Path:")

if path:
    for step, state in enumerate(path):
        print(f"Step {step}: {state}")

    print("\nTotal Moves:", len(path) - 1)
    print("Goal Reached Successfully!")

else:
    print("No path found!")
