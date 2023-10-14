from bank import Bank
from savings_account import SavingsAccount
from current_account import CurrentAccount
import sys

def main():
    commerzbank = Bank('CommerzBank', 'Wellknown Street', 55, 46589, 'Frankfurt', 'Hessen', 'Germany', 'www.commerzbank.de')
    print(f'\n---------- Welcome to {commerzbank.Name} ----------')
    while True:

        print('Select Option:'
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
            print('Select Option:'
                  '\n\t[1] Create Account'
                  '\n\t[2] Delete Account'
                  '\n\t[3] Show All User Account List'
                  '\n\t[4] Show Bank Volt Balance'
                  '\n\t[5] Show Bank Loan Balance'
                  '\n\t[6] Declare Bankrupt'
                  '\n\t[7] Sign out')
#-----------------------------------------------------------------------------------------------------------------------
        elif user_input == 3:
            print('\n----- User/Account Holder access given -----')
            print('Select Option:'
                  '\n\t[1] Create Account'
                  '\n\t[2] Delete Account'
                  '\n\t[3] Show All User Account List'
                  '\n\t[4] Show Bank Volt Balance'
                  '\n\t[5] Show Bank Loan Balance'
                  '\n\t[6] Declare Bankrupt'
                  '\n\t[7] Sign out')

        elif user_input == 4:
            print('Logged out from Admin/Managerial access.')
            sys.exit()

        else:
            print('Invalid OptionSelected.')
            continue


if __name__ == '__main__':
    main()
