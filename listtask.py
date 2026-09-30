# 1
lst = [1, 2, 3]
lst.append(4)
print(lst)                          # [1, 2, 3, 4]

# 2
lst = [10, 20, 30]
lst.remove(20)
print(lst)                          # [10, 30]

# 3
lst = [5, 3, 9, 1]
lst.sort()
print(lst)                          # [1, 3, 5, 9]

# 4
lst = [1, 2, 3, 4, 5]
print(lst[1:4])                     # [2, 3, 4]

# 5
lst = [1, 2, 3, 4]
print(lst[::-1])                    # [4, 3, 2, 1]

# 6
a = [1, 2]
b = [3, 4]
print(a + b)                        # [1, 2, 3, 4]

# 7
lst = [7, 8]
print(lst * 2)                      # [7, 8, 7, 8]

# 8
lst = [1, 2, 3, 4]
print(3 in lst)                     # True

# 9
lst = [1, 2, 2, 3, 2]
print(lst.count(2))                 # 3

# 10
lst = ["a", "b", "c", "d"]
lst.pop()
print(lst)                          # ['a', 'b', 'c']

# 11
lst = ["a", "b", "c"]
lst.insert(1, "x")
print(lst)                          # ['a', 'x', 'b', 'c']

# 12
lst = [10, 20, 30, 40]
lst[2] = 99
print(lst)                          

# 13
lst = list(range(5))
print(lst)                         

# 14
lst = [1, 2, 3, 4, 5, 6]
print(lst[1::2])                   

# 15
lst = [1, 2, 3]
lst.clear()
print(lst)                        

# 16
lst = [4, 5, 6]
copy_lst = lst.copy()
print(copy_lst)                    

# 17
lst = [1, 2, 3]
nested = [lst]
print(nested)                       

# 18
lst = [1, 2]
lst.extend([3, 4, 5])
print(lst)                          

# 19
lst = ["hello"] * 3
print(lst)                         

# 20
lst = [10, 20, 30, 40]
del lst[2]
print(lst)                          