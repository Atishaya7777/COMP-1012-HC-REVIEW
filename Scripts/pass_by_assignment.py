'''
Immutable types -> Passed by Value
'''


def modify_num(n):
    n = n + 5
    print("Inside function:", n)


x = 10
modify_num(x)
print("Outside function:", x)  # x is still 10

'''
Mutable types -> Passed by Reference
'''


def modify_list(my_list):
    my_list.append(4)
    print("Inside function:", my_list)


numbers = [1, 2, 3]
modify_list(numbers)
print("Outside function:", numbers)  # numbers is now [1, 2, 3, 4]
