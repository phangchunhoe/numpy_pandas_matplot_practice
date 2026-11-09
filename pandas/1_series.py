import pandas as pd

# # PanDas refers to Panel Data 

# data = [100, 102, 104, 200, 202]

# series = pd.Series(data, index=["a", "b", "c", "d", "e"])

# # # Locating Values
# # print(series.loc['a'])
# # print(series.iloc[1])


# # Filtering Values
# print(series[series < 200])

calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700,
}

series = pd.Series(calories)

# print(series)

# print(series.loc["Day 1"])

# series.loc["Day 3"] += 500

print(series)
print(series[series >= 2000])