"""
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Q.A. Write the difference between List and Dictionary of Python.
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Answer:
1. List items are ordered, changeable, and allow duplicate values, whereas Dictionary items are ordered, changeable but
does not allow duplicates.
2. List denotes its elements using [], whereas Dictionary denotes its elements using {}.
3. List elements are single elements, whereas Dictionary elements are paired as 'Key': 'Value'.
4. List is mutable with some methods like, index(), insert(), append(), copy(), count(), sort(), reverse(), extend(),
pop(), remove() and clear(). Whereas, Dictionary is also mutable but with some different methods like, clear(), copy(),
fromkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), update(), values().

//------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Q.A. Write about *args and **kwargs of Python with proper examples.
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Answer:

# Creating a user defined function to add two numbers and return it.
def summ2(num1, num2):
    result = num1 + num2
    return result

# Calling the summ function.
x = summ2(5, 15)
print(x)

# When we created the function above, positional arguments were 2.
# So during calling the function we'll provide only 2 parameters. Otherwise, it'll show error.
#-----------------------------------------------------------------------------------------------------------------------
# If we want to keep one or more positional argument OPTIONAL, then we can set a default value 0. Let's see how.
def summ3(num1, num2, num3=0, numm4=0):
    result = num1 + num2 + num3 + numm4
    return result

# Calling the summ function.
x = summ3(5, 15, 20, 25)
print(x)
y = summ3(5, 15, 20)
print(y)
z = summ3(5, 15)
print(z)

# To run the sum3 function, minimum 2 parameters should be given.
# 3rd and 4th parameters are optional, can be given or not.
#-----------------------------------------------------------------------------------------------------------------------
# If we do not know how many arguments that will be passed into your function, add a * before the parameter name.
# This way the function will receive a tuple of arguments, and can access/print the items accordingly.
# This is called *args.
def num4(*args):
    print(args)

num4(1, 2, 3, 4, 5)
#-----------------------------------------------------------------------------------------------------------------------
# This Tuple can also be accessed/print using for loop.
def num5(*args):
    for num in args:
        print(num)

num5(6, 7, 8, 9, 10)
#-----------------------------------------------------------------------------------------------------------------------
# Taking positional arguments and +args together in a function is also possible.
def num6(num1, num2, *args):
    for num in args:
        print(num)

num6(11, 12, 13, 14, 15)
#-----------------------------------------------------------------------------------------------------------------------
# Taking positional arguments and +args together in a function is also possible.
def num7(num1, num2, *args):
    summ = 0
    for num in args:
        summ += num
    print(summ + num1 + num2)

num7(11, 12, 13, 14, 15)
#-----------------------------------------------------------------------------------------------------------------------
# Creating a function and using f-sting into it.
def full_name(first, last):
    name = f'The full name is {first} {last}'
    print(name)

full_name('Robert', 'Bosch')
# In the above line, when we called the function, we have provided the parameters serially.

# In Python, we also can provide parameters without maintaining the serial. Let's see how.
# In this case we'll use the positional argument names. So this is called
full_name(last='Bosch', first='Robert')
#In both cases, the printed output will be same.
#-----------------------------------------------------------------------------------------------------------------------
def full_name(first, last, **additional):
    name = f'The full name is {first} {last} {additional}'
    print(name)

full_name(last='Bosch', first='Robert', salutation='Eng.', degree='P.Hd.')

# In the above code, we've used **additional to take any/unknown number of parameters.
# This is called keyword args or **kargs.
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the same code again, but this time we'll print the additional positional arguments one by one.
def full_name(first, last, **additional):
    name = f'The full name is {first} {last}'
    print(name, additional['salutation'], additional['degree'])

full_name(last='Bosch', first='Robert', salutation='Eng.', degree='P.Hd.')
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the same code again, but this time we'll print the additional positional arguments using a loop.
def full_name(first, last, **additional):
    name = f'The full name is {first} {last}'
    print(name)
    for key, value in additional.items():
        print(key, value)

full_name(last='Bosch', first='Robert', salutation='Eng.', degree='P.Hd.')
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the same code again, but this time with *args and **kargs.
def profile_info(first, last, *subjects, **marks):
    profile = f'Student Name: {first} {last}'
    print(profile)
    for sub in subjects:
        print(f'Subject: {sub}, Marks: {marks.get(sub, "N/A")}')

profile_info('Robert', 'Bosch', 'Math', 'English', 'Physics', Math=90, English=85, Physics=92)
#-----------------------------------------------------------------------------------------------------------------------
"""