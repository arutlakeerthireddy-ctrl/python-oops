#Encapsulation:wrapping data(variables) and methods(functions) together inside a class and protecting the data from direct access
#Types of Encapsulation(Access modifiers)
#pulbic:variables and methods accessed anywhere
class Student:
    def __init__(self):
        self.name="keer"
obj=Student()
print(obj.name)#keer

#protected:use a single underscore _.
#used only inside class and child classes
class Student:
    def __init__(self):
        self._course="python"
obj=Student()
print(obj._course)#python

class Student:
    def __init__(self):
        self._course="python"
class Name(Student):
    def __init__(self):
        super().__init__()
        self.name="keer"
c=Name()
print(c.name)
print(c._course)

#private:use double underscore __.
#they cannot be accessed directly outside the class
class Student:
    def __init__(self):
        self.__name="uma"
obj=Student()
print(obj.__name)#error
#using method
class Student:
    def __init__(self):
        self.__name="uma"
    def show(self):
        print(self.__name)
obj=Student()
obj.show()#uma

#Name mangling
class Student:
    def __init__(self):
        self.__name="uma"
obj=Student()
print(obj._Student__name)#uma



