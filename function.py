# def greet(name):  # name is a parameter
#     print(name)

# greet("Alice")  # "Alice" is an argument




# # Positional arguments

# def student(name, age):
#     print("Name:", name)
#     print("Age:", age)

# student("Anshif", 20)  # Positional arguments



#  # Keyword arguments

# def student(name, age):
#     print("Name:", name)
#     print("Age:", age)

# student(age=20, name="Anshif")  # Keyword arguments



# # Default argument

# def student(name, age=20):  
#     print("Name:", name)
#     print("Age:", age)

# student("Anshif")
# student("Rahul", 21)



# Return Statement

# def multiply(a, b):
#  return a * b
# result = multiply(4, 5)
# print(result)



# # Docstrings in Functions

# def add(a, b):
#  """This function adds two numbers."""
#  return a + b
# print(add.__doc__)




# # Lambda Functions in Python


# add = lambda a, b: a + b
# print(add(3, 5))



# # lambda map function

# numbers = [1, 2, 3, 4]
# squared = map(lambda x: x ** 2, numbers)
# print(list(squared))



# # lambda filter() function

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))


# # Lambda with reduce()

# from functools import reduce
# numbers = [1, 2, 3, 4]
# sum_result = reduce(lambda x, y: x + y, numbers)
# print(sum_result)




# Higher-Order Functions


# def increment(n):
#    return lambda x: x + n


# add_5 = increment(5)
# print(add_5(10)) 






# x = 10  # Global scope

# def outer_function():
#     x = 5  # Enclosing scope

#     def inner_function():
#         x = 2  # Local scope
#         print(x)

#     inner_function()

# outer_function()  # Output: 2
# print(x)          # Output: 10


# keyword arguments

# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_details(name="Alice", age=30, city="New York")




# Using *args and **kwargs Together

# def display_info(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# display_info(1, 2, 3, name="Alice", age=25)




# Order of Arguments:
# def full_function_example(param1, *args, **kwargs):
#     print("Regular parameter:", param1)
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# full_function_example(10, 20, 30, name="anshif", age=19)
