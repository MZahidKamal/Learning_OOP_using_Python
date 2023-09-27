#-----------------------------------------------------------------------------------------------------------------------
# F. Equation
# https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/F
#-----------------------------------------------------------------------------------------------------------------------
#Taking inputs, splitting and saving them into two variables and converting into list.
X, N = list(map(int, input().split()))

#Creating the 1st part of the equation.
S = (X ** 0) - 1

#Calculating the remaining part of the equation.
power = 2
while power <= N:
    S = S + (X ** power)
    power = power + 2

#Printing the final output.
print(S)
