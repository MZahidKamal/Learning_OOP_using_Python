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
# Multiple line commenting is also known as doc string.

# String concatenation in Python.
print(song + area)
print('Dance in the rain' + ' ' + 'Frankfurt am Main')
# To Learn more, visit (https://www.geeksforgeeks.org/python-string-concatenation/).


# f-String in Python.
text = f"Zahid kamal {age}, living in {area}, saving {interest_rate}% as Zakat."
print(text)
# To Learn more, visit (https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/).
#-----------------------------------------------------------------------------------------------------------------------
