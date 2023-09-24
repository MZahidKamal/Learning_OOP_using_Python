#-----------------------------------------------------------------------------------------------------------------------
# 1.9 Module Summary
#-----------------------------------------------------------------------------------------------------------------------
# HW: Take 3 numbers from the user and give me the largest number as output.
# HW: Take 3 numbers from the user and give me the summ of all numbers as output.
#-----------------------------------------------------------------------------------------------------------------------
# a = int(input("Give me a random number: "))
# b = int(input("Give me another random number: "))
# c = int(input("Give me a last random number: "))
#
# if a > b and a > c:
#     print(a, "is the largest number.")
# elif b > a and b > c:
#     print(b, "is the largest number.")
# else:
#     print(c, "is the largest number.")
#
# summ = a + b + c
# print(f"And sum of the all three numbers is {summ}.")
#-----------------------------------------------------------------------------------------------------------------------
# HW: Run a loop and show me the odd numbers between 39 and 68.
# for oddNumbers in range(39, 69, 2):
#     print(oddNumbers)
#-----------------------------------------------------------------------------------------------------------------------
# HW: Grade calculator in Python. (https://en.wikipedia.org/wiki/Academic_grading_in_Bangladesh)

totalMark = int(input("Give me the number you scored in your exam: "))

if 80 <= totalMark & totalMark <= 100:
    print("Your Letter Grade is A+, Grade Point is 4.00")

elif 75 <= totalMark & totalMark <= 79:
    print("Your Letter Grade is A, Grade Point is 3.75")

elif 70 <= totalMark & totalMark <= 74:
    print("Your Letter Grade is A-, Grade Point is 3.50")

elif 65 <= totalMark & totalMark <= 69:
    print("Your Letter Grade is B+, Grade Point is 3.25")

elif 60 <= totalMark & totalMark <= 64:
    print("Your Letter Grade is B, Grade Point is 3.00")

elif 55 <= totalMark & totalMark <= 59:
    print("Your Letter Grade is B-, Grade Point is 2.75")

elif 50 <= totalMark & totalMark <= 54:
    print("Your Letter Grade is C+, Grade Point is 2.50")

elif 45 <= totalMark & totalMark <= 49:
    print("Your Letter Grade is C, Grade Point is 2.25")

elif 40 <= totalMark & totalMark <= 44:
    print("Your Letter Grade is D, Grade Point is 2.00")

elif 0 <= totalMark & totalMark <= 39:
    print("Your Letter Grade is F, Grade Point is 0.00")
#-----------------------------------------------------------------------------------------------------------------------
