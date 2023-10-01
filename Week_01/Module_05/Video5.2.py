#-----------------------------------------------------------------------------------------------------------------------
# 5.2 Creating and Using Methods
#-----------------------------------------------------------------------------------------------------------------------

#Simple function can be written in this way.
def call():
    print('Calling Someone Global')
    return 'Call done Global.'
#But if we write the same code in the class, it'll work as method of the class.

#-----------------------------------------------------------------------------------------------------------------------

#Creating a user defined class with some attributes. And initializing some values in it.
class Phone:
    Brand = 'Samsung'
    Model = 'A71'
    ReleaseYear = 2022
    Price = 350
    Features = ['Call', 'Message', 'Camera', 'Browsing', 'Calculator']

    #Creating a method under the class.
    def call(self, phone_number):
        status = f'Calling {phone_number} to Someone from My Phone.'
        return status

    #Creating another method under the class.
    def message(self, phone_number, text):
        status = f'Texting "{text}" to {phone_number} to Someone from My Phone.'
        return status


#Creating an object of that class. And printing the object.
myPhone = Phone()

#If we write [objectName.] then the attributes will show up. Let's print the object attributes together.
print(myPhone.Brand, myPhone.Model, myPhone.ReleaseYear, myPhone.Price, myPhone.Features)

#If we write [objectName.] then beside the attributes, the [method] will also show up. Let's call the methods.
callStatus = myPhone.call(+49123456789)
print(callStatus)

messageStatus = myPhone.message(+49123456789, 'Dont be late, meeting will start soon.')
print(messageStatus)
print()
print()

#-----------------------------------------------------------------------------------------------------------------------

#Creating another user defined class. And initializing some values in it.
class Calculator:
    Brand = 'Casio MS990'
    Features = ['Add', 'Subtract', 'Multiply', 'Division']

    #Creating some methods under the class.
    def add(self, num1, num2):
        return f'Sum of {num1} and {num2} = {num1+num2}'

    def subtract(self, num1, num2):
        return f'Subtract of {num1} and {num2} = {num1 - num2}'

    def multiply(self, num1, num2):
        return f'Multiple of {num1} and {num2} = {num1 * num2}'

    def divide(self, num1, num2):
        return f'Division of {num1} and {num2} = {num1 / num2}'


#Creating an object of that class. And printing the object.
myCalculator = Calculator()
print(myCalculator.Brand, myCalculator.Features)

addStatus = myCalculator.add(22, 33)
subtractStatus = myCalculator.subtract(22, 33)
multiplyStatus = myCalculator.multiply(22, 33)
divideStatus = myCalculator.divide(22, 33)

print(addStatus)
print(subtractStatus)
print(multiplyStatus)
print(divideStatus)

#-----------------------------------------------------------------------------------------------------------------------
