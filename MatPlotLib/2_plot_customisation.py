import matplotlib.pyplot as plt
import numpy as np

x = np.array([20241, 20242, 20251, 20252, 20261])
y1 = np.array([3.98, 3.98, 3.92, 4.00, 4.00])
y2 = np.array([3.22, 3.88, 3.23, 4.00, 4.00])
y3 = np.array([3.42, 3.58, 3.46, 3.66, 3.23])

# Create a style dictionary
line_style = dict(marker=".", 
                markersize=15, 
                markerfacecolor="#1cd3fc",
                markeredgecolor="#1cd3fc", 
                linestyle="solid",
                linewidth=2)

# Use plt.plot() to plot your x and y values
# The `*` is used to UNPACK the style attributes 
plt.plot(x, y1, color ="#1c5bfc", **line_style)
plt.plot(x, y2, color = "#1cfc45", **line_style)
plt.plot(x, y3, color = "#fc1c1c", **line_style)

plt.show()