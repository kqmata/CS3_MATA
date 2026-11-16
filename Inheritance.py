# Parent Class (Superclass)
class Vehicle:
    def move(self):
        print("MOVING FORWARD...", end=" ")

# Child Class (Subclass) inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        print("CAR DRIVING SMOOTHLY")

# Create an instance of the child class
my_car = Car()

# Call the inherited method and the child's own method
my_car.move()
my_car.drive()
