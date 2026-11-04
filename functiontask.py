
# 1. Write a function that takes a number as input and returns whether the number is even or odd[cite: 1].
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


# 2. Write a function that takes three numbers as input and returns the largest number among them[cite: 1].
def find_largest(a, b, c):
    return max(a, b, c)


# 3. Write a function that takes a list of numbers as input and returns the sum of all elements in the list[cite: 1].
def sum_list(numbers):
    return sum(numbers)


# 4. Write a function that takes a list of numbers as input and returns a new list containing only even numbers[cite: 1].
def get_evens(numbers):
    return [num for num in numbers if num % 2 == 0]


# 5. Write a function that takes a string as input and returns the length of the string[cite: 1].
def string_length(s):
    return len(s)


# 6. Write a function that takes a string as input and returns the string in uppercase[cite: 1].
def to_uppercase(s):
    return s.upper()


# 7. Write a function that takes a number as input and returns whether the number is positive, negative, or zero[cite: 1].
def check_number_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


# 8. Write a function that takes a number as input and returns True if the number is a multiple of both 3 and 5, otherwise returns False[cite: 1].
def is_multiple_of_3_and_5(number):
    return number % 3 == 0 and number % 5 == 0


# 9. Write a function that takes a list of numbers as input and returns the maximum value in the list[cite: 1].
def find_max_value(numbers):
    if not numbers:
        return None
    return max(numbers)


# 10. Write a function that takes marks as input and returns the grade (A for >=90, B for >=75, C for >=60, Fail below 60)[cite: 1].
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"


# 11. Write a function that takes a price as input and returns the discounted price after applying a 10% discount[cite: 1].
def calculate_discounted_price(price):
    return price * 0.9


# 12. Write a function that takes a list of numbers as input and returns the count of even and odd numbers[cite: 1].
def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return {"even": even_count, "odd": odd_count}


# 13. Write a function that takes a temperature in Celsius as input and returns the temperature in Fahrenheit[cite: 2].
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32