'''
A class - Blueprint
'''


class Dog:
    def __init__(self, name, breed):
        self.name = name      # Property
        self.breed = breed    # Property

    def bark(self):           # Method
        print(f"{self.name} says woof!")

    def __str__(self):
        return f"The Dog is named {self.name}"


'''
Objects - Instance of a class
'''

my_dog = Dog("Buddy", "Golden Retriever")  # __init__ runs here!
print(my_dog.name)   # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
print(my_dog)        # Output: The Dog is named Buddy

my_dog.bark()        # Output: Buddy says woof!
