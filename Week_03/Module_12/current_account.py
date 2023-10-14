import random
from bank import Bank

class CurrentAccount:
    AllCurrentAccounts = []
    MaxLoanPerAccount = 50000

    def __init__(self, name, dob, road, house_no, zip_code, city, email):
        if Bank.Banking_Service_Controller:
            self.AccountNumber = CurrentAccount.generate_current_acc_no()
            account = {
                'Name': name,
                'DateOfBirth': dob,
                'Road': road,
                'HouseNo': house_no,
                'ZIPCode': zip_code,
                'City': city,
                'Email': email,
                'AccountType': 'Current Account',
                'AccountNumber': self.AccountNumber,
                'CurrentBalance': 0,
                'LoanApplicationToBeGranted': 2,
                'MaxLoanLimit': self.MaxLoanPerAccount,
                'LoanTaken': 0
            }
            CurrentAccount.AllCurrentAccounts.append(account)
            Bank.AllAccounts.append(account)
            print(f'Successfully created account {self.AccountNumber}, for {name}.')
        else:
            print(f'The Bank declared bankruptcies. Any kind of public service/transactions are discouraged.')

    @staticmethod
    def generate_current_acc_no():
        while True:
            new_acc_no = random.randrange(1000, 10000)
            if new_acc_no not in CurrentAccount.AllCurrentAccounts:
                new_acc_no = 'CR' + str(new_acc_no)
                return new_acc_no

    @staticmethod
    def account_info(account_number):
        for account in CurrentAccount.AllCurrentAccounts:
            if account['AccountNumber'] == account_number:
                print('----- Account Information -----')
                print('Account Name: ', account['Name'])
                print('Date of Birth: ', account['DateOfBirth'])
                print('Address: ', account['Road'], account['HouseNo'], account['ZIPCode'], account['City'])
                print('Email Address: ', account['Email'])
                print('Account Type: ', account['AccountType'])
                print('Account Number: ', account['AccountNumber'])
            else:
                print(f'Account {account_number} does not exist.')

    @staticmethod
    def deposit_money(account_number, deposit_amount):
        if Bank.Banking_Service_Controller:
            for account in CurrentAccount.AllCurrentAccounts:
                if account['AccountNumber'] == account_number:
                    if deposit_amount > 0:
                        account['CurrentBalance'] += deposit_amount
                        Bank.TotalBankBalance += deposit_amount
                        print(f'Successfully deposited {deposit_amount}€.')                     # Add to transaction history
                    else:
                        print('Invalid Amount.')
                else:
                    print(f'Account {account_number} does not exist.')
        else:
            print(f'The Bank declared bankruptcies. Any kind of public service/transactions are discouraged.')

    @staticmethod
    def withdraw_money(account_number, expected_amount):
        if Bank.Banking_Service_Controller:
            for account in CurrentAccount.AllCurrentAccounts:
                if account['AccountNumber'] == account_number:
                    if expected_amount > 0:
                        if expected_amount <= account['CurrentBalance']:
                            account['CurrentBalance'] -= expected_amount
                            Bank.TotalBankBalance -= expected_amount
                            print(f'Withdrawal successful, Cash out {expected_amount}€.')       # Add to transaction history
                        else:
                            print('Withdrawal amount exceeded.')
                    else:
                        print('Invalid Amount.')
                else:
                    print(f'Account {account_number} does not exist.')
        else:
            print(f'The Bank declared bankruptcies. Any kind of public service/transactions are discouraged.')

    @staticmethod
    def check_balance(account_number):
        if Bank.Banking_Service_Controller:
            for account in CurrentAccount.AllCurrentAccounts:
                if account['AccountNumber'] == account_number:
                    current_balance = account['CurrentBalance']
                    if current_balance == 0:
                        print('Currently your account is empty.')
                    else:
                        print(f'Currently your balance is {current_balance}€')
                else:
                    print(f'Account {account_number} does not exist.')
        else:
            print(f'The Bank declared bankruptcies. Any kind of public service/transactions are discouraged.')

    @staticmethod
    def transfer_money(your_account_number, target_account_number, target_amount):
        if Bank.Banking_Service_Controller:
            for cr_account in CurrentAccount.AllCurrentAccounts:
                if cr_account['AccountNumber'] == your_account_number:
                    for account in Bank.AllAccounts:
                        if account['AccountNumber'] == target_account_number:
                            if target_amount > 0:
                                if target_amount <= cr_account['CurrentBalance']:
                                    cr_account['CurrentBalance'] -= target_amount
                                    account['CurrentBalance'] += target_amount
                                    print(f'Transfer {target_amount}€, from account {cr_account} to {account} is successful.')  # Add to transaction history
                                else:
                                    print('Transfer amount exceeded.')
                            else:
                                print('Invalid Amount.')
                        else:
                            print(f'Account {target_account_number} does not exist.')
                else:
                    print(f'Account {your_account_number} does not exist.')
        else:
            print(f'The Bank declared bankruptcies. Any kind of public service/transactions are discouraged.')

    @staticmethod
    def apply_loan(account_number, expected_loan_amount):
        if Bank.Banking_Service_Controller:
            for account in CurrentAccount.AllCurrentAccounts:
                if account['AccountNumber'] == account_number:
                    if expected_loan_amount > 0:
                        if expected_loan_amount <= account['MaxLoanLimit']:
                            if account['LoanApplicationToBeGranted'] != 0:
                                if account['CurrentBalance'] != 0:
                                    account['CurrentBalance'] += expected_loan_amount
                                    account['LoanTaken'] += expected_loan_amount
                                    account['MaxLoanLimit'] -= expected_loan_amount
                                    account['LoanApplicationToBeGranted'] -= 1
                                    Bank.TotalLoanTaken += expected_loan_amount
                                    Bank.TotalBankBalance += expected_loan_amount
                                    print(f'Loan approved, Cash {expected_loan_amount}€ is credited to your account.')                                                                           # Add to transaction history
                                else:
                                    print('Empty accounts are not eligible for loan application. To apply for loan, you must deposit an amount.')
                        else:
                            print('Max Loan Limit amount exceeded.')
                    else:
                        print('Invalid Amount.')
                else:
                    print(f'Account {account_number} does not exist.')
        else:
            print(f'The Bank declared bankruptcies. Any kind of public service/transactions are discouraged.')

# (done) deposit
# (done) withdraw / handle error with “Withdrawal amount exceeded” / only withdraw money from his account if he has money in his account
# (done) check available balance
# show account information
# check transaction history
# (done) money transfer / handle error with “Account does not exist” / only transfer money from his account if he has money in his account
# (done) If a user is unable to withdraw the amount of money he has deposited in the bank, he will get a message that the bank is bankrupt.