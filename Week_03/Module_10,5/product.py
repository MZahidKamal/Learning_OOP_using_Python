from eshop import EShop
from seller import Seller


class Product(Seller):
    products = []
    total_product = 0

    @staticmethod
    def upload_product(sel_email, sel_password, pro_name, pro_price, pro_description, pro_stock_quantity):
        for seller in Seller.sellers:
            if seller['sel_email'] == sel_email and seller['sel_password'] == sel_password:
                product = {
                    'sel_email': sel_email,
                    'pro_name': pro_name,
                    'pro_price': pro_price,
                    'pro_description': pro_description,
                    'pro_stock_quantity': pro_stock_quantity
                }
                Product.total_product += 1
                Product.products.append(product)
                EShop.products.append(product)
                print(pro_name, 'is added successfully in', seller['sel_name'], 's stock.')

    @staticmethod
    def product_detail(pro_name):
        for product in Product.products:
            if product['pro_name'] == pro_name:
                print('Product Name: ', product['pro_name'], '\nDescription: ', product['pro_description'], '\nPrice: ',
                      product['pro_price'], '€')


    @staticmethod
    def remove_product(sel_email, sel_password, pro_name):
        for seller in Seller.sellers:
            if seller['sel_email'] == sel_email and seller['sel_password'] == sel_password:
                for product in Product.products:
                    if product['pro_name'] == pro_name:
                        Product.total_product -= 1
                        Product.products.remove(product)
                        EShop.products.remove(product)
                        print(pro_name, 'is removed successfully from', seller['sel_name'], 's stock.')
