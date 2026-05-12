#problem on Inheritance super() keyword------------
#initialise a parent class as Employee-constructor with parameter name, child class as Developer - constructor with parameter prog_lang, use super()
# to get 2 parameter data
class Employee:
    def __init__(self,name):
        self.name=name
        print("Employee constructor")
class Developer(Employee):
    def __init__(self,name,prog_lang):
        super().__init__(name)
        self.prog_lang=prog_lang
        print("Developer constructor")
    def display(self):
        print("Name:",self.name)
        print("prog_lang:",self.prog_lang)
d=Developer('keerthi','python')
d.display()
 '''Employee constructor
Developer constructor
Name: keerthi
prog_lang: python'''

# make a class animal - contain a method with print("animal is shouting"), make 2 child classes
#dog - method with print "bow"& cat - method with print "meow"
class Animal:
    def sound(self):
        print("animal is shouting")
class Dog(Animal):
    def dog(self):
        print("bow")
class Cat(Animal):
    def cat(self):
        print("meow")
d=Dog()
d.dog()
d.sound()
c=Cat()
c.cat()
c.sound()
'''bow
animal is shouting
meow
animal is shouting'''
