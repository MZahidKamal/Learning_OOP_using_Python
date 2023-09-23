# 1.1 Introduction to python and environment setup
#-----------------------------------------------------------------------------------------------------------------------
# History of Python (https://www.geeksforgeeks.org/history-of-python/).
# Python interpreter download link (https://www.python.org/downloads/).
# Currently, the v3.10 is latest and stable version, so I've installed this one.
# Python installation can be checked from cmd, using [python --version] command.
# Some minor Python code can also be executed in cmd, using [python] command. After entering this command, start coding.
# After coding in cmd, is can be closed using [ctrl+z] command. And the [exit] will close the cmd window.
#-----------------------------------------------------------------------------------------------------------------------
# 1.2 Run python code in terminal and VS code
#-----------------------------------------------------------------------------------------------------------------------
"""print("New Journey: Learning Python")
print(123)
print(456)
print(789)"""
#-----------------------------------------------------------------------------------------------------------------------
# 1.3 Basic Data Types and Variables in python
#-----------------------------------------------------------------------------------------------------------------------
# Variable name = value, also let's try with different type of variables.
age = 25                        # int variable
interest_rate = 2.5             # float variable
song = "Dance in the rain"      # string variable with double quotation
area = 'Frankfurt am Main'      # string variable with single quotation
is_single = True                # boolean variable
feeling_sleepy = False          # boolean variable
# To Learn more, visit (https://www.geeksforgeeks.org/python-data-types/).
# To Learn more, visit (https://www.geeksforgeeks.org/python-variables/).

# Try printing the variables.
print(age)
print(interest_rate)
print(age + interest_rate)
print(age * interest_rate)

print(song)
print(area)
print(song + area)

# Try finding the data type of variable using type function.
print(type(age))
print(type(interest_rate))
print(type(song))
print(type(area))
print(type(is_single))
print(type(feeling_sleepy))
# To Learn more, visit (https://www.geeksforgeeks.org/python-type-function/).

# Single line commenting using [#] at the beginning of the line.
# Multiple line commenting using [#] at the beginning of the line or select all and [ctrl+/].
# Multiple line commenting using [""" """] at the beginning and the ending of the code snippet.
