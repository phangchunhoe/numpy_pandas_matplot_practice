import pandas as pd

df = pd.read_csv("../../Lab 2/kyphosis.csv")

# Getting Rows out with a specific condition
no_kyphosis = df[df["Kyphosis"] == "absent"]

# Using logic operators for specific conditions
print(df[(df["Age"] > 0) & (df["Age"] < 50)])
