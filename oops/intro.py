#what is oops?
#oops:object-oriented programming system
#it is a programming approach uses class and objects to organize the code in structured way
#class:blueprint
#object:instance of class

#why do we use oops?
#To organize code in clean structure
#to reuse
#secure
#readability
#easy to maintain
#example
class student:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def display(self):
        print(self.name,self.branch)
d=student("keerthi","csm")
d.display()

#__init__:constructor used to initialize values,it runs automatically when object is created
#self:not a keyword,but must be used for every method inside class
#self refers to object
#self.variable(object): used to store data 
#d is object

#we can use oops in 
#software development,web development,data science/ml,game development

#4 pillars of oops:
#1.inheritance
#2.abstraction
#3.polymorphism
#4.Encapsulation



