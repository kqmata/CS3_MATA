#CS3 MATA EXERCISE 1 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Titoy", 67)
print(f"Name: {person1.name}, Age: {person1.age}")

# CS 3 MATA EXERCISE 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

person1 = Person("Titoy", 67)
print(f"Name: {person1.name}, Age: {person1.get_age()}")

#RELFECTION WHY IS IT BETTER TO ACCESS __AGE THROUGH GET_AGE()?
#Accessing __age through get_age() is better because it keeps the age attribute encapsulated inside the class. In Python, the double underscore triggers name mangling, which discourages direct access from outside the class. A getter provides a clear, controlled way to retrieve the value and lets the class change how it stores or validates age later without changing the code that uses it.


#CS 3 MATA EXERCISE 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


class Student(Person):
    def study(self):
        print(f"{self.name} is currently studying.")
student1 = Student("Titoy", 67)
print("Name:", student1.name)
print("Age:", student1.get_age())
student1.study()

#EXERCISE 4
class Teacher(Person):
    def teach(self):
        print(f"{self.name} is currently teaching.")

teacher1 = Teacher("Ms. Vanessa", 23)
print("Name:", teacher1.name)
print("Age:", teacher1.get_age())
teacher1.teach()

# EXERCISE 5
class Student(Person):
    def role(self):
        print(f"{self.name} is a student.")

class Teacher(Person):
    def role(self):
        print(f"{self.name} is a teacher.")

student1 = Student("Titoy", 67)
teacher1 = Teacher("Ms. Vanessa", 23)

print("Student role:")
student1.role()
print("Teacher role:")
teacher1.role()

#EXERCISE 6
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def role(self):
        print(f"{self.name} is a student.")

class Teacher(Person):
    def role(self):
        print(f"{self.name} is a teacher.")