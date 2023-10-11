from eshop import EShop
from customer import Customer
from seller import Seller

def main():
    amazon = EShop('Amazon Inc.', 'Wellknown Street', 55, '78980', 'Frankfurt', 'Hessen', 'Germany', '189746TIN4500')
    print()
    amazon.shop_info()

    print()
    Customer.register_customer('Hasib Hossain', 'hasib@email.com', '1346987pass$', 5000)
    print(len(Customer.customers))

    print()
    Customer.customer_profile('hasib@email.com', '1346987pass$')

    print()
    Customer.remove_customer('hasib@email.com', '1346987pass$')
    print(len(Customer.customers))

    print()
    Seller.register_seller('Hasib Hossain', 'hasib@email.com', '1346987pass$', '546546TIN54654', 8000)
    print(len(Seller.sellers))

    print()
    Seller.seller_profile('hasib@email.com', '1346987pass$')



if __name__ == '__main__':
    main()
