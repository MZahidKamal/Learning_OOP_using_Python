#-----------------------------------------------------------------------------------------------------------------------
# 2.5 Built-in functions and import modules
#-----------------------------------------------------------------------------------------------------------------------
# To Learn more, visit (https://docs.python.org/3/library/functions.html).

"""A
abs()
all()
any()
ascii()

B
bin()
bool()
breakpoint()
bytearray()
bytes()

C
chr()
classmethod()
compile()
complex()

D
dict()
dir()

E
enumerate()

F
float()

G
globals()

H
hash()
hex()

I
id()
input()
int()
isinstance()
issubclass()
iter()

L
len()
list()
locals()

M
map()
max()
min()

O
oct()
open()
ord()

P
pow()
print()
property()

R
range()
reversed()
round()

S
set()
slice()
sorted()
str()
sum()
super()

T
tuple()
type()
"""

# These are the function we'll be using mostly.
#-----------------------------------------------------------------------------------------------------------------------
highest = max(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(highest)

highest = max([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(highest)

smallest = min(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(smallest)

smallest = min([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(smallest)

length = len([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(length)

total = sum([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(total)
#-----------------------------------------------------------------------------------------------------------------------
# If we need to use any function, which is not in this file, but in another file.
# Rather than writing the function again, we can call the function from another file using [from, import] function.
from RandomAnotherFile import add_two_numbers

result = add_two_numbers(40, 50)
print(result)
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the same code again, but this time, using [as] keyword.
from RandomAnotherFile import add_two_numbers as summ

result = summ(40, 50)
print(result)
#-----------------------------------------------------------------------------------------------------------------------
# If we want to import all functions from another file, then we can use [import *]´. Let's see how.
from RandomAnotherFile import *

result = add_two_numbers(40, 50)
print(result)
#-----------------------------------------------------------------------------------------------------------------------
