#method overloading:Method overloading means creating multiple methods with the same name but with different parameters (different number or type of arguments).
#python not supported true method overloading
#Same method name
# Different arguments
# Different behavior

#method overloading using default argument

#example
class Calculator:
    def add(self,a,b,c=0):
        print(a+b+c)
c=Calculator()
c.add(1,2,3)
