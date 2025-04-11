'''
Iterative function to recursive: A Step by Step guide
'''


def sum_iterative(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i

    return sum


def sum_recursive_naive(n, sum, i):
    # Stopping condition
    if i > n:
        # Return the results when you want to terminate
        return sum
    else:
        # Update your counters and your parameters
        sum = sum + i
        i = i + 1
        # Converting the loop into recursive calls with updated arguments
        return sum_recursive_naive(n, sum, i)


def sum_recursive_better(n):
    # Base case: If n is 0, return 0
    if n == 0:
        return 0
    # Recursive case: Sum the current number n and the sum of the previous  numbers
    else:
        return n + sum_recursive_better(n - 1)


print(sum_iterative(5))
print(sum_recursive_naive(5, 0, 1))
print(sum_recursive_better(5))
