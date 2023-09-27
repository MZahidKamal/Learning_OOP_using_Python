#-----------------------------------------------------------------------------------------------------------------------
# 3.8 (advanced) lamda function in python
#-----------------------------------------------------------------------------------------------------------------------
# Let's create a function.
"""
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

summ = lambda x, y, z: x + y + z
print(summ(10, 20, 30))
"""
#-----------------------------------------------------------------------------------------------------------------------
# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# Syntax:       map(function, iterables)
# During printing, the map should be converted to list, and then print.
# Let's see how map works.

doubled = lambda x: x * 2

# Let's create a list of numbers and then print it.
random_numbers = [12, 56, 98, 78, 56, 12, 6, 98]
print(random_numbers)
print(type(random_numbers))
print()

random_numbers_doubled = map(doubled, random_numbers)
print(list(random_numbers_doubled))
print(type(random_numbers_doubled))
print()
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the same code again, but this time, using direct lambda function.

random_numbers_doubled = map(lambda x: x * 2, random_numbers)
print(list(random_numbers_doubled))
print(type(random_numbers_doubled))
print()
#-----------------------------------------------------------------------------------------------------------------------
# Let's do another example using direct lambda function.

random_numbers_doubled = map(lambda x: x ** 2, random_numbers)
print(list(random_numbers_doubled))
print(type(random_numbers_doubled))
print()
#-----------------------------------------------------------------------------------------------------------------------
# Let's do another example using dictionary.
# But this example is little different.
# We'll see the use of [filter] here.
# Map usually run a function on all elements of the list.
# But [filter] usually run a function on selective elements of the list, based on a conditions.

actors = [
    {'Name': 'Shabana', 'Age': 65},
    {'Name': 'Shabnoor', 'Age': 45},
    {'Name': 'Sabila Noor', 'Age': 30},
    {'Name': 'Srabonti', 'Age': 38},
    {'Name': 'Shaon', 'Age': 47}
]

junior_actors = filter(lambda actor: actor['Age'] < 40, actors)
print(list(junior_actors))
print()

fiver_actors = filter(lambda actor: actor['Age'] % 5 == 0, actors)
print(list(fiver_actors))
#-----------------------------------------------------------------------------------------------------------------------
