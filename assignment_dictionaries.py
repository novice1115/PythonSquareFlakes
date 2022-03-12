'''
1. Create a dictionary of a person that contains key value pair of
    - name: str
    - age: int
    - profession: str
    - married: bool

    a. print the value of 'name' from the dictionary
    b. add the age of the dictionary be 10 and print the dictionary items in formatted string
        Eg: {name} will be {new_age} at 2031 AD.
    c. Try getting the value of 'employed' from the dictionary.
        - If exception occurs, note it and check what the excption says.
    d. try `get()` method instead of large brackets [] in the previous question (1.c)
    e. try `get()` method with second parameter: False and see what is printed.
        Eg: person.get('employed', False)

'''
from hashlib import new


person = {"name": "Sam",
         "age": 23,
         "profession": "Engineer",
         "married": "False"
}
print(person)

# 1.a 
print(person["name"])

# 1.b
person["name"] = "Darwin"
person["age"] = 10
print(f"{person['name']} will be {person['age']} years old in 2032 A.D.")

# 1.c

# print(f"{person['employed']}") # KeyError : 'employed'

# 1.d

print(f'There is something empolyed? :{person.get("employed")}')

# 1.e

print(f'There is something empolyed? :{person.get("employed", False)}')

'''
2. create a dictionary <car> with 3 keys and values (brand, model, price).
    a. add a new key 'engine' and set some random value in car.
    b. add 3 more dictionary keys with `update` method. (color, no_of_seats, transmission).
    c. remove the key 'color' from the dictionary.
    d. try using `popitem()` method in the dictionary and see what changes in dictionary
    e. use for loop to iterate through all keys from a dictionary.
    f. use for loop to iterate through all keys from a dictionary using `keys()` method.
    g. use for loop to iterate through all values from a dictionary using `values()` method.
    h. use for loop to iterate through all keys, values from a dictionary using `items()` method.
'''

# 2.a 

car ={
    "brand" : "Ford",
    "model" : "Mustang",
    "price" : 90000
}
car.update({"engine":"Electric"})

# 2.b
car.update({"color":"grey", "no_of_seats":7,"transmission":"Electric"})
print(car)

# 2.c
car.pop("color")
print(car)


# 2.d
print(car)
print(f'Removing item: {car.popitem()} \n')
print(f'Is it same as above? : {car} \n')

# 2.e,f,g,h 
for elements in car:
    print(elements)
print(car)

for x in car:
    print(f"Keys in the dictionary 'car': {x}")

for y in car.values():
    print(f"Values in the dictionary 'car':{y}")

for a,b in car.items():
    print(f"Keys-->\t{a}\nValues-->{b}")
    
'''
3. Create a nested dictionary named yoda with following properties
    - age: 910
    - species: Yodas
    - gender: male
    - affilitions: ['Jedi', 'Galactic Republic']
    - master: <dict>
        - name: Qui-Gon Jinn
        - age: 48
        - affiliations: ['Jedi', 'Galactic Republic', 'Heliost Clan']
        - master: <dict>
            - name: Dooku
            - age: 83
            - affiliations: ['House Serenno', 'Jedi']

    a. print the value of the first affiliation of `Dooku` from the dictionary
    b. add new affiliation 'Sith' to Dooku
    c. pop the key 'master' from the dictionary

'''
# 3.a 

yoda = {
    'age': 910,
    'species': 'Yodas',
    'gender': 'male',
    'affilitions': ['Jedi', 'Galactic Republic'],
    'master': {'name': 'Qui-Gon Jinn',
    'age': 48,
    'affiliations': ['Jedi', 'Galactic Republic', 'Heliost Clan'],
    'master': {
            'name': 'Dooku',
            'age': 83,
            'affiliations': ['House Serenno', 'Jedi']
        }}
}

print(yoda)

# 3.b
new = 'Sith'
yoda['master']['master']['affiliations'].append(new)
print(f'This is dictionary after adding Sith :\n {yoda}')

#3.c 
yoda.pop('master')
print(f'Dictionary "yoda" after poping out "master": {yoda}')

