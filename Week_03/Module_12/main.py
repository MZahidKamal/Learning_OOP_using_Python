from bank import Bank
from savings_account import SavingsAccount
from current_account import CurrentAccount
import sys

def main():
    commerzbank = Bank('CommerzBank', 'Wellknown Street', 55, 46589, 'Frankfurt', 'Hessen', 'Germany', 'www.commerzbank.de')
    print(f'\n---------- Welcome to {commerzbank.Name} ----------')
    while True:

        print('\nSelect Option:'
              '\n\t[1] Show Bank Information'
              '\n\t[2] Admin/Manager Login'
              '\n\t[3] User/Account Holder Login'
              '\n\t[4] Log out')

        user_input = int(input('Your selection: '))
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
                      '\n\t[7] Declare Bankrupt'
                      '\n\t[8] Sign out')

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
                    print('Delete Action Function need to be developed.')

                elif user_input == 4:
                    print('Show All User Account List Function need to be developed.')

                elif user_input == 5:
                    print('Show Bank Volt Balance Function need to be developed.')

                elif user_input == 6:
                    print('Show Bank Loan Balance Function need to be developed.')

                elif user_input == 7:
                    commerzbank.declare_bankrupt()

                elif user_input == 8:
                    print('Logged out from Admin/Managerial access.')

                else:
                    print('Invalid Option Selected.')
                    continue

#-----------------------------------------------------------------------------------------------------------------------
        elif user_input == 3:
            print('\n----- User/Account Holder access given -----')
            print('\nSelect Option:'
                  '\n\t[1] Create Account'
                  '\n\t[2] Delete Account'
                  '\n\t[3] Show All User Account List'
                  '\n\t[4] Show Bank Volt Balance'
                  '\n\t[5] Show Bank Loan Balance'
                  '\n\t[6] Declare Bankrupt'
                  '\n\t[7] Sign out')

        elif user_input == 4:
            print('Logged out from Total System.')
            sys.exit()

        else:
            print('Invalid Option Selected.')
            continue


if __name__ == '__main__':
    main()
