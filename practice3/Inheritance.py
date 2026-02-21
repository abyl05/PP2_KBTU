class Animal:
    """
    Parent class
    """
    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    pass  

dog1 = Dog()

dog1.speak()



class Person:
    """
    Parent class
    """
    def __init__(self, name):
        self.name = name

class Student(Person):
    """
    Child class
    """
    def __init__(self, name, grade):
        super().__init__(name) 
        self.grade = grade

student1 = Student("Alice", 90)

print(student1.name)
print(student1.grade)



class Bird:
    """
    Parent class
    """
    def sound(self):
        print("Bird makes a sound.")

class Parrot(Bird):
    """
    Child class overriding method
    """
    def sound(self):
        print("Parrot says hello!")

bird1 = Bird()
parrot1 = Parrot()

bird1.sound()
parrot1.sound()



class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        super().start()  
        print("Car engine is ready!")

car1 = Car()
car1.start()




class Father:
    def skills(self):
        print("Gardening, Driving")

class Mother:
    def talents(self):
        print("Cooking, Painting")

class Child(Father, Mother):
    pass

child1 = Child()

child1.skills()
child1.talents()




from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class
    """
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 4)
print(rect.area())
