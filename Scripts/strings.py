'''
Immutability of strings
'''

name = "Castle"
# Try to change the first character
# name[0] = "M"  # ❌ This will raise an error: TypeError

# Instead, we create a new string
new_name = "F" + name[1:]
print(new_name)  # Output: Fastle


'''
Indexed and slicing
'''
greeting = "Hello"

print(greeting[0])  # Output: H
print(greeting[1])  # Output: e
print(greeting[-1])  # Output: o (last character)
print(greeting[::2])  # Output: Hlo (Skips every second letter)
