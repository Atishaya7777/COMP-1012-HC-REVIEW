import numpy as np

'''
Fixed length, indexable arrays
'''
arr = np.array([10, 20, 30])
print(arr[0])  # Output: 10
arr[0] = 99     # You CAN update values
print(arr)      # Output: [99 20 30]

# BUT you can't append() like with lists - Numpy arrays are fixed-size
# arr.append(50)  # ❌ This will raise an error: AttributeError

'''
Creating arrays from lists, ranges, zeroes
'''

a = np.array([1, 2, 3])
b = np.arange(5)  # Like range(), but returns a Numpy array
c = np.zeros(4)  # Array of 4 zeroes
d = np.ones(3) * 7  # [7. 7. 7]

print(a, b, c, d)

'''
Vectorized Operations (Element-Wise Math)
'''
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print(x + y)    # Output: [11 22 33]
print(x * 2)    # Output: [2 4 6]
print(y > 15)   # Output: [False  True  True]
