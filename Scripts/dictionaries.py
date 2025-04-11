'''
Accessing values via key
'''
person = {
    "name": "Alice",
    "age": 30,
    "job": "Engineer"
}

print(person["name"])  # Output: Alice

'''
Uniqueness of keys and Immutability of keys
'''
# Valid key types: string, number, tuple (immutable types)
my_dictionary = {
    1: "one",
    "two": 2,
    (3, 4): "three-four",
}

print(my_dictionary[(3, 4)])  # Output: three-four

'''
Useful Dictionary methods
'''
student = {
    "name": "Castle",
    "grade": "A+",
    "passed": True
}

print(student.keys())    # dict_keys(['name', 'grade', 'passed'])
print(student.values())  # dict_values(['Castle', 'A', True])
# dictionary_items([('name', 'Castle'), ('grade', 'A'), ('passed', True)])
print(student.items())
