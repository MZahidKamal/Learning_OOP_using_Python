#-----------------------------------------------------------------------------------------------------------------------
# 3.5 built in modules time, math, random, etc
#-----------------------------------------------------------------------------------------------------------------------
from math import *
from random import *
from time import *
from datetime import *

# To Learn more, visit (https://docs.python.org/3/py-modindex.html).

# Let's try the [math] — Mathematical functions.
# https://docs.python.org/3/library/math.html#module-math

# To use math functions, first we'll import all [*] function from math library. See header section.

n = 4.5678
Nc = ceil(n)
print(Nc)

Nf = floor(n)
print(Nf)
#-----------------------------------------------------------------------------------------------------------------------
# Let's try the [random] — Random functions.
# https://docs.python.org/3/library/random.html#module-random

# To use random functions, first we'll import all [*] function from math library. See header section.
print(random())
# It will provide any random number from 0 to 1.
#-----------------------------------------------------------------------------------------------------------------------
print(randint(1, 101))
# It will provide any random number from 1 to 100.
#-----------------------------------------------------------------------------------------------------------------------
players = ['hasan', 'sakib', 'asif', 'imran', 'navid', 'reyan', 'saad', 'salman', 'firoze', 'faysal']
print(choice(players))
# It will print any random name, from this given array.
#-----------------------------------------------------------------------------------------------------------------------
# Let's try the [time] — Time access and conversions.
# https://docs.python.org/3/library/time.html#module-time

# To use time functions, first we'll import all [*] function from time library. See header section.
sleep(4)
print('Sleep finished')
# It will wait/delay 4 seconds and then execute the next line.
#-----------------------------------------------------------------------------------------------------------------------
