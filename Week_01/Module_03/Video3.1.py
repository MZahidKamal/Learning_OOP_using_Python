#-----------------------------------------------------------------------------------------------------------------------
# 3.1 String Immutable and string methods
#-----------------------------------------------------------------------------------------------------------------------
# Single line String can be written in these ways.

name1 = 'Mr. Robert Bosch'
name2 = "Mrs. Julia Bosch"
print(name1, "\n", name2)
#-----------------------------------------------------------------------------------------------------------------------
# Multi line String can be written in this way.

name3 = """Robert Bosch is a pilot,
experienced with 2500 flight hours,
and holding 3 type of flight licences."""
print(name3)
#-----------------------------------------------------------------------------------------------------------------------
# Is we declare a string, using single quotation '', then inside the string want to use ', then it'll show error.
# To skip this problem, escape character [\] can be used. Let's see how.

name4 = 'Mr. Robert\'s wife.'
print(name4)
#-----------------------------------------------------------------------------------------------------------------------
# String is a sequence of character. Like a list. But list is mutable and string is immutable.

# In simple words, a mutable object can be changed/modified after it is created.
# In simple words, an immutable object can’t be changed after it is created.

# There are a plenty of string methods available, worth practicing.

print(name1.lower())            # mr. robert bosch
print(name1.upper())            # MR. ROBERT BOSCH
print(name1.title())            # Mr. Robert Bosch
print(name1.swapcase())         # mR. rOBERT bOSCH
print(name1.capitalize())       # Mr. robert bosch
print(name1.count('o'))         # 2

# To Learn more, visit (https://www.geeksforgeeks.org/python-string-methods/).
#-----------------------------------------------------------------------------------------------------------------------
