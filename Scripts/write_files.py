'''
Writing to a file
'''

with open("output.txt", "w") as file:  # This will create a new file called output.txt
    file.write("Hello, world!\n")
    file.write("This will overwrite any existing content.\n")

'''
Appending a file
'''
with open("output.txt", "a") as file:
    file.write("This line will be added to the end.\n")
