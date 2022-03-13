"""
1.
Convert the following function to a lambda function

def odd_or_even(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'
"""

odd_or_even = lambda num:"even" if num%2==0 else "odd"
# print(odd_or_even(9))
print("-"*50)
"""
2.
Create a lambda that accepts a list of numbers and return the list of squares of them

hint:
you can use list comprehension to return the list of squares
"""
list_of_square = lambda num : [x**2 for x in num]
print(list_of_square([10,9,3]))
print("-"*50)
"""
3.
create a lambda function that converts the length from meter to feet
"""
meter_to_feet = lambda meter:(f"Equivalent measure of METER to FEET:{meter*3.28}")
print(meter_to_feet(int(input("Enter a value to convert:"))))
print("-"*50)
"""
4.
Create a lambda function that takes an argument and finds out the square if it is even and cube if it is odd.
"""
number = int(input("Enter a number:\n"))
square_or_cube = lambda number:(number**2) if number%2==0 else (number**3)
print(square_or_cube(number))
print("-"*50)
"""
5.
Create a lambda function `get_date` that takes 3 arguments month, year, and day that
returns a single string in a "YY/MM/DD" format.
"""
get_date = lambda year,month,day:(f"Required date in YY/MM/DD format is: {year}/{month}/{day}.")
print(get_date(1998,2,12))
print("-"*50)
'''
6.
Create a lambda function that accepts a sentence that returns the sentence with spaces replaced by hyphens

example:
input => "A quick brown fox jumps over the lazy dog."
output => "A-quick-brown-fox-jumps-over-the-lazy-dog."

hint:
use string.replace() method
'''
statement = "A quick brown fox jumps over the lazy dog."
add_hyphen= lambda statement : statement.replace(" ", '-')
print(add_hyphen(statement))
print("-"*50)

"""
7.
Create a lambda function that checks whether the string provided is a number or not
"""
string1 = input("Enter a string:")
check_if_number = lambda string1:f"{string1} is numeric" if string1.isnumeric()==True else f"{string1} isn't numeric."
print(check_if_number(string1))
print("-"*50)

"""
8. create a lambda function to count total number of even numbers in a list
"""
list1 = []
even_number_count = lambda list1: f"Total count of even numbers in the list: {len([num for num in list1 if (num%2==0)])}"
print(even_number_count([10,11,15,89,12,55,67]))
print("-"*50)