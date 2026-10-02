#  Creating a Set

my_set = {1,2,3,4}
print(my_set)


# Using set() function
another_set = set([5, 6, 7])
print(another_set)


# Empty Set
empty_set = set()
print(type(empty_set))


# Adding a Single Item:
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)



# Adding Multiple Items:
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)


#  Removing Items from a Set

my_set = {1, 2, 3, 4}
my_set.remove(2)
print(my_set)

# discard()
my_set = {1, 2, 3, 4}
my_set.discard(5) 
print(my_set) 


#  clear()
my_set = {1, 2, 3}
my_set.clear()
print(my_set)


# update(
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set1.update(set2)
print(set1)


# Set Intersection (&)
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1 & set2
print(result)

# Set Symmetric Difference (^)
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1 ^ set2
print(result) 



# issubset(set)
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))


# Frozen Sets
my_frozenset = frozenset([1, 2, 3, 4])
print(my_frozenset)