class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

    def employee_details(self):
        print("name of the employee is",self.name)
        print("the age of the employee is",self.age)
        print("the salary of the employee is",self.salary)
        print("the gender of the employee is",self.gender)    
    
e1=Employee("akill",19,2000000,'male')
e1.employee_details()