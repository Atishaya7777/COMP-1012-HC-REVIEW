'''
Print numbers from 0 to 4 using a while loop
'''

i = 0                     # start
while i < 5:              # condition
    print(i)
    i += 1                # increment

'''
Common mistake: Infinite loop
'''

i = 0
while i < 5:
    print(i)
    # i += 1 is missing — this will cause an infinite loop!
