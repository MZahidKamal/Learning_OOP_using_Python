#-----------------------------------------------------------------------------------------------------------------------
# Q. Digits
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q
#-----------------------------------------------------------------------------------------------------------------------
#Taking input of test cases.
test_cases = int(input())

#Loop iteration for all test cases.
for test in range(test_cases):

    #Taking input, but as string.
    number_string = input()

    #Creating an empty list to save numbers after extracting from the string.
    number_list = []

    #Extracting numerical digits from the string and saving into the list.
    for digit in number_string:
        number_list.append(digit)

    #Reversing the list.
    number_list.reverse()

    #Printing the final output.
    for number in number_list:
        print(number, end=" ")

    #New line after printing each output.
    print()
