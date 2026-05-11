#Create a class Employee with name and salary. 
# Inherit a class Manager with department details and display all information.
class Employee:
    def salary(self):
        print('keerthi with salary 30k')
class Manager(Employee):
    def depart_details(self):
        print('company manager')
m=Manager()
m.salary()
m.depart_details()

#keerthi with salary 30k
#company manager 
    
    
    