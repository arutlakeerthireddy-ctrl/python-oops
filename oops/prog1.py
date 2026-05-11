#Create a class Shape with a method area(). Inherit Rectangle and calculate the area.
class Shape:
    def area(self,l,b):
        print("area of rectangle is ",l*b)
class Rectangle(Shape):
    def cal(self,l,b):
        pass
r=Rectangle()
r.area(2,5)

#Create a class BankAccount with account details. Inherit SavingsAccount and display balance with interest.
class BankAccount:
    def account(self,name,balance):
        self.name=name
        self.balance=balance
        print("Account holder:",self.name)
        print("Balance:",self.balance)
class SavingsAccount(BankAccount):
    def display(self,rate):
        Interest=(self.balance*rate)/100
        total=self.balance+Interest
        print("Interest:",Interest)
        print("Total balance:",total)
s=SavingsAccount()
s.account("keerthi",50000)
s.display(2)
'''Account holder: keerthi
Balance: 50000
Interest: 1000.0
Total balance: 51000.0'''



