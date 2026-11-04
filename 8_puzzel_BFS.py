from collections import deque

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

def bfs():
    queue = deque([(start, [])])
    visited = {start}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        for dr, dc in directions:
            r, c = row + dr, col + dc

            if 0 <= r < 3 and 0 <= c < 3:
                new_zero = r * 3 + c

                new_state = list(state)
                new_state[zero], new_state[new_zero] = (
                    new_state[new_zero], new_state[zero]
                )

                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

    return None


solution = bfs()

print("Initial State:")
display(start)

if solution is not None:
    print("\nSolution Path:")

    for step, state in enumerate(solution, 1):
        print("\nStep", step)
        display(state)

    print("\nTotal Moves:", len(solution))
    print("Goal Reached!")
else:
    print("No solution found!")