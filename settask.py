# Q1: Create a set with values {1, 2, 3, 4}.
s = {1, 2, 3, 4}
print(s)
# Output: {1, 2, 3, 4}

# Q2: Add the value 5 to the set {1, 2, 3, 4} using a set method.
s = {1, 2, 3, 4}
s.add(5)
print(s)
# Output: {1, 2, 3, 4, 5}

# Q3: Remove the value 3 from the set {1, 2, 3, 4} using a set method.
s = {1, 2, 3, 4}
s.remove(3)
print(s)
# Output: {1, 2, 4}

# Q4: Check if 2 exists in the set {1, 2, 3, 4}.
s = {1, 2, 3, 4}
print(2 in s)
# Output: True

# Q5: Convert the list [1, 2, 2, 3, 4, 4] into a set to remove duplicates.
lst = [1, 2, 2, 3, 4, 4]
s = set(lst)
print(s)
# Output: {1, 2, 3, 4}

# Q6: Convert the tuple (10, 20, 30) into a set.
t = (10, 20, 30)
s = set(t)
print(s)
# Output: {10, 20, 30}

# Q7: Find the union of sets {1, 2, 3} and {3, 4, 5}.
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
# Output: {1, 2, 3, 4, 5}

# Q8: Find the intersection of sets {1, 2, 3} and {3, 4, 5}.
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))
# Output: {3}

# Q9: Find the difference between sets {1, 2, 3, 4} and {3, 4}.
a = {1, 2, 3, 4}
b = {3, 4}
print(a.difference(b))
# Output: {1, 2}

# Q10: Create a copy of the set {5, 6, 7} using a set method.
s = {5, 6, 7}
s_copy = s.copy()
print(s_copy)
# Output: {5, 6, 7}

# Q11: Remove all elements from the set {1, 2, 3} using one set method.
s = {1, 2, 3}
s.clear()
print(s)
# Output: set()

# Q12: Check whether {1, 2} is a subset of {1, 2, 3}.
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))
# Output: True

# Q13: Check whether {1, 2, 3} is a superset of {1, 2}.
a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))
# Output: True

# Q14: Find the symmetric difference between {1, 2, 3} and {3, 4, 5}.
a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))
# Output: {1, 2, 4, 5}

# Q15: Add multiple elements {8, 9, 10} into {1, 2, 3} using a set method.
s = {1, 2, 3}
s.update({8, 9, 10})
print(s)
# Output: {1, 2, 3, 8, 9, 10}

# Q16: Remove a random element from the set {1, 2, 3} using a set method.
s = {1, 2, 3}
s.pop()
print(s)
# Output: {2, 3}

# Q17: Check if two sets {1, 2, 3} and {3, 2, 1} are equal.
a = {1, 2, 3}
b = {3, 2, 1}
print(a == b)
# Output: True

# Q18: From the list [1, 2, 2, 3, 4, 4, 5], extract only unique values using a set.
lst = [1, 2, 2, 3, 4, 4, 5]
unique_vals = set(lst)
print(unique_vals)
# Output: {1, 2, 3, 4, 5}

# Q19: Convert the set {1, 2, 3} into a list.
s = {1, 2, 3}
lst = list(s)
print(lst)
# Output: [1, 2, 3]

# Q20: From {1, 2, 3, 4, 5}, remove {2, 4} using a set method.
s = {1, 2, 3, 4, 5}
s.difference_update({2, 4})
print(s)
# Output: {1, 3, 5}


