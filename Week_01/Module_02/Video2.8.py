#-----------------------------------------------------------------------------------------------------------------------
# 2.8 (advanced) list comprehension in python
#-----------------------------------------------------------------------------------------------------------------------
# index            0   1   2   3   4   5   6   7   8   9  10
random_numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]
# -ve Index      -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

print(random_numbers)
#-----------------------------------------------------------------------------------------------------------------------
odd_numbers = []
for num in random_numbers:
    if num % 2 == 1:
        odd_numbers.append(num)

print(odd_numbers)
#-----------------------------------------------------------------------------------------------------------------------
odd_numbers = []
for num in random_numbers:
    if num % 2 == 1 and num % 5 == 0:
        odd_numbers.append(num)

print(odd_numbers)
#-----------------------------------------------------------------------------------------------------------------------
# Let's write the same code again, but this time with 'List Comprehension'.
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Syntax: newList = [ expression(element) for element in oldList if condition ]
# To Learn more, visit (https://www.geeksforgeeks.org/python-list-comprehension/).

odd_numbers = [num for num in random_numbers if num % 2 == 1 and num % 5 == 0]
print(odd_numbers)
#-----------------------------------------------------------------------------------------------------------------------
# Let's try another example.

names = ['Sakib', 'Mushfik', 'Liton', 'Mashrafi', 'Tamim']
ages = [38, 39, 34, 40, 37]

for name in names:
    for age in ages:
        print(name, age)
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the same code again, but this time creating List with these name age combination.

names = ['Sakib', 'Mushfik', 'Liton', 'Mashrafi', 'Tamim']
ages = [38, 39, 34, 40, 37]

nameAgeCombination = []
for name in names:
    for age in ages:
        nameAgeCombination.append([name, age])

print(nameAgeCombination)
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the same code again, but this time creating List using 'List Comprehension'.

names = ['Sakib', 'Mushfik', 'Liton', 'Mashrafi', 'Tamim']
ages = [38, 39, 34, 40, 37]

nameAgeCombination = [[name, age] for name in names for age in ages]

print(nameAgeCombination)
#-----------------------------------------------------------------------------------------------------------------------
