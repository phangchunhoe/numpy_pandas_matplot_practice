import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("pokemon.csv")

# Use value_counts to find the total of everything 
# (similar to summary)
type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="#03dffc", edgecolor="black")
plt.title("Number of Pokemons by Primary Types")
plt.xlabel("Count")
plt.ylabel("Type")

# Use this function if you are in a tight layout
plt.tight_layout()

plt.show()