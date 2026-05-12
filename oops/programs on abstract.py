'''shape Area (Basic)
Create an abstract class Shape
Method:
area()
Create child classes:
Circle
Rectangle
Each should implement area().'''
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print("area of circle is",3.14*self.r*self.r)
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("area of rectangle is",self.l*self.b)
c=Circle(5)
c.area()
c1=Rectangle(2,4)
c1.area()

'''2. Vehicle System
Create abstract class Vehicle
Method:
start()
Create child classes:
Car
Bike'''
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car starts")
class Bike(Vehicle):
    def start(self):
        print("bike starts")
c=Car()
c.start()
b=Bike()
b.start()
