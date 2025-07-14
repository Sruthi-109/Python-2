#1. How do you define a class in Python?

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
p1 = Person("Alice", 25)
p1.greet()

#2.	How do you create an object in Python?

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def display_info(self):
        print(f"{self.brand}, {self.year}")
my_car = Car("Ford", 2023)
my_car.display_info()

#3.	What is the purpose of the _init_() method?

#The __init__() method in Python is a special method (also called a constructor) that is automatically called when a new object of a class is created.
# Purpose of __init__():
#To initialize the object’s attributes (also called instance variables).
#To set up the object with default or user-provided values.
#Ex
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def show(self):
        print(f"Name: {self.name}, Grade: {self.grade}")
s1 = Student("Alice", "A")
s1.show()

#4.	What is the use of self keyword in class methods?

#The self keyword in Python is used within class methods to refer to the current instance of the class.
# Main Uses of self:
#Access instance variables (e.g., self.name)
#Call other instance methods (e.g., self.method_name())
#Differentiate between instance variables and local variables
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
    p1 = Person("Alice", 30)
    p1.greet()

#5.	What is the difference between a method and a function in Python?

#Feature	                    Function	                           Method
#Definition	         Defined outside of a class	            Defined inside a class
#Calling	             Called directly using its name     	Called on an object using dot syntax
#First Argument	     No special first argument	            Always takes self (or cls) as the first argument
#Example	             def greet():	                        def greet(self): in a class

def add(a, b):
    return a + b
print(add(2, 3))
#Example of a Method:
class Calculator:
    def add(self, a, b):
        return a + b
calc = Calculator()
print(calc.add(2, 3))

#6.	What is Object-Oriented Programming?

#Object-Oriented Programming (OOP) is a programming paradigm based on the concept of “objects”, which are instances of classes. It allows you to model real-world entities using code by combining data (attributes) and behavior (methods) into a single unit called a class.
# Key Concepts of OOP:
#Class:
#A blueprint for creating objects. Defines properties (attributes) and behaviors (methods).
#Object:
#An instance of a class. It holds actual data and can perform actions defined by the class.
#Encapsulation:
#Hiding internal data and exposing only what’s necessary. Achieved using private/public members.
#Inheritance:
#A class (child) can inherit attributes and methods from another class (parent).
#Polymorphism:
#Different classes can define methods with the same name but different behaviors.
#Abstraction:
#Hiding complex implementation details and showing only the essential features.
#Example:
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")
dog = Dog("Buddy")
dog.speak()

#7.	How to Define a Class Method

#A class method is a method that operates on the class itself, not on individual instances. You define it using the @classmethod decorator and it takes cls as its first parameter (not self).
class Student:
    school_name = "ABC School"
    def __init__(self, name):
        self.name = name
    @classmethod
    def get_school_name(cls):
        return cls.school_name
print(Student.get_school_name())
s1 = Student("Alice")
print(s1.get_school_name())