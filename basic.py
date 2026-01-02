# Hello world program
# print('hello world')

# conditional formet
# if 5 > 2 :
#     print("Five is greater then Two")

# variables
# x= 20
# y = "Sanju Don"
# print(x)
# print(y)

# x = 4       
# x = "Sally"
# print(x)

# x = str(3)    
# y = int(3)  
# z = float(3)
# print(x, y, z)

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# print(myvar)
# print(my_var)
# print(_my_var)
# print(myVar)
# print(MYVAR)
# print(myvar2)

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Camel Case
# Pascal Case
# Snake Case

# Many Values to Multiple Variables
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# Many Variables to single variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# Unpack a Collection  (list, tuple)
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
# dict
# x = {username: "sanju", age: 25}
# print(x)
# set
# x= ("baba", "job", "berojgar")
# print(x)


# Error
# x = 5
# y = "John"
# print(x + y)

# Global Variables
# x= "awesome"
# def myFun():
#     print("Python is", x)

# myFun()

# x = "awesome"
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()
# print("Python is " + x)

# If you use the global keyword, the variable belongs to the global scope:
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()
# print("Python is " + x)

# List  // ordered, changeable, allow deplicates
# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# print(len(thislist))

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# Tuple // ordered, unchangeable, allow deplicates
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)

# Set // A set is a collection which is unordered, unchangeable*, and unindexed.
# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# Dictionaries A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# for x, obj in myfamily.items():
#     print(x)
    
#     for y in obj:
#         print(y + ':', obj[y])

# if, elif, else
# age = 25
# is_student = False
# has_discount_code = True

# if (age < 18 or age > 65) and not is_student or has_discount_code:
#   print("Discount applies!")

# The pass Statement
# age = 16

# if age < 18:
#   pass # TODO: Add underage logic later
# else:
#   print("Access granted")

# Match Statement
# day = 4
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")
#   case _:
#     print("Looking forward to the Weekend")

# Python Loops
# Python has two primitive loop commands:
# while loops
# for loops

# while Loop
# i = 1
# while i < 6:
#   print(i)
#   i += 1

# break, continue Statement
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break #continue
#   i += 1

# For Loops
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# Python Functions
# def my_function():
#   print("Hello from a function")

# my_function()

# Without functions - repetitive code:
# temp1 = 77
# celsius1 = (temp1 - 32) * 5 / 9
# print(celsius1)

# temp2 = 95
# celsius2 = (temp2 - 32) * 5 / 9
# print(celsius2)

# temp3 = 50
# celsius3 = (temp3 - 32) * 5 / 9
# print(celsius3)

# def fahrenheit_to_celsius(fahrenheit):
#   return (fahrenheit - 32) * 5 / 9

# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(95))
# print(fahrenheit_to_celsius(50))

# Python Scope
# def myfunc():
#   x = 300
#   print(x)

# myfunc()
# Function Inside Function
# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc()

# Global Scope
# x = 300

# def myfunc():
#   print(x)

# myfunc()
# print(x)

# The LEGB Rule
# 1. Local - Inside the current function
# 2. Enclosing - Inside enclosing functions (from inner to outer)
# 3. Global - At the top level of the module
# 4. Built-in - In Python's built-in namespace

# x = "global"

# def outer():
#   x = "enclosing"
#   def inner():
#     x = "local"
#     print("Inner:", x)
#   inner()
#   print("Outer:", x)

# outer()
# print("Global:", x)

# Python Decorators  -- A decorator is a function that takes another function as input and returns a new function.
# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())

# Multiple Decorator Calls
# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())

# Arguments in the Decorated Function
# def changecase(func):
#   def myinner(x):
#     return func(x).upper()
#   return myinner

# @changecase
# def myfunction(nam):
#   return "Hello " + nam

# print(myfunction("John"))

# Lambda Functions
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# Python Recursion
# def countdown(n):
#   if n <= 0:
#     print("Done!")
#   else:
#     print(n)
#     countdown(n - 1)

# countdown(5)

# def factorial(n):
#   # Base case  -- A condition that stops the recursion
#   if n == 0 or n == 1:
#     return 1
#   # Recursive case  -- The function calling itself with a modified argument
#   else:
#     return n * factorial(n - 1)

# print(factorial(5))

