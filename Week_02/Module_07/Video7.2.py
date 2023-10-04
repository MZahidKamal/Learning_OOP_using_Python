#-----------------------------------------------------------------------------------------------------------------------
# 7.2 static attribute, static method and class method decorator
#-----------------------------------------------------------------------------------------------------------------------
class Shopping:
    cart = []                                       # This is class attribute / static attribute
    origin = 'China'                                # This is class attribute / static attribute

    def __init__(self, name, location):
        self.name = name                            # This is instance attribute
        self.location = location

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'Buying {item} for {price} Euro, with remaining {remaining} Euro.')

supermarket = Shopping('Rewe Supermarkt', '60439 Heddernheim')
supermarket.purchase('A4 Paper', 5, 10)
purchase('A4 Paper', 5, 10)

"""
See the purchase method, and supermarket object. The purchase method is only accessible if we create an object and then
call the method using the object, like we did here. This type of method is static method.

But if we want to access the method without creating any class, like...
purchase('A4 Paper', 5, 10)
it will show error.
"""