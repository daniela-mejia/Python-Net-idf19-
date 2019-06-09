#Daniela Mejia 04/25/2019
#python object oriented programming Employee Class

class Employee:

    def __init__(self, name, Id, dep, job):
        self.name = name
        self.Id = Id
        self.dep = dep
        self.job = job

#method
    def fulldata(self):
        return 'Name:{},Id: {}, Department{},Job: {}'.format(self.name,self.Id,self.dep,self.job)

#data instance variables    
emp1 = Employee('Susan Meyers','45899','Accounting','Vice President')
emp2 = Employee('Mark Jones','39119','IT','Programmer')
emp3 = Employee('Joy Rogers','81774','Manufacturing','Engineer')


print(emp1.fulldata())
print(emp2.fulldata())
print(emp3.fulldata())
