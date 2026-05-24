#Write a Python program to demonstrate private variables using double underscore (__).
class Demo:
    def __init__(self):
        self.__value=100
    def Display(self):
        print(self.__value)
obj=Demo()
obj.Display()#100