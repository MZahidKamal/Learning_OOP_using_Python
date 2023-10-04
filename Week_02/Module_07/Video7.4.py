#-----------------------------------------------------------------------------------------------------------------------
# 7.4 Understanding inner function and wrapper function
#-----------------------------------------------------------------------------------------------------------------------
# Function is a first class object in Python.
# In Python, a function can be created inside another function. Let's see how.

def outer_function():
    print('Executing Outer Function.')

    def inner_function():
        print('Executing Inner Function.')
        return 12345
    return inner_function

print('-----')
print(outer_function())
print('-----')
print(outer_function()())
print('-----')

#-----------------------------------------------------------------------------------------------------------------------
#Let's see another example.

def do_something(work):
    print('Work started...')
    print(work)
    print('Work ended...')

do_something('Driving')
print('-----')
do_something(100)
print('-----')

#-----------------------------------------------------------------------------------------------------------------------
#Let's see another example.

def do_something(work):
    print('Work started...')
    work()
    print('Work ended...')

def coding():
    print('Coding in Python.')

do_something(coding)

#-----------------------------------------------------------------------------------------------------------------------
