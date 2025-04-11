'''
Mutability of Lists
'''
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Change 'banana' to 'blueberry'
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

'''
Homogeneous storage of Lists
'''
my_list = [42, "hello", 3.14, True, [1, 2, 3]]
print(my_list)

'''
Slicing lists: list[start:end:step]
'''
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:7])        # [2, 3, 4, 5, 6]
print(numbers[::2])        # [0, 2, 4, 6, 8]
print(numbers[5:2:-1])     # [5, 4, 3]
print(numbers[::-1])       # Reversed list: [9, 8, ..., 0]
