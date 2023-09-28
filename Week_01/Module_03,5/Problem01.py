#-----------------------------------------------------------------------------------------------------------------------
# G. Palindrome Array
# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G
#-----------------------------------------------------------------------------------------------------------------------
#Taking N input.
N = int(input())

#Creating a list, and then taking inputs into it.
list_A = list(map(int, input().split()))

#Create a copy of the main list, and then reverse it.
list_R = list_A.copy()
list_R.reverse()

#Now doing the comparison and printing the final output.
if list_A == list_R:
    print('YES')
else:
    print('NO')
