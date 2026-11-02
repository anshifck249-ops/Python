def add(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i

    print("Sum =", total)

n = int(input("Enter a number: "))
add(n)