#-----------------------------------------------------------------------------------------------------------------------
# P. Minimize Number
# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P
#-----------------------------------------------------------------------------------------------------------------------
#Taking the input N as the size of the list. And then taking the list input.
N = int(input())
ListA = list(map(int, input().split()))

#Creating some necessary variable and counter.
oddFound = False
operationCounter = 0

#Loop iteration to check even/odd and run the operation.
while not oddFound:
    for num in ListA:
        if num % 2 != 0:
            oddFound = True
            break

    if not oddFound:
        ListA = [num / 2 for num in ListA]
        operationCounter += 1

#Printing the final operation counter.
print(operationCounter)
