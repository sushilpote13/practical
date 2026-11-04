# Water Jug Problem using DFS

jug1 = 4
jug2 = 3
goal = 2

visited = set()

def dfs(x, y):

    state = (x, y)

    if state in visited:
        return False

    visited.add(state)

    print("Jug 1:", x, "Jug 2:", y)

    # Check goal
    if x == goal:
        return True

    # Possible operations
    moves = [
        (jug1, y),                       # Fill Jug 1
        (x, jug2),                       # Fill Jug 2
        (0, y),                           # Empty Jug 1
        (x, 0),                           # Empty Jug 2
        (x - min(x, jug2-y), y + min(x, jug2-y)),  # Pour 1 to 2
        (x + min(y, jug1-x), y - min(y, jug1-x))   # Pour 2 to 1
    ]

    for new_x, new_y in moves:

        if dfs(new_x, new_y):
            return True

    return False


print("Water Jug Problem using DFS")

if dfs(0, 0):
    print("Goal Reached Successfully!")
else:
    print("Solution Not Found!")