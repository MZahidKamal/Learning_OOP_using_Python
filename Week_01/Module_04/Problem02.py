#-----------------------------------------------------------------------------------------------------------------------
# C - Good Sequence
# https://atcoder.jp/contests/arc087/tasks/arc087_a
#-----------------------------------------------------------------------------------------------------------------------
#Taking the input N as the size of the list. And then taking the list input.
N = int(input())
ListA = list(map(int, input().split()))

#Creating a dictionary, where list elements will be the keys and values will initially be 0.
#This dictionary will already remove the duplicates.
elementWithCountDict = {key: 0 for key in ListA}

#Creating a counter to count how many we'll have to remove.
removalCounter = 0

#We'll extract each key from the dict, will count its presence in the list, and will save the count as the value.
for key, value in elementWithCountDict.items():
    numCount = ListA.count(key)
    elementWithCountDict[key] = numCount

#Loop iteration to extract each key and value from the dict.
#If the value is more than kex, calculate how much we'll remove.
#If the value is less than key, we'll remove all of it.
for key, value in elementWithCountDict.items():
    if key < value:
        removalCounter += (value - key)
    elif key > value:
        removalCounter += value

#Printing the final removal count.
print(removalCounter)

#-----------------------------------------------------------------------------------------------------------------------

"""
#Taking the input N as the size of the list. And then taking the list input.
N = int(input())
ListA = list(map(int, input().split()))

#Creating a counter to count how many we'll have to remove.
removalCounter = 0
alreadyChecked = []

#Loop iteration to extract each num, check how many of this num we have, saving the count.
#Saving the num in a list called alreadyChecked.
#If the numCount is more than num, calculate how much we'll remove.
#If the numCount is less than num, we'll remove all of it.
for num in ListA:
    if num not in alreadyChecked:

        numCount = ListA.count(num)
        alreadyChecked.append(num)

        if num < numCount:
            removalCounter += (numCount - num)
        elif num > numCount:
            removalCounter += numCount


#Printing the final removal count.
print(removalCounter)
"""

# TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE

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

# TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE



# https://ideone.com/gIC5Ic
# //good sequence
#
# Read an integer N from the input, representing the number of elements in the list.
# Read a list of N integers, nums, from the input.
# Initialize an empty dictionary mp to store the frequency of each unique number in nums.
# Iterate through each number num in nums:
# If num is already a key in the dictionary mp, increment its corresponding value by 1.
# If num is not a key in the dictionary mp, add it as a key with a value of 1.
# Initialize a variable sum to 0 to store the final result.
# Iterate through the key-value pairs in the dictionary mp:
# For each key-value pair (key, value):
# If value is less than key, add value to the sum.
# If value is greater than key, add (value - key) to the sum.
# Print the value of sum, which represents the sum of differences between the frequency of each number
# and the number itself.
