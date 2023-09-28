#-----------------------------------------------------------------------------------------------------------------------
# S. Max Split
# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S
#-----------------------------------------------------------------------------------------------------------------------
#Taking the balanced string directly.
InputString = input()

#Creating necessary variable, list and a counter.
BalancedString = ""
BalancedStringList = []
BalancedStringCounter = 0

#Extracting each char from the InputString, adding it into a BalancedString and check if it's balanced or not.
#If balanced, saving the BalancedString into a list and increase the counter.
for char in InputString:
    BalancedString += char

    countL = BalancedString.count('L')
    countR = BalancedString.count('R')

    if countL == countR:
        BalancedStringCounter += 1
        BalancedStringList.append(BalancedString)
        BalancedString = ""

#Printing the final output.
print(BalancedStringCounter)
for word in BalancedStringList:
    print(word)
