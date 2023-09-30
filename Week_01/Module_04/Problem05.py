#-----------------------------------------------------------------------------------------------------------------------
# Take a number from the user and draw a pyramid using PyAutoGUI.
"""
Input: 1
Output:
#

Input: 5
Output:
#
##
###
####
#####
"""
import pyautogui

#-----------------------------------------------------------------------------------------------------------------------

#Taking the input of any random integer.
# N = int(input())

#Printing the character '#' incrementally with the value of i.
# for i in range(1, N+1):
#     print('#' * i)

#-----------------------------------------------------------------------------------------------------------------------

#Taking the input of any random integer.
N = int(input())

pyautogui.sleep(5)

#Printing the character '#' incrementally with the value of i.
for i in range(1, N+1):
    pyautogui.write('#' * i)
    pyautogui.press('enter')

#-----------------------------------------------------------------------------------------------------------------------

"""
N = int(input())
matrix2D = [[' ' for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        if i == j or i+j < N:
            matrix2D[i][j] = '#'


for i in range(N):
    for j in range(N):
        print(matrix2D[i][j], end="")
    print()
"""

#-----------------------------------------------------------------------------------------------------------------------
