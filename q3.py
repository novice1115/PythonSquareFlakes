"""
Create a class Employee that contains different attributes.
- id
- first_name
- last_name
- project
- department
- salary
Make attributes project, department, and salary as private and use getter and setter methods to get and
set respective values
id should be private and can only be initialized when employee instance is created
first_name and last_name should be initialized with constructor and can be changed any time
"""

class Employee:
    def __init__(self,id,first_name,last_name):
        self.__id = id
        self.first_name = first_name
        self.last_name = last_name

        self.__project = " "
        self.__department = " "
        self.__salary = " "
    
    def get_project(self):
        return self.__project
    
    def get_department(self):
        return self.__department
    
    def get_salary(self):
        return self.__salary

    def set_project(self,project):
        self.__project=project
    
    def set_department(self,department):
        self.__department=department
    
    def set_salary(self,salary):
        self.__salary=salary

Mary = Employee(1,"Mary","Evansville")

Mary.set_project("Tech Solutions")
print(Mary.get_project())

Mary.set_department("IT")
print(Mary.get_department())

Mary.set_salary(40000)
print(Mary.get_salary())





