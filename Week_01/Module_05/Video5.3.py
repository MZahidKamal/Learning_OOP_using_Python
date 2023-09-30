#-----------------------------------------------------------------------------------------------------------------------
# 5.3 Constructors and __init__ in python
#-----------------------------------------------------------------------------------------------------------------------
#Creating a user defined class. And initializing some values in it.
class Phone:
    Manufacturer = 'China'

    #Creating the constructor ot this class.
    def __init__(self, brand, model, release_year, price):
        self.brand = brand
        self.model = model
        self.release_year = release_year
        self.price = price

    #Creating methods under this class.
    def call(self, phone_number):
        status = f'Calling {phone_number} to Someone from My Phone.'
        return status

    def message(self, phone_number, text):
        status = f'Texting "{text}" to {phone_number} to Someone from My Phone.'
        return status


# #Creating an object, using the constructor of the class. And printing the object.
myPhone = Phone('Samsung', 'S4', 2018, '256€')
print(myPhone.brand, myPhone.model, myPhone.release_year, myPhone.price)

herPhone = Phone('Samsung', 'A72', 2022, '365€')
print(herPhone.brand, herPhone.model, herPhone.release_year, herPhone.price)

momPhone = Phone('iPhone', '14 ProMax', 2022, '999€')
print(momPhone.brand, momPhone.model, momPhone.release_year, momPhone.price)

#-----------------------------------------------------------------------------------------------------------------------
