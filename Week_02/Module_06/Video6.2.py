#-----------------------------------------------------------------------------------------------------------------------
# 6.2 Common and uncommon things and Inheritance
#-----------------------------------------------------------------------------------------------------------------------
class Laptop:
    def __init__(self, brand, model, price, color, memory):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'The laptop is running Properly.'

    def code(self):
        return f'Learning Python and practicing.'

#-----------------------------------------------------------------------------------------------------------------------
class Phone:
    def __init__(self, brand, price, color, duel_sim):
        self.brand = brand
        self.price = price
        self.color = color
        self.duel_sim = duel_sim

    def run(self):
        return f'The phone is running Properly.'

    def call(self, number, text):
        return f'Sending SMS to {number}, and the text is {text}.'
