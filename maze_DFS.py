# Maze Solving using DFS

maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

visited = set()
path = []

directions = [
    (1, 0),    # Down
    (0, 1),    # Right
    (-1, 0),   # Up
    (0, -1)    # Left
]

def dfs(row, col):

    if (row, col) == goal:
        path.append((row, col))
        return True

    if (row < 0 or row >= 5 or
        col < 0 or col >= 5 or
        maze[row][col] == 1 or
        (row, col) in visited):
        return False

    visited.add((row, col))
    path.append((row, col))

    for dr, dc in directions:
        if dfs(row + dr, col + dc):
            return True

    path.pop()
    return False


def print_maze():
    print("\nMaze Visualization:")

    for r in range(5):
        for c in range(5):

            if (r, c) == start:
                print(" S ", end="")

            elif (r, c) == goal:
                print(" G ", end="")

            elif maze[r][c] == 1:
                print(" # ", end="")

            elif (r, c) in path:
                print(" * ", end="")

            else:
                print(" . ", end="")

        print()


print("Maze Solving using DFS")

print("\nInitial Maze:")
print_maze()

if dfs(start[0], start[1]):

    print("\nPath Found:")

    for position in path:
        print(position)

    print("\nFinal Maze:")
    print_maze()

    print("\nGoal Reached Successfully!")

else:
    print("\nNo Path Found!")