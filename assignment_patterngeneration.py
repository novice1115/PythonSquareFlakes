"""
Pattern 1
*
*   *
*   *   *
*   *   *   *
*   *   *   *   *

"""
for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print(" ")
print("-"*50)

"""

Pattern 2
1
1   3
1   3   5
1   3   5   7
1   3   5   7   9
"""
for _ in range(6):
    for x in range(_):
        print(x*2+1,end=" ")
    print(" ")

print("-"*50)

"""
Pattern 3
1
2   2
3   3   3
4   4   4   4
5   5   5   5   5
"""

# rows = int(input("No. of rows:"))
for a in range(6):
    for b in range(a):
            print(a,end=" ")
    print(" ")
print("-"*50)
"""
Pattern 4
1
2   1
3   2   1
4   3   2   1
5   4   3   2   1
"""
for _ in range(6):
    for j in range(_, 0, -1):
        print(j, end=' ')
    print("")
print("-"*50)


'''
Pattern 5

1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25
'''

for i in range(1,6):
    for j in range(1,6):
        print(i*j,end ="\t")
    print(" ")
print("-"*50)

'''
Pattern 6

A
A   P
A   P   P
A   P   P   L
A   P   P   L   E

'''
word = "APPLE"
for i in range(0,5):
    for j in range(0,i+1):
        print((word[j]),end="\t")
    print(" ")
print("-"*50)

"""
Pattern 7

                *
            *   *
        *   *   *
    *   *   *   *
*   *   *   *   *

"""
 
rows = 5
space = 2 * 5 - 2
for i in range(0, 5):
    for j in range(0, space):
        print(end=" ")
    space -= 2
    for j in range(0, i + 1):
        print("* ", end="")
    print(" ")
print("-"*50)
'''
Pattern 8

                1
            1   3
        1   3   5
    1   3   5   7
1   3   5   7   9

'''
for row in range(1, 6):
    print('\t'*(5-row), end='')
    for col in range(1, row+1):
        print(2*col-1, end='\t')
    print(" ")

print("-"*50)
'''

Pattern 9

                A
            A   P
        A   P   P
    A   P   P   L
A   P   P   L   E

'''
word = "APPLE"
length =len(word)
for i in range(length):
    print('\t'*(5-i), end='')
    for j in range (i+1):
        print(word[j], end='\t')
    print(" ")

print("-"*50)
"""
Pattern 10  (Bonus Exercise)
                1
            1   2   1
        1   2   3   2   1
    1   2   3   4   3   2   1
1   2   3   4   5   4   3   2   1


"""
for x in range(1, 6):
    print('\t' * (5 - x), end='\t')
    for y in range(1, x+1):
        print(y, end='\t')
    for z in range(x-1,0,-1):
         print(z, end = '\t')
    print()

