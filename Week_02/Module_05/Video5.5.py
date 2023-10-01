# -----------------------------------------------------------------------------------------------------------------------
# 5.5 Explore Bank withdraw deposit and balance using class
# -----------------------------------------------------------------------------------------------------------------------
# Creating a class with instance attributes.
class Bank:

    # Creating the constructor of the class.
    def __init__(self, balance_amount):
        self.balance_amount = balance_amount
        self.min_withdraw = 100
        self.max_withdraw = 100000

    # Creating a functions/methods under the class.
    def balance(self):
        print (f'Your current account balance is {self.balance_amount} Euro.')

    def deposit(self, new_amount):
        if new_amount > 0:
            self.balance_amount += new_amount
            print(f'{new_amount} Euro is deposited successfully. Your new balance is not {self.balance_amount} Euro.')

    def withdraw(self, expected_amount):
        if expected_amount > self.balance_amount:
            print(f'You don\'t have sufficient balance in your account.')

        elif expected_amount < self.min_withdraw:
            print(f'Your expected amount is below minimum withdraw limit. Please try again.')

        elif expected_amount > self.max_withdraw:
            print(f'Your expected amount is above maximum withdraw limit. Please try again.')

        else:
            self.balance_amount -= expected_amount
            print(f'Here is your {expected_amount} Euro. Your new balance is not {self.balance_amount} Euro.')

commerzbank = Bank(15000)
commerzbank.balance()
commerzbank.deposit(2000)
commerzbank.withdraw(600)
print()

#-----------------------------------------------------------------------------------------------------------------------

#Now let's try the same code for another bank.

deutschbank = Bank(25000)
deutschbank.balance()
deutschbank.deposit(2000)
deutschbank.withdraw(600)

#-----------------------------------------------------------------------------------------------------------------------
