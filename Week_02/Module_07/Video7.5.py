#-----------------------------------------------------------------------------------------------------------------------
# 7.5 (optional) How does decorator work
#-----------------------------------------------------------------------------------------------------------------------
def timer():
    def inner():
        print('Time started.')

        print('Time ended.')
    return inner

timer()()
print('-----')

#If we call only timer(), then we'll get return the name of the inner function. But to execute the inner function we
#must give another (). Then we'll get the desired output.

#-----------------------------------------------------------------------------------------------------------------------
#Let's see another example.

def timer(func):
    def inner():
        print('Time started.')
        print(func)
        print('Time ended.')
    return inner

@timer
def get_factorial():
    print('Factorial starting.')

# timer(get_factorial)
# print('-----')
# timer(get_factorial)()
# print('-----')
# timer(get_factorial())()
# print('-----')

#A function can be called from another function in various ways. But the easiest way to do this is by using decorator.

get_factorial()

#If we add [@timer] just above the get_factorial function(), and then if we call the get_factorial() function, then
#actually this [ timer(get_factorial)() ] is executing.

#-----------------------------------------------------------------------------------------------------------------------

#Let's see another example.
import math

def timer(func):
    def inner(n):
        print('Time started.')
        func(n)
        print('Time ended.')
    return inner

@timer
def get_factorial(n):
    print('Factorial starting.')
    result = math.factorial(n)
    print(f'Factorial of {n} is {result}.')

get_factorial(5)

#-----------------------------------------------------------------------------------------------------------------------

#Let's see another example.

def timer(func):
    def inner(*args):
        print('Time started.')
        func(*args)
        print('Time ended.')
    return inner

@timer
def get_factorial(n):
    print('Factorial starting.')
    result = math.factorial(n)
    print(f'Factorial of {n} is {result}.')

get_factorial(6)

#-----------------------------------------------------------------------------------------------------------------------

#Let's see another example.

def timer(func):
    def inner(*args, **kwargs):
        print('Time started.')
        func(*args, **kwargs)
        print('Time ended.')
    return inner

@timer
def get_factorial(n):
    print('Factorial starting.')
    result = math.factorial(n)
    print(f'Factorial of {n} is {result}.')

get_factorial(n=7)

#-----------------------------------------------------------------------------------------------------------------------

#Let's see another example.
import time

def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        print(f'Time started at {start}.')
        func(*args, **kwargs)
        end = time.time()
        print(f'Time ended at {end}.')
        print(f'Total duration is {end - start} minute.')
    return inner

@timer
def get_factorial(n):
    print('Factorial starting.')
    result = math.factorial(n)
    print(f'Factorial of {n} is {result}.')

get_factorial(n=120)

#-----------------------------------------------------------------------------------------------------------------------
