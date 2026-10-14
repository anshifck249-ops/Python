#  Square Star Pattern

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()



#  Pyramid Star Pattern

for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)


#  Reverse Pyramid Star Pattern

for i in range(5, 0, -1):
    print(" " * (5 - i) + "* " * i)


# LeftAligned  Star Pattern

n = 5

for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)