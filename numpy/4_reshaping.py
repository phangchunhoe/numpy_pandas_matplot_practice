import numpy as np

arr1 = np.arange(1, 25)
print(arr1)
print('\n\n')

# Use .reshape to give it the shape that you want
# .reshape(rows, columns)
arr2 = arr1.reshape(6, -1)
print(arr2)
print("\n\n\n")

# Can make it to 3D
arr3 = arr1.reshape(4, 3, 2)
print(arr3)
print("\n\n\n")


# Reduce the dimension size strictly to 1D
arr4 = arr1.flatten()
print(arr4)
print("\n\n\n")

# Transpose Arrays
arr5 = arr2.T 
# similarly, this works too 
arr5 = np.transpose(arr2)
print(arr5)