#-----------------------------------------------------------------------------------------------------------------------
# Y. Range sum query
# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Y
#-----------------------------------------------------------------------------------------------------------------------
#Taking input of N and the number of test queries.
N, testQueries = list(map(int, input().split()))

input_List = list(map(int, input().split()))

#Loop iteration for all test cases.
for test in range(testQueries):
    # Taking input of left index and right index.
    L, R = list(map(int, input().split()))

    #Calculating the sum of all elements from left index to right index.
    summLR = 0
    for num in input_List[L - 1: R]:
        summLR = summLR + num

    #Printing the final summ.
    print(summLR)

# TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE
