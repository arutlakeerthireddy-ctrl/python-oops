#Create an abstract class Animal with an abstract method sound(). Implement it in a child class Dog.
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("Animal make sound")
class Dog(Animal):
    def sound(self):
        print("dog barks")
d=Dog()
d.sound()

#Design an abstract class Shape with an abstract method area(). Implement it for a Circle class.
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        print("area of shape")
class Circle(Shape):
    def area(self):
        print("Area of circle")
c=Circle()
c.area()
