class Bank:
    AllAccounts = []
    AllSavingAccounts = []
    AllCurrentAccounts = []
    TotalBankBalance = 0
    TotalLoanTaken = 0
    Banking_Service_Controller = True


    def __init__(self, name, road, house_no, zip_code, city, state, country, url):
        self.Name = name
        self.Road = road
        self.HouseNo = house_no
        self.ZIPCode = zip_code
        self.City = city
        self.State = state
        self.Country = country
        self.Website = url


    def bank_info(self):
        print(f'\n----- Bank Information -----\n{self.Name}\n{self.Road} {self.HouseNo}\n{self.ZIPCode} {self.City}\n{self.State} {self.Country}\n{self.Website}')


    def declare_bankrupt(self):
        self.Banking_Service_Controller = False
        print(f'{self.Name} declared bankruptcies. Any kind of public service/transactions are discouraged.')

    def delete_account(self, target_account_number):
        for account in self.AllAccounts:
            if account['AccountNumber'] == target_account_number:
                if account['AccountType'] == 'Savings Account':
                    balance = account['CurrentBalance']
                    self.AllAccounts.remove(account)
                    if balance > 0:
                        print(f'Successfully removed account {target_account_number}.')
                    else:
                        print(f'Successfully removed account {target_account_number}.')

# Can delete any user account
# Can see all user accounts list
# Can check the total available balance of the bank
# Can check the total loan amount
# Can on or off the loan feature of the bank.
