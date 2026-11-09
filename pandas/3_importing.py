import pandas as pd

# # If you want to specify how to address each column: 
# df = pd.read_csv("../../Lab 2/kyphosis.csv", index_col="Age")
df = pd.read_csv("../../Lab 2/kyphosis.csv")

# # Use df.to_string() to print out the whole list
# # Selection by Column
# # print(df["Kyphosis"])
# print(df["Age"])
# print("\n\n")

# # To display multiple SPECIFIC column
# print(df[["Kyphosis", "Age", "Start"]])

# Selection by ROW/S
# Select index AND column
print(df.loc[71, ["Kyphosis", "Start"]])

# Selecting a Range
# Follow the syntax of [start : end : step]
print(df.loc[0:49:2, ["Kyphosis", "Start"]])

# Selection based on position
print(df.iloc[0:49:2, 0:3])

