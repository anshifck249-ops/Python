# Q1: Create a tuple (1,2,3,4) and access the element 3 using indexing.
t = (1, 2, 3, 4)
print(t[2])
# Output: 3

# Q2: Convert the tuple (10,20,30) into a list.
t = (10, 20, 30)
lst = list(t)
print(lst)
# Output: [10, 20, 30]

# Q3: Convert the list [1,2,3] into a tuple.
lst = [1, 2, 3]
t = tuple(lst)
print(t)
# Output: (1, 2, 3)

# Q4: From the tuple ("a","b","c","d"), extract ("b","c") using slicing.
t = ("a", "b", "c", "d")
print(t[1:3])
# Output: ('b', 'c')

# Q5: Check if "x" exists inside the tuple ("x","y","z").
t = ("x", "y", "z")
print("x" in t)
# Output: True

# Q6: Given (5,3,9,1), find the maximum value using a tuple function.
t = (5, 3, 9, 1)
print(max(t))
# Output: 9

# Q7: Given (1,2,3), create a new tuple (1,2,3,1,2,3) using tuple operations only.
t = (1, 2, 3)
new_t = t * 2
print(new_t)
# Output: (1, 2, 3, 1, 2, 3)

# Q8: Count how many times 2 appears in (1,2,2,3,2) using a tuple method.
t = (1, 2, 2, 3, 2)
print(t.count(2))
# Output: 3

# Q9: Find the index of "cat" in ("dog","cat","mouse").
t = ("dog", "cat", "mouse")
print(t.index("cat"))
# Output: 1

# Q10: Reverse (1,2,3,4,5) using slicing.
t = (1, 2, 3, 4, 5)
print(t[::-1])
# Output: (5, 4, 3, 2, 1)

# Q11: Combine (1,2) and (3,4) into (1,2,3,4) using tuple operations.
a = (1, 2)
b = (3, 4)
print(a + b)
# Output: (1, 2, 3, 4)

# Q12: Convert "hello" into a tuple of characters.
t = tuple("hello")
print(t)
# Output: ('h', 'e', 'l', 'l', 'o')

# Q13: Convert (1,2,3,4) into the list [1,4] by extracting only first & last elements.
t = (1, 2, 3, 4)
lst = [t[0], t[-1]]
print(lst)
# Output: [1, 4]

# Q14: Given a tuple (10,20,30,40), replace the value 30 with 99
# (hint: convert to list → modify → convert back).
t = (10, 20, 30, 40)
temp = list(t)
temp[2] = 99
t = tuple(temp)
print(t)
# Output: (10, 20, 99, 40)

# Q15: Using unpacking, extract a=1, b=2, c=3 from (1,2,3).
a, b, c = (1, 2, 3)
print(a, b, c)
# Output: 1 2 3

# Q16: Create a nested tuple: turn (1,2,3) into ((1,2,3),).
t = (1, 2, 3)
nested = (t,)
print(nested)
# Output: ((1, 2, 3),)

# Q17: Merge ("a","b") with ["c","d"] to get a single tuple ("a","b","c","d")
# (hint: convert list → tuple).
t1 = ("a", "b")
lst = ["c", "d"]
merged = t1 + tuple(lst)
print(merged)
# Output: ('a', 'b', 'c', 'd')

# Q18: Check if tuple (1,2,3) is equal to its reverse.
t = (1, 2, 3)
print(t == t[::-1])
# Output: False

# Q19: Convert a tuple of lists ([1,2],[3,4]) into a single flat list [1,2,3,4].
t = ([1, 2], [3, 4])
flat = t[0] + t[1]
print(flat)
# Output: [1, 2, 3, 4]

# Q20: Given (1, [2,3], 4), add 5 inside the inner list so result becomes (1, [2,3,5], 4).
t = (1, [2, 3], 4)
t[1].append(5)
print(t)
# Output: (1, [2, 3, 5], 4)