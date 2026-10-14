#  CONDITIONAL & CONTROL STATEMENTS


# Q1. Check whether a number is positive, negative, or zero.
# num = float(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# # Q2. Check if a number is even or odd.
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# # Q3. Check if a number is greater than 100.
# num = int(input("Enter a number: "))
# if num > 100:
#     print("Greater than 100")
# else:
#     print("Not greater than 100")


# Q4. Check voting eligibility (age >= 18).
# age = int(input("Enter age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")


# Q5. Print the greater of two numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print(a)
# elif b > a:
#     print(b)
# else:
#     print("Both numbers are equal")


# Q6. Print the largest of three numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a >= b and a >= c:
#     print(a)
# elif b >= a and b >= c:
#     print(b)
# else:
#     print(c)


# # Q7. Check whether a year is a leap year.
# year = int(input("Enter year: "))
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# # Q8. Print Pass or Fail (mark >= 40).
# mark = int(input("Enter mark: "))
# if mark >= 40:
#     print("Pass")
# else:
#     print("Fail")


# # Q9. Print grades.
# mark = int(input("Enter mark: "))
# if mark >= 90:
#     print("A")
# elif mark >= 75:
#     print("B")
# elif mark >= 60:
#     print("C")
# else:
#     print("Fail")


# # Q10. Check whether a character is a vowel or consonant.
# ch = input("Enter a character: ").lower()
# if len(ch) != 1 or not ch.isalpha():
#     print("Invalid character")
# elif ch in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")


# # Q11. Print numbers from 1 to 10 but stop at 6.
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)


# # Q12. Print numbers from 1 to 10 but skip 5.
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)


# # Q13. Use pass inside an if block.
# num = int(input("Enter a number: "))
# if num > 0:
#     pass
# print("pass does nothing and prevents a syntax error in an empty block.")


# # Q14. Print all even numbers between 1 and 20.
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)


# # Q15. Find the sum of numbers from 1 to 10.
# total = 0
# for i in range(1, 11):
#     total += i
# print("Sum:", total)


# # Q16. Check whether a number is a multiple of both 3 and 5.
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print("Multiple of both 3 and 5")
# else:
#     print("Not a multiple of both 3 and 5")


# # Q17. Print Hello five times.
# for i in range(5):
    # print("Hello")


# # Q18. Print numbers greater than 3.
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num > 3:
#         print(num)


# Q19. Advanced Login System.
# for attempt in range(1, 4):
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username.lower() == "anshif" and password == "1234":
#         print("Login successful")
#         break
#     else:
#         remaining = 3 - attempt
#         print("Incorrect username or password")
#         print("Attempts remaining:", remaining)
# else:
#     print("Account locked")


# # Q20. Enhanced Traffic Light Controller.
# signal = input("Enter signal (1/red, 2/yellow, 3/green): ").lower()

# if signal in ("1", "red"):
#     print("Stop and wait for 60 seconds")
# elif signal in ("2", "yellow"):
#     print("Ready and wait for 5 seconds")
# elif signal in ("3", "green"):
#     print("Go and drive safely")
# else:
#     print("Invalid signal")




