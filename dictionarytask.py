# ==================== DICTIONARY QUESTIONS ====================

# Question 1: Create a dictionary with keys "name" and "age" and values "Nik" and 20.
d = {"name": "Nik", "age": 20}
print(d)
# Output: {'name': 'Nik', 'age': 20}


# Question 2: Access the value of key "name" from {"name": "Nik", "age": 20}.
d = {"name": "Nik", "age": 20}
print(d["name"])
# Output: Nik


# Question 3: Add a new key "city" with value "Delhi" to {"name": "Nik", "age": 20}.
d = {"name": "Nik", "age": 20}
d["city"] = "Delhi"
print(d)
# Output: {'name': 'Nik', 'age': 20, 'city': 'Delhi'}


# Question 4: Update the value of "age" to 25 in {"name": "Nik", "age": 20}.
d = {"name": "Nik", "age": 20}
d["age"] = 25
print(d)
# Output: {'name': 'Nik', 'age': 25}


# Question 5: Delete the key "age" from {"name": "Nik", "age": 20}.
d = {"name": "Nik", "age": 20}
del d["age"]
print(d)
# Output: {'name': 'Nik'}


# Question 6: Check if the key "email" exists in {"name": "Nik", "age": 20}.
d = {"name": "Nik", "age": 20}
print("email" in d)
# Output: False


# Question 7: Get all keys from {"name": "Nik", "age": 20} using a dictionary method.
d = {"name": "Nik", "age": 20}
print(d.keys())
# Output: dict_keys(['name', 'age'])


# Question 8: Get all values from {"name": "Nik", "age": 20} using a dictionary method.
d = {"name": "Nik", "age": 20}
print(d.values())
# Output: dict_values(['Nik', 20])


# Question 9: Convert the dictionary {"a": 1, "b": 2} into a list of (key, value) pairs.
d = {"a": 1, "b": 2}
print(list(d.items()))
# Output: [('a', 1), ('b', 2)]


# Question 10: Create a dictionary from two lists (use zip method).
#              keys = ["name", "age"], values = ["Nik", 20]
keys = ["name", "age"]
values = ["Nik", 20]
d = dict(zip(keys, values))
print(d)
# Output: {'name': 'Nik', 'age': 20}


# Question 11: Count how many keys are in {"a": 1, "b": 2, "c": 3}.
d = {"a": 1, "b": 2, "c": 3}
print(len(d))
# Output: 3


# Question 12: Merge two dictionaries {"a": 1} and {"b": 2} into one.
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)
print(d1)
# Output: {'a': 1, 'b': 2}


# Question 13: Clear all elements from {"a": 1, "b": 2} using a dictionary method.
d = {"a": 1, "b": 2}
d.clear()
print(d)
# Output: {}


# Question 14: Copy the dictionary {"x": 10, "y": 20} using a dictionary method.
d = {"x": 10, "y": 20}
d_copy = d.copy()
print(d_copy)
# Output: {'x': 10, 'y': 20}


# Question 15: Get the value of key "salary" safely from {"name": "Nik", "age": 20}
#              without getting an error.
d = {"name": "Nik", "age": 20}
print(d.get("salary"))
# Output: None


# Question 16: From {"a": 1, "b": 2, "c": 3}, remove the last inserted item
#              using a dictionary method.
d = {"a": 1, "b": 2, "c": 3}
removed = d.popitem()
print(removed)
print(d)
# Output: ('c', 3)
#         {'a': 1, 'b': 2}


# Question 17: Given student = {"name": "Rahul", "marks": {"math": 90, "science": 85}},
#              access only the "science" marks.
student = {"name": "Rahul", "marks": {"math": 90, "science": 85}}
print(student["marks"]["science"])
# Output: 85


# Question 18: From the above student dictionary, update "math" marks to 95.
student["marks"]["math"] = 95
print(student)
# Output: {'name': 'Rahul', 'marks': {'math': 95, 'science': 85}}


# Question 19: Add a new subject "english": 88 inside the "marks" dictionary.
student["marks"]["english"] = 88
print(student)
# Output: {'name': 'Rahul', 'marks': {'math': 95, 'science': 85, 'english': 88}}


# Question 20: Delete the subject "science" from inside "marks".
del student["marks"]["science"]
print(student)
# Output: {'name': 'Rahul', 'marks': {'math': 95, 'english': 88}}