#polymorphism(many forms):same methode or function can behave differently for different objects
#types
#method overriding
#method overloading

#method overriding:method overriding happens when a child class uses a same method name as parent class but gives different implementation
#child class changes the behaviour of parent class method

#examples
'''create a parent class animal havving sound as a method, child class dog having sound as a method'''
class Animal:
    def sound(self):
        print("Animal sounds")
class Dog(Animal):
    def sound(self):
        print("dog barks")
c=Dog()
c.sound()

'''p-employ, ch- developer, ch- manager classes---work method'''
class Employee:
    def work(self):
        print("Employee working at office")
class Developer(Employee):
    def work(self):
        print("Developer will develop the project")
class Manager(Employee):
    def work(self):
        print("manager will do job")
c1=Developer()
c2=Manager()
c1.work()
c2.work()

'''p-payment, ch-upi, ch-card---method=pay(self, amnt)'''
class Payment:
    def pay(self,amount):
        print("payment processing")
class Upi(Payment):
    def pay(self,amount):
        print(f'paid {amount} using upi')
class Card(Payment):
    def pay(self,amount):
        print(f'paid {amount} using card')
c1=Upi()
c2=Card()
c1.pay(500)
c2.pay(500)
