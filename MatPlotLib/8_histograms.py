import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)
scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins=20,
                color="lightgreen",
                edgecolor="black",)

# Adding Labels
plt.title("Exam Scores")
plt.xlabel("Score")
plt.ylabel("Number of students")

plt.show()