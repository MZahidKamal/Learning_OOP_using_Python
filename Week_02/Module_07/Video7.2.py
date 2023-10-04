#-----------------------------------------------------------------------------------------------------------------------
# 7.2 static attribute, static method and class method decorator
#-----------------------------------------------------------------------------------------------------------------------
class Shopping:
    cart = []                                       # This is class attribute / static attribute
    origin = 'China'                                # This is class attribute / static attribute

    def __init__(self, name, location):
        self.name = name                            # This is instance attribute
        self.location = location

    @classmethod
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Buying {item} for {price} Euro, with remaining {remaining} Euro.')

    @staticmethod
    def multiple(a, b):
        print(a*b)


supermarket = Shopping('Rewe Supermarkt', '60439 Heddernheim')
supermarket.purchase('A4 Paper', 5, 10)
Shopping.purchase('A4 Paper', 5, 10)

Shopping.multiple(4, 6)
supermarket.multiple(4, 6)

"""
See the purchase method, and supermarket object. The purchase method is only accessible if we create an object and then
call the method using the object, like we did here. This type of method is static method.

But if we want to access the method, from the class level, without creating any object, like...
Shopping.purchase('A4 Paper', 5, 10)
it will show error.

But if we add [@classmethod] just above the method snippet, then this method will also be accessible from the class
level. It will not show any error. And must not, but in that case, instead of self, cls can be used.

Let's see another method [multiple]. If we write [@staticmethod], just above the snippet, then this method will also
be accessible from the class level and as well as from the instance level. And we must not use the self in this method.

#To Learn more, visit (https://www.geeksforgeeks.org/class-method-vs-static-method-python/).
#To Learn more, visit (https://www.tutorialspoint.com/class-method-vs-static-method-in-python).
"""
#-----------------------------------------------------------------------------------------------------------------------
