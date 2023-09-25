#-----------------------------------------------------------------------------------------------------------------------
# 2.4 local and global scope in python
#-----------------------------------------------------------------------------------------------------------------------
balance = 3000

def buy_things(item, price):
    print(f'Balance after buying {item} is {balance}.')

buy_things('sunglass', 1000)

# See the above code. Global variable can be accessed from any function inside.
#-----------------------------------------------------------------------------------------------------------------------
balance1 = 3000

def buy_things(item, price):
    # balance1 = balance1 - price
    print(f'Balance after buying {item} is {balance1}.')

buy_things('sunglass', 1000)

# See the above code. Now the Global variable can't be accessed from the function inside.
# Because local variable is present already. So it's showing error.
#-----------------------------------------------------------------------------------------------------------------------
balance2 = 3000

def buy_things(item, price):
    balance2 = 2000
    balance2 = balance2 - price
    print(f'Balance after buying {item} is {balance2}.')

buy_things('sunglass', 1000)

# See the above code. Now the function is accessing the local variable balance2.
# and the global variable balance2 is playing no roll.
#-----------------------------------------------------------------------------------------------------------------------
# So there are two ways to get rid of this problem.
# 1. Take the global variable inside the function as an argument.
# 2. Or use a keyword [global]. Let's learn this one.

balance3 = 3000

def buy_things(item, price):
    global balance3
    balance3 = balance3 - price
    print(f'Balance after buying {item} is {balance3}.')

buy_things('sunglass', 1000)

# Global variable can be accessed from inside any function, as long as there is no local variable of same name.
# Global variable can be accessed from inside any function, along with local variable, by using [global] keyword.
# Global variable can also be modified from inside any function, along with local variable, by using [global] keyword.
# #-----------------------------------------------------------------------------------------------------------------------
