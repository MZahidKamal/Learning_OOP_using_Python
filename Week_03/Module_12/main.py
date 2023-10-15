from bank import Bank
from savings_account import SavingsAccount
from current_account import CurrentAccount
import sys

def main():
    commerzbank = Bank('CommerzBank', 'Wellknown Street', 55, 46589, 'Frankfurt', 'Hessen', 'Germany', 'www.commerzbank.de')


#---Some dummy data for test purposes-----------------------------------------------------------------------------------
    SavingsAccount('Robert Bosch', '15.12.1980', 'Ring Road', 41, 15783, 'Offenbach', 'robert@bosch.com')
    SavingsAccount('Alice Johnson', '05.07.1992', 'Oak Street', 123, 54321, 'Springfield', 'alice@example.com')
    SavingsAccount('Bob Smith', '12.03.1985', 'Maple Avenue', 456, 98765, 'Pleasant ville', 'bob@example.com')
    SavingsAccount('Eva Davis', '20.09.1978', 'Elm Road', 789, 24680, 'Sunset City', 'eva@example.com')
    SavingsAccount('David Wilson', '15.11.1987', 'Cedar Lane', 555, 11111, 'Bayside', 'david@example.com')
    SavingsAccount('Sophia Lee', '30.04.1995', 'Pine Street', 777, 33333, 'Hometown', 'sophia@example.com')

    CurrentAccount('John Doe', '10.08.1980', 'Elm Street', 123, 45678, 'Springfield', 'john@example.com')
    CurrentAccount('Jane Smith', '25.05.1990', 'Oak Avenue', 456, 98765, 'Pleasant ville', 'jane@example.com')
    CurrentAccount('Michael Johnson', '15.02.1975', 'Maple Road', 789, 12345, 'Sunset City', 'michael@example.com')
    CurrentAccount('Lisa Williams', '03.12.1989', 'Cedar Lane', 555, 22222, 'Bayside', 'lisa@example.com')
    CurrentAccount('Daniel Brown', '20.06.1982', 'Pine Street', 777, 33333, 'Hometown', 'daniel@example.com')
    CurrentAccount('Sarah Davis', '15.11.1977', 'Willow Lane', 321, 54321, 'Riverdale', 'sarah@example.com')
#-----------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------R E P L I C A  S Y S T E M---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

    print(f'\n---------- Welcome to {commerzbank.Name} ----------')
    while True:

        print('\nSelect Option:'
              '\n\t[1] Show Bank Information'
              '\n\t[2] Admin/Manager Login'
              '\n\t[3] User/Account Holder Login'
              '\n\t[4] Log out')

        user_input = int(input('Your selection: '))

#-----------------------------------------------------------------------------------------------------------------------

        if user_input == 1:
            commerzbank.bank_info()
            continue

#-----------------------------------------------------------------------------------------------------------------------

        elif user_input == 2:
            print('\n----- Admin/Managerial access given -----')
            while True:
                print('\nSelect Option:'
                      '\n\t[1] Create Savings Account'
                      '\n\t[2] Create Current Account'
                      '\n\t[3] Delete Account'
                      '\n\t[4] Show All User Account List'
                      '\n\t[5] Show Bank Volt Balance'
                      '\n\t[6] Show Bank Loan Balance'
                      '\n\t[7] NO/OFF Loan Feature'
                      '\n\t[8] Declare Bankrupt'
                      '\n\t[9] Sign out')

                user_input = int(input('Your selection: '))

                if user_input == 1:
                    name = input('Enter your name: ')
                    dob = input('Date of Birth: ')
                    road = input('Road: ')
                    house_no = input('House No: ')
                    zip_code = input('ZIP Code: ')
                    city = input('City: ')
                    email = input('Email: ')
                    SavingsAccount(name, dob, road, house_no, zip_code, city, email)

                elif user_input == 2:
                    name = input('Enter your name: ')
                    dob = input('Date of Birth: ')
                    road = input('Road: ')
                    house_no = input('House No: ')
                    zip_code = input('ZIP Code: ')
                    city = input('City: ')
                    email = input('Email: ')
                    CurrentAccount(name, dob, road, house_no, zip_code, city, email)

                elif user_input == 3:
                    account_number = input('Enter your account number: ')
                    commerzbank.delete_account(account_number)

                elif user_input == 4:
                    commerzbank.show_all_account_info()

                elif user_input == 5:
                    commerzbank.show_bank_volt_balance()

                elif user_input == 6:
                    commerzbank.show_total_bank_loan_amount()

                elif user_input == 7:
                    print('\nSelect Option:'
                          '\n\t[1] Turn ON Loan Feature'
                          '\n\t[2] Turn OFF Loan Feature')
                    user_input = int(input('Your selection: '))
                    if user_input == 1:
                        commerzbank.loan_feature_controller('ON')
                    elif user_input == 2:
                        commerzbank.loan_feature_controller('OFF')
                    else:
                        print('Invalid Option Selected.')

                elif user_input == 8:
                    commerzbank.declare_bankruptcy()

                elif user_input == 9:
                    print('Logged out from Admin/Managerial access.')
                    break

                else:
                    print('Invalid Option Selected.')
                    continue

#-----------------------------------------------------------------------------------------------------------------------

        elif user_input == 3:
            print('\n----- User/Account Holder access given -----')
            while True:
                print('\nSelect Option:'
                      '\n\t[1] Create Account'
                      '\n\t[2] Show Available Balance'
                      '\n\t[3] Deposit Money'
                      '\n\t[4] Withdraw Money'
                      '\n\t[5] Transfer Money'
                      '\n\t[6] Apply for Loan'
                      '\n\t[7] Show Loan Balance'
                      '\n\t[8] Show Transaction History'
                      '\n\t[9] Sign out')

                user_input = int(input('Your selection: '))

                if user_input == 1:
                    while True:
                        print('\nAccount Type:'
                              '\n\t[1] Savings Account'
                              '\n\t[2] Current Account')

                        user_input = int(input('Your selection: '))

                        if user_input == 1:
                            name = input('Enter your name: ')
                            dob = input('Date of Birth: ')
                            road = input('Road: ')
                            house_no = input('House No: ')
                            zip_code = input('ZIP Code: ')
                            city = input('City: ')
                            email = input('Email: ')
                            SavingsAccount(name, dob, road, house_no, zip_code, city, email)
                            break

                        elif user_input == 2:
                            name = input('Enter your name: ')
                            dob = input('Date of Birth: ')
                            road = input('Road: ')
                            house_no = input('House No: ')
                            zip_code = input('ZIP Code: ')
                            city = input('City: ')
                            email = input('Email: ')
                            CurrentAccount(name, dob, road, house_no, zip_code, city, email)
                            break

                        else:
                            print('Invalid Option Selected.')
                            continue

                elif user_input == 2:
                    account_number = input('Enter your account number: ')
                    for account in commerzbank.AllAccounts:
                        if account['AccountNumber'] == account_number:
                            print('Currently your account balance is', account['CurrentBalance'], '€')

                elif user_input == 3:
                    account_number = input('Enter your account number: ')
                    deposit_amount = int(input('How much you want to deposit: '))

                    if account_number[:2] == 'SV':
                        SavingsAccount.deposit_money(account_number, deposit_amount)
                    elif account_number[:2] == 'CR':
                        CurrentAccount.deposit_money(account_number, deposit_amount)
                    else:
                        print(f'Invalid account number.')

                elif user_input == 4:
                    account_number = input('Enter your account number: ')
                    desire_amount = int(input('How much you want to withdraw: '))

                    if account_number[:2] == 'SV':
                        SavingsAccount.withdraw_money(account_number, desire_amount)
                    elif account_number[:2] == 'CR':
                        CurrentAccount.withdraw_money(account_number, desire_amount)
                    else:
                        print(f'Invalid account number.')

                elif user_input == 5:
                    your_account_number = input('Enter your account number: ')
                    target_account_number = input('Enter beneficiary account number: ')
                    transfer_amount = int(input('How much you want to transfer: '))

                    if your_account_number[:2] == 'SV':
                        SavingsAccount.transfer_money(your_account_number, target_account_number, transfer_amount)
                    elif your_account_number[:2] == 'CR':
                        CurrentAccount.transfer_money(your_account_number, target_account_number, transfer_amount)
                    else:
                        print(f'Invalid account number.')

                elif user_input == 6:
                    account_number = input('Enter your account number: ')
                    loan_amount = int(input('How much you want to loan: '))

                    if account_number[:2] == 'SV':
                        print('Loan feature is only available for Current accounts.')
                    elif account_number[:2] == 'CR':
                        CurrentAccount.apply_loan(account_number, loan_amount)
                    else:
                        print(f'Invalid account number.')

                elif user_input == 7:
                    account_number = input('Enter your account number: ')
                    if account_number[:2] == 'SV':
                        print('Loan feature is only available for Current accounts.')
                    elif account_number[:2] == 'CR':
                        account_exists = False
                        for account in commerzbank.AllCurrentAccounts:
                            if account['AccountNumber'] == account_number:
                                account_exists = True
                                print('Currently total loan taken under your account is', account['LoanTaken'], '€')
                                continue
                        if not account_exists:
                            print(f'Account {account_number} does not exist.')
                    else:
                        print(f'Invalid account number.')

                elif user_input == 8:
                    account_number = input('Enter your account number: ')
                    if account_number[:2] == 'SV':
                        SavingsAccount.TransactionHistory(account_number)
                    elif account_number[:2] == 'CR':
                        CurrentAccount.TransactionHistory(account_number)
                    else:
                        print(f'Invalid account number.')

                elif user_input == 9:
                    print('Logged out from User/Account Holder access.')
                    break
                else:
                    print('Invalid Option Selected.')
                    continue

#-----------------------------------------------------------------------------------------------------------------------

        elif user_input == 4:
            print('Logged out from Total System.')
            sys.exit()

#-----------------------------------------------------------------------------------------------------------------------

        else:
            print('Invalid Option Selected.')
            continue

#-----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
