#-----------------------------------------------------------------------------------------------------------------------
# 5.6 Shopping checkout and price calculations
#-----------------------------------------------------------------------------------------------------------------------
#Creating a class with instance attributes.
class Shop:

    #Creating the constructor of the class.
    def __init__(self, buyer_name):
        self.buyer_name = buyer_name
        self.cart = []

    #Creating a function/method under the class.
    def add_to_cart(self, name, price, quantity):
        product = {'name': name, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def remove_from_cart(self, name, remove_quantity):
        for item in self.cart:
            if name == item['name']:
                if remove_quantity == item['quantity']:
                    self.cart.remove(item)
                    print(f'{name} is removed successfully.')
                elif remove_quantity < item['quantity']:
                    item['quantity'] -= remove_quantity
                    print(f'{name} {remove_quantity} pieces removed successfully.')

    def total_checkout_price(self):
        total_price = 0
        for each_item in self.cart:
            total_price += (each_item['price'] * each_item['quantity'])
        print(f'Total price including VAT is {total_price} Euro.')

    def checkout(self, given_cash):
        total_price = 0
        for each_item in self.cart:
            total_price += (each_item['price'] * each_item['quantity'])
        if given_cash < total_price:
            print(f'Total price is {total_price} Euro. Therefore you have to pay {total_price - given_cash} Euro more.')
        elif given_cash > total_price:
            print(f'Successfully paid {total_price} Euro. Here is your return {given_cash - total_price} Euro.')
        else:
            print(f'Successfully paid {total_price} Euro.')


#Creating an object of the class, using the constructor.
tisha = Shop('Tisha')

#Calling add_to_cart function, and buying 2 items.
tisha.add_to_cart('shoe', 1200, 2)
tisha.add_to_cart('phone', 899, 2)
tisha.add_to_cart('dress', 65, 2)

#Printing the cart of Mehjabeen and see the items in the cart.
for item in tisha.cart:
    print(item)

tisha.total_checkout_price()
print()

tisha.remove_from_cart('phone', 1)

for item in tisha.cart:
    print(item)

tisha.total_checkout_price()
print()

tisha.checkout(4000)
