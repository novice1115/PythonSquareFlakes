"""
1. Write a python function to find the largest out of 3 numbers
You should use comparison operator to find out the maximum of 3 numbers.
"""
def largest_number(a,b,c):
    if a>(b and c):
        print(f"{a} is the largest number.")
    elif b>(c and a):
        print(f"{b} is the largest number.")
    else:
        print("f{c} is the largest number.")
largest_number(190,1900,300)
print("")


"""
2. Write a python function that calculates the number of upper case characters, lower case characters
 and spaces in the string and returns them as a tuple.
for example
x = "A Quick Brown Fox Jumps Over The Lazy Dog."
Number of upper case characters: 9
Number of lower case characters: 14
Number of spaces: 8
"""

x = "A Quick Brown Fox Jumps Over The Lazy Dog."
def count(n:str):
    upper_case = 0
    lower_case = 0
    spaces = 0
    for letters in n:
        if letters.isupper()==True:
            upper_case+=1
        if letters.islower()==True:
            lower_case+=1
        if letters ==" ":
            spaces+=1
    print(f"Number of upper case characters:{upper_case}\nNumber of lower case characters:{lower_case}\nNumber of spaces:{spaces}")
count("Joe Biden is the President of United States of America.")
print("-"*50)
"""
3.
Suppose you went to a coffee shop. A shopkeeper asked you to create a program that serves coffee
according to the customer's requirements.
The coffee machine should ask user to enter any numbers below that should make a coffee and serve it to the user.
Please use the `make_coffee()` function below to prepare a coffee and serve it.
Followings are the ingredients for coffee:
Sugar: no. of spoons
beans: no. of spoons
milk: volume in ml.
The total volume of coffee should be 250ml. The maximum volume of milk can be only upto  150ml. greater than that
should give the error saying not acceptable.
Finally print the line describing the coffee you prepared along with  milk and water composition.
"""
def make_coffee():
    print("Follow the instructions for the composition of coffee:")
    sugar = int(input("How much sugar do you need in your coffee?"))
    beans = int(input("Enter number of spoons of coffee beans you need:"))
    milk = int(input("How much milk (in mililiter) do you need?:")) 
    while milk <= 150:
        more = input(f"Do you need more milk?[y/n]")
        if milk<=150 and more.lower()=="y":
            milk_to_add = int(input("Milk to add(in ml):"))
            total_milk =milk+milk_to_add
            print(f"Milk (after adding): {total_milk} ml.")
        if total_milk>150:
            print(f"Volume of milk greater than 150ml is not acceptable.")
        else:
            print(f"The coffee with {sugar} spoons of sugar, {beans} spoon of coffee beans, {total_milk}ml of milk and {250-total_milk} ml of water is ready.")
            break
make_coffee()
"""
4.
Write a program to create a multiplication table of the given number.
The `mul_table()` function should have the following arguments:
- `number`: the number to print multiplication table of.
- `limit`: the number upto which multiples are printed which should have the default value of 10
Multiplication table for 13
| 13  X   1|    13|
| 13  X   2|    26|
| 13  X   3|    39|
| 13  X   4|    52|
| 13  X   5|    65|
| 13  X   6|    78|
| 13  X   7|    91|
| 13  X   8|   104|
| 13  X   9|   117|
| 13  X  10|   130|
"""
def mul_table(number,limit):
    for num in range(1,limit+1):
        print(f"|{number} x {num}| \t {number* num}|")
mul_table(12,10)

"""
5.
Write a function that takes a string and checks whether the word is palindrome or not.
- A palindrome is a string that reads the same backward or forward.
- Examples: eve, dad, rotator
Your program should be able to ask user to enter the word and check whether it is palindrome or not.
The program should not end until user enters no.
The program should start with the
The output should show inside a box as shown below with text justified center.
Example Output:
=============================[ Palindrome Finder ]=============================
Enter a word: rotator
+-----------------------------------------------------------------------------+
|                   The word 'rotator' is a palindrome                        |
+-----------------------------------------------------------------------------+
The word 'rotator' is a palindrome word
Do you want to check again? [yes/no]: yes
Enter a word: dad
+-----------------------------------------------------------------------------+
|                     The word 'dad' is a palindrome                          |
+-----------------------------------------------------------------------------+
Do you want to check again? [yes/no]: no
=================================[ exiting now ]================================
"""
def to_find_if_pallindrome(word):
    condition = input(f"Enter YES to continue and NO to exit:")
    if condition=="YES":
        word = input(f"Enter a word to check if pallindrome or not:")
        if word==word[::-1]:
            value = (f"{word} is pallindrome.")
            print(f'+{"-"*78}+')
            print(f'|{value.center(78)}|')
            print(f'+{"-"*78}+')
            print(f"Would you like to check another word? please enter YES or NO:")
            to_find_if_pallindrome(word)
        else:
            value = print(f"{word} is not palindrome.") 
            print(f'+{"-"*78}+')
            print(f'|{value.center(78)}|')
            print(f'+{"-"*78}+')
            print(f"Would you like to check another word? YES or NO:")
            to_find_if_pallindrome(word)
            
    return "EXITING OUT"
to_find_if_pallindrome(" ")
print("-"*50)

"""
6.
Write a function that accepts words that are separated by hyphen returns the 
alphabetically sorted words
separated by hyphen.
Hint:
- split the words using string.split() method
- sort the list
- join the list to a string with string.join() method
"""
word = input("Enter hyphenated words to sort in output:")
def sort_words(word):
    word = word.split("-")
    word.sort()
    word = '-'.join(word)
    return word
word = sort_words(word)
print(word)
print("-"*50)


"""
7.
Write a function that accepts a number x
- if x is a multiple of 2, it should return the value y = x**2 + 2x + 3
- if x is a multiple of 3, it should return the value y = x**3 + 4x + 5
- if x is a multiple of both 2 and 3, it should return the value y = x**3 + 4x**2 + 5x + 6
- in other cases it should return negative value of the given number
"""

def number_input(x):
    if x%2==0:
        y = x**2 + 2*x + 3
        return y
    if x%3==0:
        y = x**3 + 4*x + 5
        return y
    if (x%2 and x%3==0):
        y = x**3 + (4*x)**2 + 5*x + 6
        return y
    else:
        y= int(input("Enter a number"))
        return -y
print(number_input(20))
print(" ")
print("-"*50)

"""
8.
Write a function that accepts any number of arguments
find out the sum of all numbers by multiplying by 2 if it is odd and dividing by 2 if the number is even.
Example if arguments are (5,6,7,8)
the result should be 31 [ 5*2 + 6/2 + 7*2 + 8/2 ]
"""

def test(*args):
    sum = 0
    for number in args:
        if number%2==0:
            sum+=number/2
        if number%2!=0:
            sum+=2*number
    return sum
print(int(test(5,6,7,8)))

