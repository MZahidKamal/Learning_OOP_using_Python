#-----------------------------------------------------------------------------------------------------------------------
# M. Replace MinMax
# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M
#-----------------------------------------------------------------------------------------------------------------------
#Taking N input.
N = int(input())

#Creating a list, and then taking inputs into it.
list_A = list(map(int, input().split()))

#Saving max and min elements of the list.
max_value = max(list_A)
min_value = min(list_A)

#Finding the index of max and min from the liat.
max_index = -1
min_index = -1

for i in range(N):
    if list_A[i] == max_value:
        max_index = i
    if list_A[i] == min_value:
        min_index = i

#Swaping the max and min elements.
list_A[max_index], list_A[min_index] = list_A[min_index], list_A[max_index]

#Printing the modified list.
for x in list_A:
    print(x, end=" ")
