#abstraction method:hiding implementation details and showing important features to user
#main concepts 
#1.abstract class:contains one or more abstract methods,used as blueprint for child class,cannot create objects directly
#example
from abc import ABC
class Animal(ABC):
    pass
#2.abstract method:declared without implementation
#created using @abstractmethod
#child classes must implement it
#ex:
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
#3.inheritance in abstraction:child classes inherit abstract classes and provide implementation for abstract methods
class dog(Animal):
    def sound(self):
        print("dog barks")
d=dog()
d.sound()

#Types of abstraction
#data abstraction:hide unnecessary data
#ex:ATM balance details
#process abstraction:hides internal working process
#ex:using car without knowing engine details

#module used for abstraction
#python uses abc module
#import statement
from abc import ABC,abstractmethod

#example
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("start")
class Car(Vehicle):
    def start(self):
        print("car starts")
c=Car()
c.start() #car starts




