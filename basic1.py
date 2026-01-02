# import datetime
# import math
# import json
# import re

# Python Datetime  -- A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
# x = datetime.datetime.now()
# print(x)

# print(x.year)
# print(x.day)
# print(x.month)
# print(x.strftime("%A"))
# print(x.strftime("%B"))

# Python Math -- Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.
# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)

# x = abs(-7.25)
# print(x)

# x = pow(4, 3)
# print(x)

# x = math.sqrt(64)
# print(x)
# x = math.ceil(1.4)
# y = math.floor(1.4)
# print(x)
# print(y)

# Python JSON  -- JSON is a syntax for storing and exchanging data.
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
# y = json.loads(x)
# print(y["age"])

# a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# convert into JSON:
# y = json.dumps(x)
# print(y)

# Python RegEx  -- A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# Python Try Except
# 1. The try block lets you test a block of code for errors.
# 2. The except block lets you handle the error.
# 3. The else block lets you execute code when there is no error.
# 4. The finally block lets you execute code, regardless of the result of the try- and except blocks.
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# x = "hello"
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")

