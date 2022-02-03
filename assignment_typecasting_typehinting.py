"""
1. Type Hinting
    a. create a variable <odd> with hinting as `int` and assign a value to it.
    b. create a variable <PI> with hinting as `float` and assign 3.1415 to it.

    c. create any variable with `string` type hinting and assign `integer` value to it.
        - Check whether the program gives error in execution or not.
        - If it gives or does not give error, then why it gives or does not give error?
"""

# 1.a

odd:int = 21

# 1.b

PI:float = 3.1415

# 1.c
var:str = 90

# This does not give an error because it treats the entered integer as a string.

# ----------TYPE CONVERSION-------------

# 2.a

PI = 3.1415
# to print the value of PI to be 3

print(int(PI))

# 2.b
str_1 = "20"
str_2 = "30"
result = int(str_1) + int(str_2)
print(f'Result is:{result}\t')

# 2.c

x = ['1', '2', '3', '4', '5']
sum = 0
"""
- I want the value of sum to be 15.
- The way I get 15 is by adding all items from the list `x`.

Hint: the addition may involve
- for loops in the list
- type conversion
"""
for lists in range(0,len(x)):
    sum+= int(x[lists])
print(f"SUM OF THE ELEMENTS IN THE LIST:{sum}")

# 2.d

odd = [1, 3, 5, 7, 9, 11, 13, 15]
prime = [2, 3, 5, 7, 11, 13, 17]
"""
use type conversion to these lists to appropriate data type and find out
    - numbers that are odd but not prime
    - numbers that are either odd or prime
    - numbers that are prime but not odd.

Final values should be converted into list again and stored to variables.
"""
converted_odd = set(odd)
converted_prime = set(prime)
print(converted_odd.difference(converted_prime)) # for numbers that are odd but not prime
print(converted_odd.symmetric_difference(converted_prime)) # for numbers that are either odd or prime
print(converted_prime.difference(converted_odd)) # for numbers that are prime but not odd
result1 = converted_odd.difference(converted_prime)
print(list(result1)) # to print list of numbers that are odd but not prime
result2 = converted_odd.symmetric_difference(converted_prime)
print(list(result2)) # to print list of numbers that are either odd or prime
result3 = converted_prime.difference(converted_odd)
print(list(result3)) # to print list of numbers that are prime but not odd






