class Bank:
    AllAccounts = []
    TotalBankBalance = 0
    TotalLoanTaken = 0
    WithdrawController = True
    LoanController = True


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
        print(f'----- Bank Information -----\n{self.Name}\n{self.Road} {self.HouseNo}\n{self.ZIPCode} {self.City}\n{self.State} {self.Country}\n{self.Website}')


    def declare_bankrupt(self):
        self.WithdrawController = False
        self.LoanController = False
        print(f'{self.Name} bank declared bankruptcies. Any kind of public transactions are discouraged.')
