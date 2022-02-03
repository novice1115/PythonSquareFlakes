'''
1. Write a program to create a tuple to  add 5 different numbers.
    a. find out the length of the tuple
    b. find out the 3rd element of the tuple by accessing it through the index
    c. use `enumerate()` function to map each element with its index and print it using the foreach loop
        - please see the reference to the file 02_data_types/06_tuples.py
'''
# 1.a 


tuple1 = (2,22,42,62,82)
# print(sum(tuple1))
print(tuple1.__len__())

# 1.b
print(tuple1[2])

# 1.c
for x in enumerate(tuple1):
    print(x)

"""
2. Write a program to create a nested tuple and access different elements of the inner tuple using
   positive and negative index positions.

"""
# 2 

nested = ((1,3),(2,4),(5,7),(6,8))
print(nested[0][-1])

'''
Bonus:
3. create two different tuples t1 and t2 with different elements inside it
    a. create the next tuple t3 to add all values of t1 and t2 using the destructuring method

    - suppose t1 has (1,6,9,4,3)
    - and t2 has (2,7,8,3,5)
    -t3 must have (1,6,9,4,3,2,7,8,3,5)
    - make sure to use destructuring method using `*` operator in the tuples
'''

# 3

t1 = ("Sam","Mathematics",80)
t2 = ("Gracy","Physics",78)
t3 = (*t1,*t2)
print(t3)
