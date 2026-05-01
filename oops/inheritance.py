#inheritance:inheritance in oops where one class(child/subclass) can get properties of another class(parent/superclass)
#it helps to reuse code and avoid writing same code again
#example
class Animal:
    def speak(self):
        print("animal is speaking")
class Cat(Animal):
    def meow(self):
        print("cat sounds meow meow")
c=Cat()
c.meow()
c.speak()

#types of inheritance
#1.single inheritance:One parent → one child
class parent:
    def father(self):
        print("parent is father")
class child(parent):
    def son(self):
        print("child is son")
c=child()
c.father()
c.son()

#2.multiple inheritance:One child → multiple parents
class parent1:
    def father(self):
        print("parent1 is father")
class parent2:
    def mother(self):
        print("parent2 is mother")
class child(parent1,parent2):
    def son(self):
        print("child is son")
c=child()
c.father()
c.mother()
c.son()

#3.multilevel inheritance:Grandparent → parent → child
class grandparent:
    def grandfather(self):
        print("grandparent is grandfather")
class parent(grandparent):
    def father(self):
        print("parent is father")
class child(parent):
    def son(self):
        print("child is son")
p=parent()
p.grandfather()
c=child()
c.son()

#4.hierachial inheritance:One parent → many children
class parent:
    def father(self):
        print("parent is father")
class child1(parent):
    def son(self):
        print("child1 is son")
class child2(parent):
    def daughter(self):
        print("child2 is daughter")
c1=child1()
c1.father()
c1.son()
c2=child2()
c2.father()
c2.daughter()

