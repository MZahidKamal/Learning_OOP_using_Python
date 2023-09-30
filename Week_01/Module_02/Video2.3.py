#-----------------------------------------------------------------------------------------------------------------------
# 2.3 (advanced) kargs, multiple return from a function
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
# Creating a function which returns multiple value. Let's see how.
def calculate(num1, num2, num3):
    summ = num1 + num2 + num3
    deduction = num1 - num2 - num3
    multiplication = num1 * num2 * num3
    division = num1 / num2 / num3
    return summ, deduction, multiplication, division

# Calling the calculate function.
calc = calculate(5, 15, 20)
print(calc)
#-----------------------------------------------------------------------------------------------------------------------
