class Car:
    """
    A simple Car class with basic attributes.
    """
    brand = "Toyota"  


car1 = Car()
car2 = Car()

print(car1.brand) 
print(car2.brand)



class Student:
    """
    Student class with constructor method.
    """
    def __init__(self, name, grade):
        self.name = name      
        self.grade = grade    

student1 = Student("Alice", 90)
student2 = Student("Bob", 85)

print(student1.name, student1.grade)
print(student2.name, student2.grade)



class BankAccount:
    """
    BankAccount class to demonstrate methods.
    """
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Adds money to the account balance.
        """
        self.balance += amount
        print("New balance:", self.balance)

    def withdraw(self, amount):
        """
        Subtracts money if sufficient balance exists.
        """
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful. New balance:", self.balance)
        else:
            print("Insufficient funds.")

account1 = BankAccount("Alice", 1000)

account1.deposit(200)
account1.withdraw(500)



class Employee:
    """
    Demonstrates difference between class and instance variables.
    """
    company = "TechCorp"   

    def __init__(self, name, salary):
        self.name = name       
        self.salary = salary    

emp1 = Employee("John", 50000)
emp2 = Employee("Emma", 60000)


print(emp1.company)
print(emp2.company)

Employee.company = "InnovateTech"

print(emp1.company)
print(emp2.company)

emp1.salary = 55000

print(emp1.salary) 
print(emp2.salary)  



class Person:
    """
    Demonstrates modifying and deleting attributes.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)


person1.age = 26
print(person1.age)


del person1.age

del person1