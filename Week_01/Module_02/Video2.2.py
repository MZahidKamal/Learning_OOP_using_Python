#-----------------------------------------------------------------------------------------------------------------------
# 2.2 Default parameters and args in python
#-----------------------------------------------------------------------------------------------------------------------
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
# To Learn more, visit (https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp).
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
