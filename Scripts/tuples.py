'''
Immutability of tuples
'''
coordinates = (10, 20)

# Attempting to change a value
# ❌ TypeError: 'tuple' object does not support item assignment
# coordinates[0] = 15

'''
Indexing tuples
'''
person = ("Castle", 30, "Engineer")

print(person[0])  # Output: Castle
print(person[1])  # Output: 30

'''
Cannot append or insert to tuples
'''
colors = ("red", "green", "blue")

# colors.append("yellow")  # ❌ AttributeError
# colors.insert(1, "black")  # ❌ AttributeError

'''
Converting a tuple to a list. Making it mutable.
'''
colors = list(colors)
colors[0] = 'gg'
print(colors)
