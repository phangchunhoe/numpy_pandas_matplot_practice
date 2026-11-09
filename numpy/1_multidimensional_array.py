import numpy as np

# Learning Dimensions
array = np.array([
                  [['A', 'B', 'C'], 
                   ['D', 'E', 'F']],
                   
                   [['A', 'B', 'C'], 
                    ['D', 'Z', 'F']],
                ])

# * Use 'ndim' to check how many dimensions are in the array
print(array.ndim)
print(array)

# use the 'shape' attribute. 
# it returns a tuple of integers
# it is formatted in (row, column, depth)
print(array.shape)

# Indexing
print(array[0][1][1]) # You can use this conventional way
print(array[0, 1, 1]) # This gets the work done the same way



