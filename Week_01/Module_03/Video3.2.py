#-----------------------------------------------------------------------------------------------------------------------
# 3.2 tuples and tuples methods in python
#-----------------------------------------------------------------------------------------------------------------------
# Python has 4 built-in Data Types, to store collection od data. Not single Data.
# List, Tuple, Set, Dictionary.

# x = ["apple", "banana", "cherry"]
# x = ("apple", "banana", "cherry")
# x = {"apple", "banana", "cherry"}
# x = {"name" : "John", "age" : 36}

# All of them with different qualities and different usage.
#-----------------------------------------------------------------------------------------------------------------------

# List items are ordered, changeable, and allow duplicate values.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Dictionary items are ordered, changeable, and does not allow duplicates.

#-----------------------------------------------------------------------------------------------------------------------
# Let's see how to return List, Tuple, Set and Dictionary from a function.
def multiple():
    return [3, 4]

print(multiple())
print(type(multiple()))

# The above function returned elements in a List.
# Necessary methods for List (https://www.geeksforgeeks.org/list-methods-in-python/).
#-----------------------------------------------------------------------------------------------------------------------
def multiple():
    return 3, 4

print(multiple())
print(type(multiple()))

# The above function returned elements in a Tuple.
# Necessary methods for Tuple (https://www.geeksforgeeks.org/python-tuple-methods/).
#-----------------------------------------------------------------------------------------------------------------------
def multiple():
    return {3, 4}

print(multiple())
print(type(multiple()))

# The above function returned elements in a Set.
# Necessary methods for Set (https://www.geeksforgeeks.org/python-set-methods/).
#-----------------------------------------------------------------------------------------------------------------------
def multiple():
    return {3: 4}

print(multiple())
print(type(multiple()))

# The above function returned elements in a Dictionary.
# Necessary methods for Dictionary (https://www.geeksforgeeks.org/python-dictionary-methods/).
#-----------------------------------------------------------------------------------------------------------------------
# These data type can contain another data type in it. Let's say...
# list = ["tupple", "tupple", "tupple"]
# tupple = ("list", "list", "list")
#-----------------------------------------------------------------------------------------------------------------------
