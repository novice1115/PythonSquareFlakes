""" 
1. Write a program to create an empty list named `my_list` and

    a. add numbers 5 and 9 to the list using `append()` method

    b. ask the user to input any number in the console and add the number to the list.
        - you can use int() to change the type from string to integer if you want.

    c. create another list `more_items` with 3 items on it and extend the list `my_list`
        using `extend` method.

    d. now find the length of the list and print the length of list describing it in a sentence.
        - you can always use string formatting for better outputs.

    e. now remove the second item using `pop()` method and see if the item exists in the list
        - you can print the list before and after using the `pop()` method.
"""
# 1.a 

my_list = []
my_list.append(5)
my_list.append(9)


# 1.b

my_list.append(int(input("Enter any item:\t")))
print(my_list)

# 1.c
more_items = [67, 50,60]
my_list.extend(more_items)
print(my_list)

# 1.d

length_of_list = my_list.__len__()
# print(my_list.__len__)
print(f"The length of list is:\t{length_of_list} ")

# 1.e
print(my_list)
my_list.pop(1)
print(my_list)

"""
2. Write a program to add 5 different wild animals to a list named `wild`.
    - tiger, lion, deer, bear, zebra

    a. sort them in ascending using the `sort()` method.
    b. reverse the list using the `reverse()` method.
    c. now add 3 more animals to the list `wild`.  ['leopard', 'elephant', 'rhino']
    d. find the position of `leopard` using the `index()` method and remove  it using `the pop()` method.
        - pop should have the index value returned using the `index()` method.
        - do not hard-code the position of leopard by manually counting it from the list.
        - check whether the leopard is removed from the list or not by `index()` method again.
          if the value error occurs, you have successfully removed it from the list.
          otherwise, try to do it again.
        - you can then comment the line that gives exception to continue to the next question.
    e. Now add `leopard` agin in the index 2 using `insert()` method.
    f. Again, remove `rhino` from the list using remove() method.

    note: you can print the values of list after each successful operations to see what is being changed.
"""

# 2.a

wild = ["Tiger", "Lion","Deer","Bear","Zebra"]
wild.sort()
# wild.sort(reverse=True)
print(wild)

# 2.b

wild.reverse()
print(wild)

# 2.c
wild.extend(["Leopard", "Elephant","Rhino"])
print(wild)

# 2.d
index = wild.index("Leopard")
wild.pop(index)
print(wild)

'''Above code can be written for 2d instead of the one below'''
# print(wild.index("Leopard"))
# wild.pop(5)
# print(wild)
# print(wild.index("Leopard")) This gave ValueError: 'Leopard' is not in the list.

# 2.e

wild.insert(2,"Leopard")
print(wild)

# 2.f

wild.remove("Rhino")
print(wild)

"""
3. Try creating a multi-dimensional list or nested list `multi` of different numbers.
    eg: [[12,52,37],[46,51,16],[17,82,39]]

    a. access the number 51 from the list.
    b. access the number 82 using the negative indices.
    c. append another list [40, 61, 10] inside the list `multi`.
        the final list should be: [[12,52,37],[46,51,16],[17,82,39],[40, 61, 10]]
    d. use foreach in the list `multi` to print each list item to the console.
        - Bonus: try using nested foreach to access each item inside of the inner list
    e. finally clear the list `multi` using the `clear()` method and verify if the list is empty or not
"""

# 3.a
multi = [[[12,25,37],[46,51,16],[17,82,39]]]
print(multi)
print(multi[0][1][1]) # to access 51

# 3.b
print(multi[-1][-1][-2]) # to access 82

# 3.c
multi1 = [40,61,10]
multi.append([multi1])
print(multi)

# 3.d

for list in multi:
    for elements in list:
        print(elements) # To print each list item


# 3.e
multi.clear()
print(multi)




    

































