'''
Reading the entire file
'''

with open("example.txt", "r") as file:  # If you don't use with, you have to close the file
    contents = file.read()
    print(contents)

'''
Reading the file line by line
'''

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline at the end


'''
Reading a file and splitting the contents
'''
with open("data.txt", "r") as file:
    for line in file:
        words = line.strip().split()  # Splits on whitespace by default
        print(words)
