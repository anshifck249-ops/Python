
# 1. FILE HANDLING (Q1 - Q8)

# Q1. Create a file and write text
f = open("data.txt", "w")
f.write("Hello File Handling")
f.close()

# Q2. Read a file
f = open("data.txt", "r")
print(f.read())
f.close()

# Q3. Append text
f = open("data.txt", "a")
f.write("\nPython is awesome")
f.close()

# Q4. Count number of lines
f = open("data.txt", "r")
print("Lines:", len(f.readlines()))
f.close()

# Q5. Count number of words
f = open("data.txt", "r")
print("Words:", len(f.read().split()))
f.close()

# Q6. Copy one file into another
f = open("data.txt", "r")
data = f.read()
f.close()

f = open("copy.txt", "w")
f.write(data)
f.close()

# Q7. Print lines containing Python
f = open("data.txt", "r")
for line in f:
    if "Python" in line:
        print(line)
f.close()

# Q8. Sum of numbers in a file
f = open("numbers.txt", "r")
total = 0
for n in f:
    total += int(n)
print("Sum:", total)
f.close()


# 2. EXCEPTION HANDLING (Q9 - Q15)

# Q9. Handle ValueError
try:
    n = int(input("Enter number: "))
    print(n)
except ValueError:
    print("Invalid input")

# Q10. Handle invalid input
try:
    n = float(input("Enter number: "))
    print(n)
except ValueError:
    print("Invalid number")

# Q11. Handle FileNotFoundError
try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File not found")

# Q12. Using try, except and else
try:
    n = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("Number:", n)

# Q13. Using try, except and finally
try:
    n = int(input("Enter number: "))
    print(n)
except ValueError:
    print("Invalid input")
finally:
    print("Program ended")

# Q14. Multiple exceptions
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a / b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Q15. Raise custom error
try:
    n = int(input("Enter number: "))
    if n < 0:
        raise ValueError("Negative number not allowed")
    print(n)
except ValueError as e:
    print(e)


# 3. MODULES & LIBRARIES (Q16 - Q21)

# Q16. Square root
import math
n = int(input("Enter number: "))
print(math.sqrt(n))

# Q17. Power
import math
a = int(input("Enter base: "))
b = int(input("Enter power: "))
print(math.pow(a, b))

# Q18. Factorial
import math
n = int(input("Enter number: "))
print(math.factorial(n))


