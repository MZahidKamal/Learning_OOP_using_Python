# -----------------------------------------------------------------------------------------------------------------------
# 3.7 Try except finally and file read write in python
# -----------------------------------------------------------------------------------------------------------------------
# 8.3. Handling Exceptions
# 8.7. Defining Clean-up Actions
# https://docs.python.org/3/tutorial/errors.html
# -----------------------------------------------------------------------------------------------------------------------

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# Try the above code with 9 and -9.
# -----------------------------------------------------------------------------------------------------------------------
# The try statement works as follows:
#    1. First, the statement(s) between the try and except keywords is executed.
#    2. If no error/exception occurs, the except clause is skipped and execution of the try statement is finished.
#    3. If an error/exception occurs during execution of the try clause, the rest of the clause is skipped.
#    4. Then, the except clause will be executed.
#    5. A try statement may have more than one except clause.
# -----------------------------------------------------------------------------------------------------------------------
# This is another version.

def bool_return():
    try:
        return True
    finally:
        return False


# -----------------------------------------------------------------------------------------------------------------------
# This is another complicated version.

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


# -----------------------------------------------------------------------------------------------------------------------
# result = 45/0       # Which will produce obvious error. So let's see, how we can handle the exception here.

try:
    result = 45 / 5
except:
    print('Infinite result. Exception handled.')
finally:
    print('Finally execution completed.')

print('Done')

# Try the above code with 0 and 5.
#-----------------------------------------------------------------------------------------------------------------------
# File handling in Python
# .csv file => Comma Separated Value
# .txt file => Text file

# Creating a text file and writing in it.
# with open('TextFile.txt', 'w') as file:
#     file.write('I Love You Python !!\n')

# Appending the same text file.
# with open('TextFile.txt', 'a') as file:
#     file.write('I Love You Python !!\n')

# Reading the same text file.
with open('TextFile.txt', 'r') as file:
    text = file.read()
    print(text)

# To Learn more, visit (https://docs.python.org/3/library/filesys.html).
#-----------------------------------------------------------------------------------------------------------------------
