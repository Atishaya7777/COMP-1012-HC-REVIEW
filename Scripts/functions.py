'''
Reusable blocks of code
'''


def greet(name):
    print("Hello {}!".format(name))


greet("Castle")
greet("Bobby")

'''
Calling other functions
'''


def square(x):
    return x * x


def sum_of_squares(a, b):
    return square(a) + square(b)


print(sum_of_squares(3, 4))  # Output: 25
