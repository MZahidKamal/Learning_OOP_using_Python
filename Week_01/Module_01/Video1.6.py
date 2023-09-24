#-----------------------------------------------------------------------------------------------------------------------
# 1.6 Conditional Statement in python
#-----------------------------------------------------------------------------------------------------------------------
# Identity Operators in Python
# is        = True if the operands are identical
# is not    = True if the operands are not identical
#-----------------------------------------------------------------------------------------------------------------------
# Membership Operators in Python
# in        = True if value is found in the sequence
# not in    = True if value is not found in the sequence
#-----------------------------------------------------------------------------------------------------------------------
# [if + elif + else] statement in Python
a = 5
b = 10

if a > b:
    print("a is larger")
elif a == b:
    print("a and b are equal")
else:
    print("b is larger")
#-----------------------------------------------------------------------------------------------------------------------
# [If + else + is] statement with boolean in Python
boss = True

if boss is True:
    print("Win the boss")
else:
    print("Fire the boss")
#-----------------------------------------------------------------------------------------------------------------------
# [if + else + is not] statement with boolean in Python
boss = False

if boss is True:
    print("Win the boss")
elif boss is not True:
    print("Fire the boss")
#-----------------------------------------------------------------------------------------------------------------------
# Nested loop
weather = "sunnyday"
day = "sunday"
condition = "feeling windy"
time = 12

if weather == "sunnyday":
    if day == "sunday":
        if condition == "feeling windy":
            if time == 12:
                print("I am enjoying the weekend.")
            else:
                print("It's working day and I am working.")
        else:
            print("It's rainy outside.")
    else:
        print("It's a weekday.")
else:
    print("I am not in the right mode.")
#-----------------------------------------------------------------------------------------------------------------------
