


# 3. Opening and Closing Files



# file = open("sample.txt", "r")
# file.close()


# # 4. Reading Files

# # read()

# file = open("sample.txt", "r")
# content = file.read()
# print(content)
# file.close()


# # readline()

# file = open("sample.txt", "r")
# line1 = file.readline()
# print(line1)
# file.close()


# # readlines()

# file = open("sample.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()


# # 5. Writing to Files

# write()

# file = open("sample.txt", "w")
# file.write("Hello, World anshif how are you!")
# file.close()


# # writelines()

# file = open("sample.txt", "w")
# lines = ["Hello\n", "Welcome to Python\n"]
# file.writelines(lines)
# file.close()


# # 6. Appending Data

# file = open("sample.txt", "a")
# file.write("Appended text.\n")
# file.close()


# # 7. Using with Statement

# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)


# # 8. File Positioning (Seek and Tell)

# file = open("sample.txt", "r")

# position = file.tell()
# print(position)

# file.seek(5)
# print(file.read())

# file.close()




