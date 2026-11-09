import numpy as np

# # Vertically Stacking 2 1D Arrays
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# vstack = np.vstack((arr1, arr2))
# print(vstack)
# print("\n\n")

# # Vertically 2 2D Arrays 
# arr3 = np.arange(1, 7)
# arr3 = arr3.reshape(2, 3)
# arr4 = np.array([7, 8, 9])
# vstack2 = np.vstack((arr3, arr4))
# print(vstack2)

# # Horizontally Stacking Arrays
# arr5 = np.arange(1, 4)
# arr6 = np.arange(4, 7)
# hstack = np.hstack((arr5, arr6))
# print(hstack)
# print("\n\n")

# # Horizontal Stacks with 2D Arrays
# arr7 = np.array([[1, 2, 3], [4, 5, 6]])
# arr8 = np.array([[7, 8, 9], [10, 11, 12]])
# hstack2 = np.hstack((arr7, arr8))
# print(hstack2)

# # Concentenation
# arr9 = np.arange(1, 7).reshape(2, 3)
# arr10 = np.arange(7, 13).reshape(2, 3)
# concat_axis0 = np.concatenate((arr9, arr10), axis=0)
# print(concat_axis0)
# print("\n\n")
# concat_axis1 = np.concatenate((arr9, arr10), axis=1)
# print(concat_axis1)
# print("\n\n")

# Row Stack (same as vstack)
arr11 = np.arange(1, 7).reshape(2, 3)
arr12 = np.arange(7, 13).reshape(2, 3)
row_stack = np.row_stack((arr11, arr12))
print(row_stack)
print("\n\n")

# Column Stack (same as hstack)
arr11 = np.arange(1, 7).reshape(2, 3)
arr12 = np.arange(7, 13).reshape(2, 3)
column_stack = np.column_stack((arr11, arr12))
print(column_stack)
print("\n\n")

