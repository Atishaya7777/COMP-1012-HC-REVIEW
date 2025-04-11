'''
Global vs Local variable
'''

x = 10  # Global variable


def my_func():
    x = 5  # This is a local variable — completely separate from the global x
    print("Inside function:", x)


my_func()
print("Outside function:", x)


'''
Trying to modify global variable inside of a function
'''


count = 0  # Global variable


def increment():
    count = count + 1  # ❌ This will raise an error
    print("Inside function:", count)


increment()

'''
Correct way:
'''

count = 0


def increment():
    global count
    count = count + 1
    print("Inside function:", count)


increment()
print("Outside function:", count)
