# Inheritance
class Animal:
    def __init__(self, name: str):
        self.name = name

# Define the child class that inherits from Animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

# --- Running the code ---

# 1. Instantiate a Dog object
my_dog = Dog("Buddy")

# 2. Invoke the inherited attribute and unique subclass method
print(my_dog.bark())