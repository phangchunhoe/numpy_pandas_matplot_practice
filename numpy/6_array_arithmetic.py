import numpy as np

arr1 = np.arange(1, 5).reshape(2, 2)
arr2 = np.arange(5, 9).reshape(2, 2)
print(f"Array 1: \n{arr1} \n\nArray 2: \n{arr2} \n\n")

# # Element Wise 
# elementMultiplication = arr1 * arr2
# print(elementMultiplication)
# print("\n\n")

# # Matrix Multiplication
# # np.matmul() = np.dot() = __ @ __
# print(arr1 @ arr2) 
# print("\n\n")
# print(np.matmul(arr1, arr2)) # Does the same thing
# print("\n\n") # Works with np.matmul

# Finding the Determinanat
det = np.linalg.det(arr1)
print(f"\n\n Determinant: {det}\n\n")

# Finding the Inverse
inverse = np.linalg.inv(arr2)
print(inverse)

# Solving Simulataneous Equations
A = np.array([[3, 2], [5, 1]])
b = np.array([7, 11])
x = np.linalg.solve(A, b)
print(f"\nValue of x: {x[0]}, y = {x[1]}\n\n")

# Statistics Operatiosn
data = np.array([12, 15, 18, 21, 24, 27, 30, 33, 36])

print("Data:", data)
print("\nBasic Statistics:")
print(f"Sum: {np.sum(data)}")
print(f"Mean (average): {np.mean(data)}")
print(f"Median: {np.median(data)}")
print(f"Standard deviation: {np.std(data)}")
print(f"Variance: {np.var(data)}")
print(f"Minimum: {np.min(data)}")
print(f"Maximum: {np.max(data)}")

# Finding Positions of Min/Max
print(f"Index of minimum: {np.argmin(data)}")
print(f"Maximum value: {np.max(data)}")
print(f"Index of maximum: {np.argmax(data)}")

# Finding Positions in 2D Array
data_2d = np.array([[12, 45, 23],
                    [67, 31, 89],
                    [15, 78, 34]])

print("\n\n2D Array:")
print(data_2d)
print(f"\nMaximum value: {np.max(data_2d)}")
print(f"Flat index of maximum: {np.argmax(data_2d)}\n")

# Finding the percentile
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("\n\nData:", data)
print(f"\n25th percentile (Q1): {np.percentile(data, 25)}")
print(f"50th percentile (Median/Q2): {np.percentile(data, 50)}")
print(f"75th percentile (Q3): {np.percentile(data, 75)}")
print(f"\n90th percentile: {np.percentile(data, 90)}")