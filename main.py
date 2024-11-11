import numpy as np
import matplotlib.pyplot as plt
import random

# Generate a 21x21 grid with random values to represent heatmap data
gridSize = 21
heatmap = np.zeros((gridSize, gridSize))

def updateHeatmap(x, y):
    heatmap[x, y] += 1

# Simulating robot movement with dummy values.
def moveRobot(steps):
    x, y = gridSize // 2, gridSize // 2  # Start the robot in the middle of the grid.
    for _ in range(steps):
        updateHeatmap(x, y)

        # Simulate motor movement (dummy values)
        # leftMotor.run_angle(200, 360, wait=False)
        # rightMotor.runAngle(200, 360)
        # wait(1000)

        # Simulate sensor readings (dummy values)
        distance = random.randint(0, 500)  # Random distance between 0 and 500 cm
        angle = random.randint(0, 360)  # Random angle between 0 and 360 degrees

        if distance < 300:
            # Simulate obstacle avoidance
            # leftMotor.run_angle(200, 180, wait=False)
            # rightMotor.runAngle(200, -180)
            x += random.choice([-1, 1])
            y += random.choice([-1, 1])
        else:
            x += random.choice([-1, 0, 1])
            y += random.choice([-1, 0, 1])

        # Ensure the robot stays within the grid boundaries
        x = max(0, min(gridSize - 1, x))
        y = max(0, min(gridSize - 1, y))

# Simulate 1000 steps of robot movement.
moveRobot(1000)

# Plotting the heatmap
plt.imshow(heatmap, cmap="magma", interpolation="bicubic", extent=[-10, 10, -10, 10])
plt.title("Robot Heatmap")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.colorbar(label="Amount picked up")
plt.show()