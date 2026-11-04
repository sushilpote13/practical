
from collections import deque

# Initial state: all disks are on peg A
# State represents the peg containing each disk (smallest to largest)
start = ('A', 'A', 'A')

# Goal state: all disks are on peg C
goal = ('C', 'C', 'C')

def get_moves(state):

    moves = []

    pegs = {
        'A': [], 'B': [], 'C': []
    }

    # Arrange disks on their respective pegs
    for disk, peg in enumerate(state):
        pegs[peg].append(disk)

    # Find the top disk of each peg
    for source in pegs:

        if not pegs[source]:
            continue

        disk = min(pegs[source])

        for destination in pegs:

            if source == destination:
                continue

            # Move only onto an empty peg or a larger disk
            if (not pegs[destination] or
                    disk < min(pegs[destination])):

                new_state = list(state)
                new_state[disk] = destination

                moves.append((tuple(new_state),
                              disk + 1, source, destination))

    return moves


def bfs():

    queue = deque([(start, [])])
    visited = {start}

    while queue:

        state, path = queue.popleft()

        if state == goal:
            return path

        for new_state, disk, source, destination in get_moves(state):

            if new_state not in visited:

                visited.add(new_state)

                queue.append((
                    new_state,
                    path + [(disk, source, destination)]
                ))

    return None


# Execute BFS
solution = bfs()

print("Tower of Hanoi using State Space Search")
print("\nInitial State:", start)

print("\nSolution Steps:")

for step, (disk, source, destination) in enumerate(solution, 1):
    print(f"Step {step}: Move Disk {disk} from {source} to {destination}")

print("\nGoal State:", goal)
print("Goal Reached Successfully!")
