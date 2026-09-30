# Q1: Create a list [1,2,3] and add 4 to the end using a list method.
lst = [1, 2, 3]
lst.append(4)
print(lst)

# Q2: Given [10,20,30], remove 20 using a list method.
lst = [10, 20, 30]
lst.remove(20)
print(lst)

# Q3: From [5,3,9,1], sort the list in ascending order using a list method.
lst = [5, 3, 9, 1]
lst.sort()
print(lst)

# Q4: From [1,2,3,4,5], extract [2,3,4] using slicing only.
lst = [1, 2, 3, 4, 5]
print(lst[1:4])

# Q5: Reverse the list [1,2,3,4] using slicing (no loops).
lst = [1, 2, 3, 4]
print(lst[::-1])

# Q6: Combine [1,2] and [3,4] into one list using list operations.
a = [1, 2]
b = [3, 4]
print(a + b)

# Q7: Convert [7,8] into [7,8,7,8] using list operations.
lst = [7, 8]
print(lst * 2)

# Q8: Check if 3 exists in [1,2,3,4] using a list operator.
lst = [1, 2, 3, 4]
print(3 in lst)

# Q9: Count how many times 2 appears in [1,2,2,3,2] using a list method.
lst = [1, 2, 2, 3, 2]
print(lst.count(2))

# Q10: Remove the last element from ["a","b","c","d"] using a list method.
lst = ["a", "b", "c", "d"]
lst.pop()
print(lst)

# Q11: Insert "x" at index 1 in ["a","b","c"] using a list method.
lst = ["a", "b", "c"]
lst.insert(1, "x")
print(lst)

# Q12: Replace the element at index 2 in [10,20,30,40] with 99 using indexing.
lst = [10, 20, 30, 40]
lst[2] = 99
print(lst)

# Q13: Convert range(5) into a list using list functions.
lst = list(range(5))
print(lst)

# Q14: Using slicing, extract every 2nd element from [1,2,3,4,5,6] → expected [2,4,6].
lst = [1, 2, 3, 4, 5, 6]
print(lst[1::2])

# Q15: Remove all elements from [1,2,3] using one list method.
lst = [1, 2, 3]
lst.clear()
print(lst)

# Q16: Copy a list [4,5,6] using only list tools (no modules).
lst = [4, 5, 6]
copy_lst = lst.copy()
print(copy_lst)

# Q17: Convert [1,2,3] into a nested list [[1,2,3]] using list operations.
lst = [1, 2, 3]
nested = [lst]
print(nested)

# Q18: Extend [1,2] with [3,4,5] using a list method.
lst = [1, 2]
lst.extend([3, 4, 5])
print(lst)

# Q19: Using list repetition, create a list ["hello","hello","hello"].
lst = ["hello"] * 3
print(lst)

# Q20: Remove the element at index 2 from [10,20,30,40] using a list method.
lst = [10, 20, 30, 40]
del lst[2]
print(lst)