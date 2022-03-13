"""
1.
write a program to calculate the factorial of a non-negative number using recursive function
"""

def factorial1(num):
    if num < 0:
        return(f"{num} is negative.")
    elif num==0:
        return 1
    return num *factorial1(num-1)
print(factorial1(int(input("Enter a number to find a factorial:"))))
print("-"*60)
"""
2.
Write a recursive function to take a number and calculate the sum of its digits.
"""
def sum_of_digits(number):
    if number<10:
        return number
    return sum_of_digits (number//10) + number%10
sum = sum_of_digits(int(input("Enter a number:")))
print(sum)
print("-"*60)
"""
3.
Write a recursive function to find out the sum of first n natural numbers
"""
def sum_of_natural_numbers(number):
    if number==1:
        return 1
    return number+sum_of_natural_numbers(number-1)
sum1 = sum_of_natural_numbers(int(input("Enter a number:")))
print(sum1)
print("-"*60)

"""
4.
write a recursive function to print out the nth element of a fibbonacci series below
series = [1, 1, 2, 3, 5, 8, 13, 21, 44, 65, ...]
example:
fib(6) should return 8
"""

def fibonacci(number):
    if number==1:
        return 1
    if number==2:
        return 1
    return fibonacci(number-1)+fibonacci(number-2)
result = fibonacci(int(input("Enter a number:")))
print(result)
print("-"*60)

"""
5.
try the same for the fibonnaccii series below
series = [4, 6, 10, 16, 26, 42, ...]
"""

def fibonacci(number):
    if number==1:
        return 4
    if number==2:
        return 6
    return fibonacci(number-1)+fibonacci(number-2)
result = fibonacci(int(input("Enter a number:")))
print(result)