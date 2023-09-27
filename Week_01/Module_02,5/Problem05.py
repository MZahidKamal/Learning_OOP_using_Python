#-----------------------------------------------------------------------------------------------------------------------
# Z. Three Numbers
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Z
#-----------------------------------------------------------------------------------------------------------------------
#Taking inputs, splitting and saving them into two variables and converting into list.
K, S = list(map(int, input().split()))

#Creating a counter variable.
count = 0

#Nested loop, to iterate through each possible values of X, Y and Z.
#Then sum them up and see if is equal to S or not. If yes then increase the counter.
for X in range(K+1):
    for Y in range(K+1):
        for Z in range(K+1):
            if X + Y + Z == S:
                count = count + 1

#Printing the final output.
print(count)

# TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE TLE
