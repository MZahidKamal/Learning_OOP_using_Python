import random
from bank import Bank

class SavingsAccount:
    AllSavingAccountNumbers = []

    def __init__(self, name, dob, road, house_no, zip_code, city, email):
        self.AccountNumber = SavingsAccount.generate_savings_acc_no()
        account = {
            'Name': name,
            'DateOfBirth': dob,
            'Road': road,
            'HouseNo': house_no,
            'ZIPCode': zip_code,
            'City': city,
            'Email': email,
            'AccountType': 'Saving Account',
            'AccountNumber': self.AccountNumber,
            'CurrentBalance': 0
        }
        SavingsAccount.AllSavingAccountNumbers.append(account)
        Bank.AllAccounts.append(account)
        print(f'Successfully created account {self.AccountNumber}, for {name}.')

    @staticmethod
    def generate_savings_acc_no():
        while True:
            new_acc_no = random.randrange(100, 1000)
            if new_acc_no not in SavingsAccount.AllSavingAccountNumbers:
                new_acc_no = 'SV' + str(new_acc_no)
                return new_acc_no

    @staticmethod
    def deposit_money(account_number, deposit_amount):
        for account in SavingsAccount.AllSavingAccountNumbers:
            if account['AccountNumber'] == account_number:
                if deposit_amount > 0:
                    account['CurrentBalance'] += deposit_amount
                    Bank.TotalBankBalance += deposit_amount
                    print(f'Successfully deposited {deposit_amount}€.')                     # Add to transaction history
                else:
                    print('Invalid Amount.')
            else:
                print(f'Account {account_number} does not exist.')

    @staticmethod
    def withdraw_money(account_number, expected_amount):
        for account in SavingsAccount.AllSavingAccountNumbers:
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

    @staticmethod
    def check_balance(account_number):
        for account in SavingsAccount.AllSavingAccountNumbers:
            if account['AccountNumber'] == account_number:
                current_balance = account['CurrentBalance']
                if current_balance == 0:
                    print('Currently your account is empty.')
                else:
                    print(f'Currently your balance is {current_balance}€')
            else:
                print(f'Account {account_number} does not exist.')



# (done) deposit
# (done) withdraw / handle error with “Withdrawal amount exceeded” / only withdraw money from his account if he has money in his account
# (done) check available balance
# check transaction history
# money transfer / handle error with “Account does not exist” / only transfer money from his account if he has money in his account
# If a user is unable to withdraw the amount of money he has deposited in the bank, he will get a message that the bank is bankrupt.
