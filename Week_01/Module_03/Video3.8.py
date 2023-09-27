#-----------------------------------------------------------------------------------------------------------------------
# 3.8 (advanced) lamda function in python
#-----------------------------------------------------------------------------------------------------------------------
# Let's create a function.

def double_it(x):
    return x * 2

result = double_it(25)
print(result)

#-----------------------------------------------------------------------------------------------------------------------
# In Python the lambda keyword is used to create anonymous functions.
# An anonymous function means that a function is without a name.
# Syntax
#       lambda arguments : expression
# This function can have any number of arguments but only one expression, which is evaluated and returned.

# Let's create the same function again, but this time using Lambda keyword.

doubled = lambda x: x * 2
squared = lambda x: x ** 2
print(doubled(44))
print(squared(9))
#-----------------------------------------------------------------------------------------------------------------------
# Let's write another function using Lambda, but this time using multiple arguments.

summ = lambda x, y, z : x + y + z
print(summ(10, 20, 30))
#-----------------------------------------------------------------------------------------------------------------------
