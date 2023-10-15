import random
from bank import Bank
from transaction import Transaction

class SavingsAccount:
    TransactionHistory = []

    def __init__(self, name, city, email):
        self.AccountNumber = SavingsAccount.generate_savings_acc_no()
        account = {
            'Name': name,
            'City': city,
            'Email': email,
            'AccountType': 'Savings Account',
            'AccountNumber': self.AccountNumber,
            'CurrentBalance': 0
        }
        if Bank.Banking_Service_Controller:
            Bank.AllSavingAccounts.append(account)
            Bank.AllAccounts.append(account)
            print(f'Successfully created account {self.AccountNumber}, for {name}.')
        else:
            print(f'The Bank declared bankruptcies. Any kind of public service/transactions are discontinued/discouraged.')

    @staticmethod
    def generate_savings_acc_no():
        while True:
            new_acc_no = random.randrange(100, 1000)
            if new_acc_no not in Bank.AllSavingAccounts:
                new_acc_no = 'SV' + str(new_acc_no)
                return new_acc_no

    @staticmethod
    def account_info(account_number):
        for account in Bank.AllSavingAccounts:
            if account['AccountNumber'] == account_number:
                print('----- Account Information -----')
                print('Account Name: ', account['Name'])
                print('Address: ', account['City'])
                print('Email Address: ', account['Email'])
                print('Account Type: ', account['AccountType'])
                print('Account Number: ', account['AccountNumber'])
                return
        print(f'Account {account_number} does not exist.')

    @staticmethod
    def deposit_money(account_number, deposit_amount):
        if Bank.Banking_Service_Controller:
            for account in Bank.AllSavingAccounts:
                if account['AccountNumber'] == account_number:
                    if deposit_amount > 0:
                        account['CurrentBalance'] += deposit_amount
                        Bank.TotalBankBalance += deposit_amount
                        SavingsAccount.TransactionHistory.append(Transaction.record(account_number, 'Deposit Money', deposit_amount))
                        print(f'Successfully deposited {deposit_amount}€.')
                        return
                    else:
                        print('Invalid Amount.')
                        return
            print(f'Account {account_number} does not exist.')
        else:
            print(f'The Bank declared bankruptcies. Any kind of public service/transactions are discontinued/discouraged.')

    @staticmethod
    def withdraw_money(account_number, expected_amount):
        if Bank.Banking_Service_Controller:
            for account in Bank.AllSavingAccounts:
                if account['AccountNumber'] == account_number:
                    if expected_amount > 0:
                        if expected_amount <= account['CurrentBalance']:
                            account['CurrentBalance'] -= expected_amount
                            Bank.TotalBankBalance -= expected_amount
                            SavingsAccount.TransactionHistory.append(Transaction.record(account_number, 'Withdraw Money', expected_amount))
                            print(f'Withdrawal successful, Cash out {expected_amount}€.')
                            return
                        else:
                            print('Withdrawal amount exceeded.')
                            return
                    else:
                        print('Invalid Amount.')
                        return
            print(f'Account {account_number} does not exist.')
        else:
            print(f'The Bank declared bankruptcies. Any kind of public service/transactions are discontinued/discouraged.')

    @staticmethod
    def check_balance(account_number):
        if Bank.Banking_Service_Controller:
            for account in Bank.AllSavingAccounts:
                if account['AccountNumber'] == account_number:
                    current_balance = account['CurrentBalance']
                    if current_balance == 0:
                        print('Currently your account is empty.')
                        return
                    else:
                        print(f'Currently your balance is {current_balance}€')
                        return
            print(f'Account {account_number} does not exist.')
        else:
            print(f'The Bank declared bankruptcies. Any kind of public service/transactions are discontinued/discouraged.')

    @staticmethod
    def transfer_money(your_account_number, target_account_number, target_amount):
        if Bank.Banking_Service_Controller:
            for sv_account in Bank.AllSavingAccounts:
                if sv_account['AccountNumber'] == your_account_number:
                    for account in Bank.AllAccounts:
                        if account['AccountNumber'] == target_account_number:
                            if target_amount > 0:
                                if target_amount <= sv_account['CurrentBalance']:
                                    sv_account['CurrentBalance'] -= target_amount
                                    account['CurrentBalance'] += target_amount
                                    SavingsAccount.TransactionHistory.append(Transaction.record(your_account_number, 'Transfer Money', target_amount))
                                    print(f'Transfer {target_amount}€, from account {your_account_number} to {target_account_number} is successful.')
                                    return
                                else:
                                    print('Transfer amount exceeded.')
                                    return
                            else:
                                print('Invalid Amount.')
                                return
                    print(f'Account {target_account_number} does not exist.')
            print(f'Account {your_account_number} does not exist.')
        else:
            print(f'The Bank declared bankruptcies. Any kind of public service/transactions are discontinued/discouraged.')

    @staticmethod
    def show_transaction_history(account_number):
        if Bank.Banking_Service_Controller:
            account_exists = False
            for account in Bank.AllSavingAccounts:
                if account['AccountNumber'] == account_number:
                    account_exists = True
                    print(f'Transaction History for {account_number}:')
                    for transaction in SavingsAccount.TransactionHistory:
                        if transaction['AccountNo'] == account_number:
                            print('Date/Time:', transaction['DateAndTime'], '\t', transaction['TransactionType'], '\t',
                                  transaction['Amount'], '€')
                        else:
                            print(f'No transaction made so far.')
            if not account_exists:
                print(f'Account {account_number} does not exist.')
        else:
            print(
                f'The Bank declared bankruptcies. Any kind of public service/transactions are discontinued/discouraged.')
