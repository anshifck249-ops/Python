# 1. Creating a Python Module

# mymodule.py
def greet(name):
    return f"Hello, {name}!"

# main.py
import mymodule
print(mymodule.greet("Alice"))


# 2. Importing Modules

import math
print(math.sqrt(25))

from math import pi
print(pi)

import math as m
print(m.sqrt(25))


# 3. Built-in Modules

import os
print(os.name)


# 4. Python Module vs Library

# Module = Single Python file
# Example: math, os

# Library = Collection of modules
# Example: NumPy, Pandas, Django


# 5. Standard Libraries

# a. math
import math
print(math.sqrt(16))
print(math.factorial(5))

# b. datetime
from datetime import datetime
now = datetime.now()
print(now)

# c. os
import os
print(os.getcwd())

# d. sys
import sys
print(sys.version)

# e. json
import json
data = '{"name": "John", "age": 30}'
parsed_data = json.loads(data)
print(parsed_data)


# 6. Third-party Libraries

# a. NumPy
import numpy as np
arr = np.array([1, 2, 3])
print(arr)

# b. Pandas
import pandas as pd
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)

# c. Matplotlib
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 40]
plt.plot(x, y)
plt.show()

# d. Requests
import requests
response = requests.get('https://api.github.com')
print(response.status_code)

# e. BeautifulSoup
from bs4 import BeautifulSoup
import requests
page = requests.get("https://example.com")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.title.text)

# f. TensorFlow
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
print(hello)

# g. Django and Flask
# pip install django
# pip install flask

# h. OpenCV
import cv2
img = cv2.imread('image.jpg')
cv2.imshow('Image', img)
cv2.waitKey(0)






