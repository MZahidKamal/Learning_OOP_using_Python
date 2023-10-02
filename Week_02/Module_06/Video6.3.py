#-----------------------------------------------------------------------------------------------------------------------
# 6.3 Multi-level Inheritance
#-----------------------------------------------------------------------------------------------------------------------
class Device:
    def __init__(self, brand, model, price, origin):
        self.brand = brand
        self.model = model
        self.price = price
        self.origin = origin

    def run(self):
        return f'The Device is running Properly.'

#-----------------------------------------------------------------------------------------------------------------------
class Laptop:
    def __init__(self, color, memory):
        self.color = color
        self.memory = memory

    def code(self):
        return f'Learning Python and practicing.'

#-----------------------------------------------------------------------------------------------------------------------
class Phone:
    def __init__(self, color, duel_sim):
        self.color = color
        self.duel_sim = duel_sim

    def call(self, number, text):
        return f'Sending SMS to {number}, and the text is {text}.'

#-----------------------------------------------------------------------------------------------------------------------

class Camera:
    def __init__(self, pixel, lens):
        self.pixel = pixel
        self.lens = lens

    def capture(self, number, text):
        pass

#-----------------------------------------------------------------------------------------------------------------------
