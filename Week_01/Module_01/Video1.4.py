#-----------------------------------------------------------------------------------------------------------------------
# 1.4 Basic Input and Output and Typecasting in python
#-----------------------------------------------------------------------------------------------------------------------
# Taking input.
# print("Product price?")
# input()
# input("Discounted Product price: ")

# Taking input and saving into a variable.
# penPrice = input("What is the price of this pen? ")
# print(penPrice)

# Printing it again using f-String.
# print(f"The price of the pen is {penPrice}, and it's fixed.")
#-----------------------------------------------------------------------------------------------------------------------
# Again taking input, saving into a variable, and then print it.
# penPrice = input("The price of the pen is: ")
# paperPrice = input("The price of the paper is: ")

# print(penPrice, paperPrice)
# print("The prices of the pen and paper are respectively ", penPrice, paperPrice)

# Now adding the prices and printing the total price.
# totalPrice = penPrice + paperPrice
# print("The total price of the pen and paper is ", totalPrice)

# Here is a problem!! If we say the penPrice is 20 and the paperPrice is 10, then the total price will be printed 2010.
# Why? Because Python TAKE INPUTS only as string data type by default. So it's actually concatenating 20 and 10.

# Let's check it.
# print(type(totalPrice))

# To get the mathematical summation we'll convert the prices into int data type. This is called type casting.
# To Learn more, visit (https://www.geeksforgeeks.org/type-casting-in-python/).
#-----------------------------------------------------------------------------------------------------------------------
# Again taking input, saving into a variable, convert them into int data type, sum them and then print.
# penPrice = input("The price of the pen is: ")
# penPrice_int = int(penPrice)

# paperPrice = input("The price of the paper is: ")
# paperPrice_int = int(paperPrice)

# Now adding the prices mathematically and printing the total price.
# totalPrice_int = penPrice_int + paperPrice_int
# print("The total price of the pen and paper is ", totalPrice_int)
#-----------------------------------------------------------------------------------------------------------------------
# Let's do the exact same thing again, but this time, taking int input directly.
penPrice_int = int(input("The price of the pen is: "))
paperPrice_int = int(input("The price of the paper is: "))

# Now adding the prices and printing the total price.
totalPrice = penPrice_int + paperPrice_int
print("The total price of the pen and paper is", totalPrice)

# To Learn more, visit (https://www.geeksforgeeks.org/how-to-convert-data-types-in-python-3/).
#-----------------------------------------------------------------------------------------------------------------------
