import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# figure, axes = plt.subplots(2, 2)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

figures, axes = plt.subplots(2, 2)

# At [0, 0] position
axes[0, 0].plot(x, x*2, color="red")
axes[0, 0].set_title("2x Graph")

# At [0, 1] position
axes[0, 1].plot(x, x ** 2, color="blue")
axes[0, 1].set_title("x^2 Graph")

# At [1, 0]
axes[1, 0].plot(x, x ** 3, color="green")
axes[1, 0].set_title("x^3 Graph")

# At [1, 1]
axes[1, 1].plot(x, x ** 4, color="purple")
axes[1, 1].set_title("x^4 Graph")

plt.tight_layout()
plt.show()
