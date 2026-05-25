#Create a class with private data members and access them using a public method.
class Bank:
    def __init__(self):
        self.cash=5000
    def Display(self):
        print(self.cash)
obj=Bank()
obj.Display()#5000

#Write a Python program to demonstrate private variables using double underscore (__).
class Demo:
    def __init__(self):
        self.__value=90
    def show(self):
        print(self.__value)
obj=Demo()
obj.show()#90

#Create a class Student with private attributes name and marks.
class Student:
    def __init__(self):
        self.__name="keer"
        self.__marks=90
    def show(self):
        print(self.__name)
        print( self.__marks)
        
obj=Student()
obj.show()

