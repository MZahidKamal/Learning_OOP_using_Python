from bank import Bank
from savings_account import SavingsAccount

def main():
    commerzbank = Bank('CommerzBank', 'Wellknown Street', 55, 46589, 'Frankfurt', 'Hessen', 'Germany', 'www.commerzbank.de')
    commerzbank.bank_info()
    #commerzbank.declare_bankrupt()

    SavingsAccount('Robert Bosch', '15.12.1980', 'Ring Road', 41, 15783, 'Offenbach', 'robert@bosch.com')
    SavingsAccount('Alice Johnson', '05.07.1992', 'Oak Street', 123, 54321, 'Springfield', 'alice@example.com')
    SavingsAccount('Bob Smith', '12.03.1985', 'Maple Avenue', 456, 98765, 'Pleasant ville', 'bob@example.com')
    SavingsAccount('Eva Davis', '20.09.1978', 'Elm Road', 789, 24680, 'Sunset City', 'eva@example.com')
    SavingsAccount('David Wilson', '15.11.1987', 'Cedar Lane', 555, 11111, 'Bayside', 'david@example.com')
    SavingsAccount('Sophia Lee', '30.04.1995', 'Pine Street', 777, 33333, 'Hometown', 'sophia@example.com')


if __name__ == '__main__':
    main()
