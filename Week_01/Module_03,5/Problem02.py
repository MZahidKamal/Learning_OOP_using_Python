#-----------------------------------------------------------------------------------------------------------------------
# K. Sum Digits
# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/K
#-----------------------------------------------------------------------------------------------------------------------
#Taking N input.
N = int(input())

#Creating a string variable, and then taking input into it.
input_string = input()

#Now extracting each character, converting them into int, and the calculating the summ variable.
summ = 0
for c in input_string:
    summ = summ + int(c)

#Printing the final output.
print(summ)
