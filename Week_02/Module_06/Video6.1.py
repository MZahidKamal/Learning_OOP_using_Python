#-----------------------------------------------------------------------------------------------------------------------
# 6.1 Introduction to OOP with Fleet management
#-----------------------------------------------------------------------------------------------------------------------
#Creating a FlixBus fleet management service using OOP.

class Company:
    def __init__(self, name):
        self.name = name
        self.buses = []
        self.counters = []
        self.routes = []
        self.fares = []
        self.drivers = []
        self.supervisors = []
        self.managers = []

#-----------------------------------------------------------------------------------------------------------------------

class Driver:
    def __init__(self, name, age, licence):
        self.name = name
        self.age = age
        self.licence = licence

#-----------------------------------------------------------------------------------------------------------------------

class Counter:
    def __init__(self):
        pass

    def purchase_ticket(self, start, destination):
        pass

#-----------------------------------------------------------------------------------------------------------------------

class Passenger:
    def __init__(self):
        pass

#-----------------------------------------------------------------------------------------------------------------------

class Supervisor:
    def __init__(self):
        pass

#-----------------------------------------------------------------------------------------------------------------------

lalMia = Driver('Lal Mia', 32, 12345)
print(lalMia)