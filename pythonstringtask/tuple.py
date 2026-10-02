# Creating a tuple
my_tuple = (1, 2, 3, 'Python', 4.5)
print(my_tuple) # Output: (1, 2, 3, 'Python', 4.5)


#  Accessing Tuple Items
my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple[1]) # Output: 'banana'
print(my_tuple[-1])       #'cherry' 


# slicingtuple

my_tuple = (10,20,30,40,50,60)
print(my_tuple[1:4])



# Reassigning a Tuple:

my_tuple = (1,2,3,4)
my_tuple = (6,7,8,9)
print(my_tuple)

# Convert Tuple to Lis

my_tuple = ('apple', 'banana', 'cherry')
temp_list = list(my_tuple)
temp_list[1] = 'orange' 
my_tuple = tuple(temp_list)
print(my_tuple) 


# Unpacking Tuples

my_tuple = ('apple', 'banana', 'cherry')
(fruit1, fruit2, fruit3) = my_tuple
print(fruit1) # Output: 'apple'
print(fruit2) # Output: 'banana'
print(fruit3) # Output: 'cherry


# joining tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined_tuple = tuple1 + tuple2
print(joined_tuple) # Output: (1, 2, 3, 4, 5, 6)


# deletin a tuple

my_tuple = ('apple', 'banana', 'cherry')
del my_tuple
# print(my_tuple)