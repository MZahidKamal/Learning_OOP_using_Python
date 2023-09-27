#-----------------------------------------------------------------------------------------------------------------------
# Y. Easy Fibonacci
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Y
#-----------------------------------------------------------------------------------------------------------------------
# Index              1  2  3  4  5  6  7   8   9  10
# Fibonacci Series: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#Taking input and saving into a variable.
N = int(input())

#Creating the function to nth value of Fibonacci series.
def fib(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

#Finding the values of Fibonacci series and saving them into a list.
for x in range(1, N+1):
    print(fib(x), end=" ")

