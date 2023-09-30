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


#-----------------------------------------------------------------------------------------------------------------------
"""
//Three numbers

Read two integers, start and end, from the input.

Initialize a variable counter to 0. This variable will be used to count the valid triplets.

Use two nested loops to iterate through all possible values of x and y from 0 to start.

For each combination of x and y, calculate the value of z using the condition end - x - y.

Check if the value of z is non-negative (i.e., 0 <= z) and if it is less than or equal to start. If both conditions are satisfied, increment the counter by 1.

Continue iterating through all possible combinations of x and y.

After both loops complete, counter will contain the count of valid triplets.

Print the value of counter.
"""
#-----------------------------------------------------------------------------------------------------------------------
