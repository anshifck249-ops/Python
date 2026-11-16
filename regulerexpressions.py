
import re

# # 1. Basic Functions in re Module

# 1. re.search()
text = "Hello world"
print(re.search(r"world", text).group())

# 2. re.match()
text = "Hello world"
print(re.match(r"Hello", text).group())
print(re.match(r"world", text))

# 3. re.findall()
text = "I have 2 apples and 5 oranges."
print(re.findall(r"\d+", text))

text_price = "The price is 45 dollars, 30 cents, and 50 rupees."
print(re.findall(r"\d+", text_price))

# 4. re.finditer()
text = "I have 2 apples and 5 oranges."
for match in re.finditer(r"\d+", text):
    print(match.group(), "at", match.start())

# 5. re.sub()
text = "Hello 123, welcome 456!"
print(re.sub(r"\d+", "number", text))

# 6. re.split()
text = "apple, orange; banana, grape"
print(re.split(r"[;,]\s*", text))


# 2. Grouping & Capturing

text = "John: 34, Alice: 45, Bob: 23"
print(re.findall(r"(\w+): (\d+)", text))


# 3. Compiling Regex

pattern = re.compile(r"\d+")
text = "123 apples and 456 oranges"
print(pattern.findall(text))


# 4. Regex Flags

# 1. re.IGNORECASE
text = "HELLO world"
print(re.search(r"hello", text, re.IGNORECASE).group())

# 2. re.MULTILINE
text = """first line
second line
third line"""

print(re.findall(r"^s\w+", text, re.MULTILINE))
print(re.findall(r"\w+e$", text, re.MULTILINE))

# 3. re.DOTALL
text = "Hello\nWorld"
print(re.search(r"Hello.*World", text))
print(re.search(r"Hello.*World", text, re.DOTALL).group())


# 5. Real-Life Uses of Regular Expressions

# 1. Validation
email = "user@example.com"

if re.fullmatch(r"[\w.-]+@[\w.-]+\.\w+", email):
    print("Valid email")
else:
    print("Invalid email")


# 2. Data Cleaning
text = "Price: $123.45"
print(re.sub(r"[^0-9.]", "", text))


# 3. Text Extraction
tweet = "Excited for #Python3 and following @openai!"
print(re.findall(r"#\w+", tweet))
print(re.findall(r"@\w+", tweet))


# 4. Search & Replace
text = "Card: 1234-5678-9012-3456"
print(re.sub(r"\d{4}-\d{4}-\d{4}-\d{4}",
             "****-****-****-****", text))
