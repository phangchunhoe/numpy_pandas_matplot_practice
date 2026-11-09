import numpy as np

array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])
print(array)
print("\n\n")


# # Syntax: [start: end: step]
# print(array[::-2])
# print("\n\n")
# print(array[::2])

# If you want to select an index from all rows of the array
# Remember that the syntax is always array[ROW, COLUMN]
# so, array[:, x] represents ALL ROW, 
# array[x, :] represents all column; same as array[x]

# array[:, ::2] means every second element in the column
print(array[:, ::2])
print(array[:, ::-1]) # reverses the row order
print("\n\n")
print(array[:2, :2])