import numpy as np

'''
2D Numpy arrays are just arrays of arrays
'''
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

'''
Indexing: arr[row][col] or arr[row, col]
'''
print(matrix[0][1])      # Output: 2
print(matrix[0, 1])      # Also output: 2 (preferred NumPy syntax)

'''
Slicing: Row, then Column -> arr[row_start:row_end, col_start:col_end]
'''
print(matrix[0:2, 1:3])

'''
Useful tricks:
'''
print(matrix[1])        # Entire 2nd row: [4 5 6]
print(matrix[:, 2])     # Entire 3rd column: [3 6 9]
