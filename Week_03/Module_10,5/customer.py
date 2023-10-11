from eshop import *
class Customer:
    customers = []
    total_customer = 0

    @staticmethod
    def register_customer(cus_name, cus_email, cus_password, initial_deposit):
        customer = {
            'cus_name': cus_name,
            'cus_email': cus_email,
            'cus_password': cus_password,
            'cus_wallet': 0 + initial_deposit
        }
        Customer.total_customer += 1
        Customer.customers.append(customer)
        EShop.customers.append(customer)
        print(f'Welcome {cus_name}, Your account is created Successfully.')


    @staticmethod
    def customer_profile(cus_email, cus_password):
        for customer in Customer.customers:
            if customer['cus_email'] == cus_email and customer['cus_password'] == cus_password:
                print('Customer Name: ', customer['cus_name'], '\nEmail: ', customer['cus_email'], '\nBalance: ', customer['cus_wallet'], '€')


    @staticmethod
    def remove_customer(cus_email, cus_password):
        cus_refund = 0
        for customer in Customer.customers:
            if customer['cus_email'] == cus_email and customer['cus_password'] == cus_password:
                cus_refund = customer['cus_wallet']
                Customer.customers.remove(customer)
                EShop.customers.remove(customer)
        print(f'Account deletion successful. You will get {cus_refund}€ refund.')
