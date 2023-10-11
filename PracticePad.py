from eshop import *


class Customer:
    customers = []
    total_customer = 0

    @staticmethod
    def register_customer(cus_name, cus_email, cus_password, initial_deposit):
        customer = (cus_name, cus_email, cus_password, initial_deposit)

        Customer.total_customer += 1
        Customer.customers.append(customer)
        EShop.customers.append(customer)
        print(f'Welcome {cus_name}, Your account is created Successfully.')

    @staticmethod
    def remove_customer(cus_email, cus_password):
        refund = 0
        for customer in Customer.customers:
            if customer[1] == cus_email and customer[2] == cus_password:
                refund = Customer.customers[3]
                Customer.customers.remove(customer)
        print(f'Account deletion successful. You will get {refund}€ refund.')
