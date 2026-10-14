def greet(name):  # name is a parameter
    print(name)

greet("Alice")  # "Alice" is an argument




# Positional arguments

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Anshif", 20)  # Positional arguments



 # Keyword arguments

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Anshif")  # Keyword arguments



# Default argument

def student(name, age=20):  
    print("Name:", name)
    print("Age:", age)

student("Anshif")
student("Rahul", 21)