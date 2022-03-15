"""
Create a class Vehicle add some attributes and methods to it
    - name
    - brand
    - wheels_count
    - engine_type
    - braking_system
Create a child class HeavyVehicle and inherit all the attributes from the parent class Vehicle
    - change the wheels_count from 4 to 6  in the initializer or accept the value while instantiating
    - add more instance attributes like max_load, mileage, etc.
Create a child class Bike and inherit all the attributes from the parent class Vehicle
    - change the wheels_count from 4 to 2 in the initializer
    - add setter or getter methods or property to add bike number, and owner name
    - try adding property instead of setter or getter for passenger/ pillion attribute
create different instances of Vehicle, HeavyVehicle, and Bike and check whether each other are subclasses
and instances of different classes or not.
"""
class Vehicle:
    wheels_count = 4
    engine_type = "Diesel Engine"
    braking_system = "ABS" 
    def __init__(self,name,brand,):
        self.name = name
        self.brand = brand
    
class HeavyVehicle(Vehicle):
    max_load = 4000
    mileage =40
    def __init__(self, name, brand):
        self.wheels_count =6
        super().__init__(name, brand)  

class Bike(Vehicle):
    def __init__(self, name, brand):
        self.wheels_count =2
        super().__init__(name, brand)
        self.__registration_no = ""
        self.__owner = " "

    @property
    def registration_no(self):
        return self.__registration_no

    @registration_no.setter
    def registration_no(self,value):
        self.__registration_no = value
    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value: str):
        self.__owner = value

bike1 = Bike("Apache RTR 200", "TVS")
bike1.reg_no = 11223344
bike1.owner = "Eric Brown"

print(bike1.registration_no)
print(bike1.owner)


print(issubclass(Bike, Vehicle))
print(isinstance(bike1, Vehicle))
print(isinstance(bike1, HeavyVehicle))



        