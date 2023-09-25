#-----------------------------------------------------------------------------------------------------------------------
# 2.1 Introduction to functions in python
#-----------------------------------------------------------------------------------------------------------------------
# Creating a user defined function to make a number double and print it. This function will not return anything.
# After creating a function it's necessary to keep two blank lines.
def double_this_number(num):
    result = num * 2
    print(result)


# Calling the double_this_number function.
double_this_number(10)
double_this_number(15)
double_this_number(10.5)
double_this_number(22.45)


#-----------------------------------------------------------------------------------------------------------------------
# Creating a user defined function to add two numbers and return it. This returned value can be saved into a variable.
def add_two_numbers(num1, num2):
    result = num1 + num2
    return result


# Calling the double_this_number function.
x = add_two_numbers(5, 15)
print(x)
y = add_two_numbers(5.30, 15.40)
print(y)


#-----------------------------------------------------------------------------------------------------------------------
# Let's use the double_this_number function again. Example of using a function into another function.
double_this_number(x)
double_this_number(y)
#-----------------------------------------------------------------------------------------------------------------------
