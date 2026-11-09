import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 30])

# Title
plt.title("Class Size", fontsize=20, family="Times New Roman", color="#2d4cfc", fontweight="bold")

# Axis Labels
plt.xlabel("Year", fontsize=20, family="Times New Roman", fontweight="bold", color="#2d4cfc")
plt.ylabel("Students", fontsize=20, family="Times New Roman", fontweight="bold", color="#2d4cfc")


# Plotting Points
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

# Customising the X Axis
plt.xticks(x)
plt.tick_params(axis="both", colors="#2dbefc")


# Showing Plot
plt.show()