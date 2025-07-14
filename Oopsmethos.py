#1.	Create a class Person with instance attributes name and age. Write an instance method display() that prints the name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
p1 = Person("Ajay", 25)
p1.display()

#2.	Create a class Employee with attributes name and salary. Write an instance method update_salary() to update the salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated to: {self.salary}")
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
emp1 = Employee("John", 50000)
emp1.display()
emp1.update_salary(80000)
emp1.display()

#3.	Create a class BankAccount with   “balance attribute deposit() and withdraw()” instance methods.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}, New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}, Remaining Balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")
    def display_balance(self):
        print(f"Current Balance: {self.balance}")
account = BankAccount(1000)
account.display_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)

#4.	Create a class Student with  Attributes  name, marks (list) Method: average() → returns average marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        if self.marks:
            return sum(self.marks) / len(self.marks)
        else:
            return 0
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, Average: {self.average():.2f}")

s1 = Student("Alice", [85, 90, 78, 92])
s1.display()
s2 = Student("Bob", [])
s2.display()

#5.	Difference Between Class Method and Instance Method.

 #Instance Method vs Class Method
#Feature	                 Instance Method	                      Class Method
#Defined with	        Regular def inside class	            Decorated with @classmethod
#First parameter        self → refers to the instance	        cls → refers to the class
#Accesses	            Instance attributes and methods	        Class attributes and other class methods
#Called using	        Object (instance) of the class	        Class name or object (both work)
#Purpose	            Operate on individual object data	    Operate on class-level data or provide alternate constructors
class Example:
    class_var = "I am a class variable"
    def __init__(self, data):
        self.data = data
    def instance_method(self):
        print("Instance Method:", self.data)
    @classmethod
    def class_method(cls):
        print("Class Method:", cls.class_var)
obj = Example("Instance Data")
obj.instance_method()

obj.class_method() 