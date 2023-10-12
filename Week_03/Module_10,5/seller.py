from eshop import EShop
#from product import Product

class Seller:
    sellers = []
    total_seller = 0

    @staticmethod
    def register_seller(sel_name, sel_email, sel_password, sel_tin, initial_deposit):
        seller = {
            'sel_name': sel_name,
            'sel_email': sel_email,
            'sel_password': sel_password,
            'sel_tin': sel_tin,
            'sel_wallet': 0 + initial_deposit
        }
        Seller.total_seller += 1
        Seller.sellers.append(seller)
        EShop.sellers.append(seller)
        print(f'Welcome {sel_name}, Your seller account is created Successfully.')

    @staticmethod
    def seller_profile(sel_email, sel_password):
        for seller in Seller.sellers:
            if seller['sel_email'] == sel_email and seller['sel_password'] == sel_password:
                print('Seller Name: ', seller['sel_name'], '\nEmail: ', seller['sel_email'], '\nBalance: ',
                      seller['sel_wallet'], '€')


    # def upload_sel_product(self, sel_email, sel_password, pro_name, pro_price, pro_description, pro_stock_quantity):
    #     for seller in Seller.sellers:
    #         if seller['sel_email'] == sel_email and seller['sel_password'] == sel_password:
    #             Product.upload_product(sel_email, sel_password, pro_name, pro_price, pro_description, pro_stock_quantity)

    @staticmethod
    def remove_seller(sel_email, sel_password):
        sel_refund = 0
        for seller in Seller.sellers:
            if seller['sel_email'] == sel_email and seller['sel_password'] == sel_password:
                sel_refund = seller['sel_wallet']
                Seller.sellers.remove(seller)
                EShop.sellers.remove(seller)
        print(f'Account deletion successful. You will get {sel_refund}€ refund.')
