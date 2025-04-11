'''
Factorial function example
'''


def factorial(n):
    # Base case: When n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: Call the function with a reduced value of n
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120

'''
Fibonacci Sequence example
'''


def fibonacci(n):
    # Base case: First two numbers in the Fibonacci sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: Sum of the previous two numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # Output: 5
