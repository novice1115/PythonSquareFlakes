"""
1. Write a program to create two different set of countries
    i.  rich: {'USA', 'China', 'Japan', 'Germany', 'France', 'Australia', 'Italy'}
    ii. europe: {'Germany', 'France', 'England', 'Switzerland', 'Italy', 'Portugal', 'Sweden'}

    Use the Set methods to find out:

    a. countries that are rich but not in Europe
    b. countries that are in Europe but not rich
    c. countries that are both rich and are in Europe
    d. countries that are either rich or in Europe, but not both
    e. all the countries in either of the sets. (Names must be unique)
    f. see if two sets are disjoint or not
    g. now remove the common countries from the `rich` set and check if two sets are disjoint or not.
        - hint: use `difference_update()` method. for more, please refer to python documentation
"""
# 1.a

rich = {"USA", "China", "Japan", "Germany", "France", "Australia", "Italy"}
europe ={"Germany", "France","England", "Switzerland", "Italy", "Portugal", "Sweden"}

# for countries that are rich but not in Europe 
print(rich.difference(europe))


# 1.b for countries that are in Europe but not rich
print(europe.difference(rich))


# 1.c

print(rich.intersection(europe)) # for countries that are both rich and are in Europe

# 1.d for countries that are either rich or in Europe, but not both

print(rich.symmetric_difference(europe))
# print(europe.symmetric_difference(rich))

# 1.e for all the countries in either of the sets

print(europe.union(rich))

# 1.f to see if disjoint or not

print(europe.isdisjoint(rich))

# 1.g 

print(rich.difference_update(europe))
print(europe.isdisjoint(rich))

"""
2. Create two more sets
    i.  `asian_rich` and add {'China', 'Japan'} to it.
    ii. `american_rich` and add {'USA', 'Canada'} to it.
   and check whether:

   a. `asian_rich` is a subset of `rich` or not
   b. `rich` is a superset of `asian_rich` or not
   c. `american_rich` is a subset of `rich` or not

"""

# 2.a
asian_rich = {"China", "Japan"}
american_rich = {"USA", "Canada"}
print(asian_rich.issubset(rich))

# 2.b
print(rich.issuperset(asian_rich))

# 2.c 
print(american_rich.issubset(rich))



