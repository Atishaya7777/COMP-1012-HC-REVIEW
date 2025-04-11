'''
Uniqueness of sets
'''
numbers = {1, 2, 3, 2, 1}
print(numbers)  # Output: {1, 2, 3}

'''
Sets are NOT indexable
'''
my_set = {"apple", "banana", "cherry"}

# print(my_set[0])  # ❌ TypeError: 'set' object is not subscriptable

'''
Set theoretic operations: Union, Intersection, Difference
'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))  # Union: {1, 2, 3, 4, 5, 6}
print(a.intersection(b))  # Intersection: {3, 4}
print(a.difference(b))  # Difference: {1, 2}
print(b.difference(a))  # Difference (other way): {5, 6}
