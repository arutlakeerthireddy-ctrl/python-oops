'''Problem 1
Create a base class Animal.
Subclasses:
Dog
Cat
Each class should implement: sound method()
Expected:
Dog → "Bark"
Cat → "Meow"'''
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog bark")
class Cat(Animal):
    def sound(self):
        print('Cat meow')
d=Dog()
c=Cat()
d.sound()
c.sound()
'''Dog bark
Cat meow'''\

'''Problem 2
Create base class:
Employee
Subclasses:
Manager
Developer
Intern
Each employee has:
name
salary
Manager gets bonus salary.
Developer gets project allowance.
Intern gets stipend.
Create:
calculate_salary()'''
class Employee:
    def calculate_salary(self):
        pass
class Manager(Employee):
    def calculate_salary(self):
        print('Manager gets bonus salary')
class Developer(Employee):
    def calculate_salary(self):
        print('Developer gets project allowance')
class Intern(Employee):
    def calculate_salary(self):
        print('Intern gets stipend')
c1=Manager()
c2=Developer()
c3=Intern()
c1.calculate_salary()
c2.calculate_salary()
c3.calculate_salary()
'''Manager gets bonus salary
Developer gets project allowance
Intern gets stipend'''

'''Problem 3
Create abstract class:
Shape
Abstract method:
area()
Subclasses:
Circle
Rectangle
Triangle
Calculate respective areas.'''
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print("Area of circle:",3.14*self.r*self.r)
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area of rectangle:",self.l*self.b)
class Triangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        print("Area of triangle:",0.5*self.b*self.h)
c=Circle(6)
r=Rectangle(3,4)
t=Triangle(8,9)
c.area()
r.area()
t.area()
'''
Area of circle: 113.03999999999999
Area of rectangle: 12
Area of triangle: 36.0
'''

