"""
Create a python class with following properties:
1. private class attribute
2. public class attribute
3. instance attribute
4. initializer method
5. string representation method [__str__()]
"""
class Student:
    def __init__(self,name,rollno,address,grade):
        self.name = name
        self.rollno = rollno
        self.address = address
        self.grade = grade

    var = 300
    __var1 = "John Doe"
    _var2 = "Gracy Helman" 

    def __str__(self) -> str:
        return (f"The student named {self.name} of class {self.grade} has roll number {self.rollno} and {self._var2},{self.__var1} are her friends..She lives in {self.address}.")  
student1 = Student("Emily",2,"Granger",3)
print(student1)

print("*"*60)
