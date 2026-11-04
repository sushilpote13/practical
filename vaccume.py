
import random
import time

SIZE = 5

# Generate random dirt (0 = Clean, 1 = Dirty)
rooms = [[random.choice([0, 0, 1]) for j in range(SIZE)]
         for i in range(SIZE)]

rooms[0][0] = 0
robot_row, robot_col = 0, 0

# Display matrix
def display():
    print("\n+---" * SIZE + "+")
    for i in range(SIZE):
        print("|", end="")
        for j in range(SIZE):
            if (i, j) == (robot_row, robot_col):
                print(" R |", end="")
            elif rooms[i][j] == 1:
                print(" * |", end="")
            else:
                print("   |", end="")
        print("\n" + "+---" * SIZE + "+")

# Start simulation
print("INITIAL VACUUM CLEANER WORLD")
display()
time.sleep(0.6)

for i in range(SIZE):

    # Zigzag movement
    columns = range(SIZE) if i % 2 == 0 else range(SIZE - 1, -1, -1)

    for j in columns:
        robot_row, robot_col = i, j

        display()

        if rooms[i][j] == 1:
            print("Dirt Found! Action: SUCK")
            rooms[i][j] = 0
            print("Dirt Cleaned!")

        time.sleep(0.6)

print("\nALL CELLS SCANNED!")
print("FINAL ENVIRONMENT:")
display()
print("Cleaning completed successfully!")
