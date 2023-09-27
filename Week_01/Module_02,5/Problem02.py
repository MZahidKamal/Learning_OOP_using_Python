#-----------------------------------------------------------------------------------------------------------------------
# S. Sum of Consecutive Odd Numbers
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/S
#-----------------------------------------------------------------------------------------------------------------------
#Taking input of test cases.
test_cases = int(input())

#Loop iteration for all test cases.
for test in range(test_cases):

    #Taking inputs and saving them into a list. Then sorting the list.
    input_list = list(map(int, input().split()))
    input_list.sort()

    #Now finding ranging elements excluding the beginning and ending of the range.
    range_elements = []
    for x in range(input_list[0] + 1, input_list[1]):
        range_elements.append(x)

    #Finding the odd numbers from the ranging elements, and then calculating the summ.
    summ = 0
    for x in range_elements:
        if x % 2 != 0:
            summ = summ + x

    #Printing the final output.
    print(summ)
