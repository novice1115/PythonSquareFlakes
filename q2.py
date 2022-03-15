"""
Create a class named Person and add the following attributes and methods:
    - name:     Instance attribute
    - age:      Instance attribute
    - gender:   Instance attribute
    - weight:   Class attribute
    - year_of_birth():
        Returns the year by subtracting the age from the current year.
    - get_pronouns():
        Returns list of ['he', 'his', 'him'] or ['she', 'her', 'hers'] by checking the gender
    the initializer method should take name, age, and gender
"""

import datetime
current_year = datetime.date.today().year

male = "MALE"
female = "FEMALE"
class Person:
    def __init__(self,name,age,gender,weight):
        self.name = name
        self.age = age
        self.gender = gender
        
              
    def year_of_birth(self):
        return datetime.date.today().year - self.age
    def get_pronouns(self):
        return ["he","his","him"] if self.gender=="MALE" else ["she","her","hers"]

person1 = Person("Addy Helman",24,"FEMALE"," ")
print(person1.year_of_birth())
print(person1.get_pronouns())