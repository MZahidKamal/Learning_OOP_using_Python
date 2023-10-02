#-----------------------------------------------------------------------------------------------------------------------
# 6.5 Encapsulation and Access Modifiers (Public, Private, Protected)
#-----------------------------------------------------------------------------------------------------------------------
"""
class Bank:
    def __init__(self, acc_holder_name, initial_deposit):
        self.acc_holder_name = acc_holder_name
        self.initial_deposit = initial_deposit

rafsan = Bank('Rafsan Hossain', 15000)
print(rafsan.acc_holder_name)
print(rafsan.initial_deposit)

rafsan.initial_deposit = 0

print(rafsan.acc_holder_name)
print(rafsan.initial_deposit)
"""
#-----------------------------------------------------------------------------------------------------------------------
"""
Se the above code, a [Bank] class is created, and under the bank class, an object [rafsan] is created. Rafsan has 
deposited 15000 into his bank account.

Then we have printed the account holder name and the account balance.
Then the account balance is updated to 0.
And then printed again. That means thw account balance can be accessed from outside, which is obviously not expected
in case of sensitive object like bank account.

To prevent this access, the idea of Encapsulation is introduced.

This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
Those types of variables are known as private variables.

The goal of information hiding is to ensure that an object’s state is always valid by controlling access to attributes 
that are hidden from the outside world.

#To Learn more, visit (https://www.geeksforgeeks.org/encapsulation-in-python/).
"""
#-----------------------------------------------------------------------------------------------------------------------
"""
class Bank:
    def __init__(self, acc_holder_name, initial_deposit):
        self.acc_holder_name = acc_holder_name
        self.__initial_deposit = initial_deposit

rafsan = Bank('Rafsan Hossain', 15000)
print(rafsan.acc_holder_name)
#print(rafsan.initial_deposit)
"""

#-----------------------------------------------------------------------------------------------------------------------
"""
See the above code. Before initial deposit we've added two __ underscores and now the initial deposit is no more
accessible from outside world. If you try, it'll show error.

No _   :: Public variable
One _  :: Protected variable
Two __ :: Private variable

"""
#-----------------------------------------------------------------------------------------------------------------------
class Bank:
    def __init__(self, acc_holder_name, initial_deposit, bank_branch):
        self.acc_holder_name = acc_holder_name
        self.__initial_deposit = initial_deposit
        self._bank_branch = bank_branch

    def deposit_money(self, deposit_amount):
        self.__initial_deposit += deposit_amount
        #print(f'{deposit_amount} Euro deposited successfully.')

    def get_balance(self, pin_number):
        if pin_number == 1234:
            return f'Your current account balance is {self.__initial_deposit} Euro.'
        else:
            return f'Wrong PIN, Try again.'

rafsan = Bank('Rafsan Hossain', 15000, 'Banani 11')

print(rafsan.acc_holder_name)
print(rafsan.deposit_money(2000))
print(rafsan.get_balance(1234))

#-----------------------------------------------------------------------------------------------------------------------

print(dir(rafsan))
print(rafsan._Bank__initial_deposit)

"""
Even after Encapsulation, we can use [dir()] function to get all the sub-directories of that class. Hence we can have
access over some private information. Later we'll learn how to protect this loop hole. 
"""
#-----------------------------------------------------------------------------------------------------------------------
