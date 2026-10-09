# Creating a Dictionary

my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)


# Using dict() function

another_dict = dict(name="Alice", age=25, city="Los Angeles")
print(another_dict)


# Empty Dictionary

empty_dict = {}
print(empty_dict)


# Accessing Dictionary Items

my_dict = {"name": "John", "age": 30}
print(my_dict["name"])


# Using get()

my_dict = {"name": "John", "age": 30}
print(my_dict.get("age"))
print(my_dict.get("salary"))


# Changing Dictionary Items

my_dict = {"name": "John", "age": 30}
my_dict["age"] = 31
print(my_dict)


# Adding Items to a Dictionary

my_dict = {"name": "John", "age": 30}
my_dict["city"] = "New York"
print(my_dict)


# Removing Items using pop()

my_dict = {"name": "John", "age": 30, "city": "New York"}
age = my_dict.pop("age")
print(age)
print(my_dict)


# Removing Items using popitem()

my_dict = {"name": "John", "age": 30}
last_item = my_dict.popitem()
print(last_item)


# Removing Items using del

my_dict = {"name": "John", "age": 30}
del my_dict["age"]
print(my_dict)


# clear()

my_dict = {"name": "John", "age": 30}
my_dict.clear()
print(my_dict)


# Copying a Dictionary using copy()

original = {"name": "John", "age": 30}
copy_dict = original.copy()
print(copy_dict)


# Copying a Dictionary using dict()

original = {"name": "John", "age": 30}
copy_dict = dict(original)
print(copy_dict)


# Nested Dictionary

nested_dict = {
    "person1": {"name": "John", "age": 30},
    "person2": {"name": "Alice", "age": 25}
}

print(nested_dict["person1"]["name"])


# keys()

my_dict = {"name": "John", "age": 30}
print(my_dict.keys())


# values()

my_dict = {"name": "John", "age": 30}
print(my_dict.values())


# items()

my_dict = {"name": "John", "age": 30}
print(my_dict.items())


# update()

my_dict = {"name": "John", "age": 30}
my_dict.update({"city": "New York", "age": 31})
print(my_dict)


# fromkeys()

keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "Unknown")
print(new_dict)


# setdefault()

my_dict = {"name": "John", "age": 30}
city = my_dict.setdefault("city", "New York")
print(city)
print(my_dict)