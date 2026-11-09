import pandas as pd

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

# print(df.loc["Employee 1"])
# print(df.iloc[0])

# Adding a new Column
df["Job"] = ["Cook", "N/A", "Cashier"]

print(df)

# Adding a new Row
new_row = pd.DataFrame([{
    "Name": "Sandy",
    "Age": 28,
    "Job": "Engineer"
}], index=["Employee 4"])


# Adding new Rows
new_rows = pd.DataFrame([{
    "Name": "Sandy",
    "Age": 28,
    "Job": "Engineer"
}, {
    "Name": "Eugene",
    "Age": 60,
    "Job": "Manager"
}], index=["Employee 5", "Employee 6"])

df = pd.concat([df, new_rows])
print(df)
