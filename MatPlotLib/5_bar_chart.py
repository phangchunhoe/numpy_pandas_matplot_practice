import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4, 3, 2, 5, 3, 1])

# Call this to create BAR CHARTs
plt.bar(categories, values, color="skyblue")

# # To call horizontal bar:
# plt.barh(categories, values)

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()