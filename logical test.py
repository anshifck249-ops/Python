def solve():
    arr = list(map(int, input("Enter array elements: ").split()))

    even = []
    odd = []

    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    print("Even numbers in the array:", *even)
    print("Odd numbers in the array:", *odd)
    print("Largest element:", max(arr))
    print("Smallest element:", min(arr))
    print("Sum of all elements:", sum(arr))
    print("Sum of even numbers:", sum(even))
    print("Sum of odd numbers:", sum(odd))
    print("Count of even numbers:", len(even))
    print("Count of odd numbers:", len(odd))

    n = int(input("Enter the number of rows: "))
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

solve()