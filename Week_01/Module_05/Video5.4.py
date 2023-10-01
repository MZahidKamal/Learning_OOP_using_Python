#-----------------------------------------------------------------------------------------------------------------------
# 5.4 Class Attributes vs instance attributes
#-----------------------------------------------------------------------------------------------------------------------
#Creating a class with class attributes.
class Shop:
    cart = []

    #Creating the constructor of the class.
    def __init__(self, buyer_name):
        self.buyer_name = buyer_name

    #Creating a function/method under the class.
    def add_to_cart(self, item_name):
        self.cart.append(item_name)

#Creating an object of the class, using the constructor.
Mehjabeen = Shop('Mehjabeen')

#Calling add_to_cart function, and buying 2 items.
Mehjabeen.add_to_cart('shoes')
Mehjabeen.add_to_cart('phone')

#Printing the cart of Mehjabeen and see the items in the cart.
print(Mehjabeen.cart)

#Creating another object of the class, using the constructor.
Nisho = Shop('Nisho')

#Calling add_to_cart function, and buying 2 items.
Nisho.add_to_cart('sunglass')
Nisho.add_to_cart('laptop')

#Printing the cart of Mehjabeen and see the items in the cart.
print(Nisho.cart)

#-----------------------------------------------------------------------------------------------------------------------
"""
See the output of the above code.

['shoes', 'phone']
['shoes', 'phone', 'sunglass', 'laptop']

Mehjabeen has purchased shoes and phone. But these two items are also available in the cart of Nisho.

Actually the thing is, cart is a class attribute. And class attribute is shared to all instances. Therefore the cart is
same for Mehjabeen and Nisho.




"""
