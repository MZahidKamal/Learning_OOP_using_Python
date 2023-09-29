#-----------------------------------------------------------------------------------------------------------------------
# C - Good Sequence
# https://atcoder.jp/contests/arc087/tasks/arc087_a
#-----------------------------------------------------------------------------------------------------------------------
#Taking the input N as the size of the list. And then taking the list input.
N = int(input())
ListA = list(map(int, input().split()))

#Creating a counter to count how many we'll have to remove.
removalCounter = 0

#Loop iteration to extract each num, check how many of this num we have, saving the count and replacing all num with -1.
#If the numCount and num are equal then ok.
#If the numCount is more than num, calculate how much we'll remove.
#If the numCount is less than num, we'll remove all of it.
for num in ListA:
    if num != -1:
        numCount = ListA.count(num)
        #print(f'{num} = {numCount} times.')

        ListA = [-1 if x == num else x for x in ListA]
        #print(ListA)

        if num < numCount:
            removalCounter += (numCount - num)
        elif num > numCount:
            removalCounter += numCount

#Printing the final removal count.
print(removalCounter)




#-----------------------------------------------------------------------------------------------------------------------
"""
#Taking the input N as the size of the list. And then taking the list input.
N = int(input())
ListA = list(map(int, input().split()))

#Creating a counter to count how many we'll have to remove.
removalCounter = 0

#Loop iteration to extract each num, check how many of this num we have, saving the count and replacing all num with -1.
#If the numCount and num are equal then ok.
#If the numCount is more than num, calculate how much we'll remove.
#If the numCount is less than num, we'll remove all of it.
for num in ListA:
    if num != -1:
        numCount = ListA.count(num)
        #print(f'{num} = {numCount} times.')

        ListA = [-1 if x == num else x for x in ListA]
        #print(ListA)

        if num < numCount:
            removalCounter += (numCount - num)
        elif num > numCount:
            removalCounter += numCount

#Printing the final removal count.
print(removalCounter)
"""