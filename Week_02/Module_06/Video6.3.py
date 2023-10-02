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
class Laptop(Device):
    def __init__(self, brand, model, price, origin, color, memory):
        self.color = color
        self.memory = memory
        super().__init__(brand, model, price, origin)

    def __repr__(self):
        return f'Brand {self.brand}, Model {self.model}, Price {self.price}, Origin {self.origin}, Color {self.color} and Memory {self.memory}.'

    def code(self):
        return f'Learning Python and practicing.'

#-----------------------------------------------------------------------------------------------------------------------
class Phone(Device):
    def __init__(self, brand, model, price, origin, color, duel_sim):
        self.color = color
        self.duel_sim = duel_sim
        super().__init__(brand, model, price, origin)

    def __repr__(self):
        return f'Brand {self.brand}, Model {self.model}, Price {self.price}, Origin {self.origin}, Color {self.color} and Duel-Sim {self.duel_sim}.'

    def call(self, number, text):
        return f'Sending SMS to {number}, and the text is {text}.'

#-----------------------------------------------------------------------------------------------------------------------

class Camera(Device):
    def __init__(self, brand, model, price, origin, pixel, lens):
        self.pixel = pixel
        self.lens = lens
        super().__init__(brand, model, price, origin)

    def __repr__(self):
        return f'Brand {self.brand}, Model {self.model}, Price {self.price}, Origin {self.origin}, Pixel {self.pixel} and Lens {self.lens}.'

    def capture(self, number, text):
        pass

#-----------------------------------------------------------------------------------------------------------------------

my_laptop = Laptop('Huawei', 'Slimbook', 860, 'China', 'Silver', '1TB')
print(my_laptop)
print(my_laptop.brand)
print(my_laptop.model)
print(my_laptop.price)
print(my_laptop.origin)
print(my_laptop.color)
print(my_laptop.memory)
print()

my_phone = Phone('Samsung', 'A71', 350, 'Korea', 'Black', 'Yes')
print(my_phone)
print(my_phone.brand)
print(my_phone.model)
print(my_phone.price)
print(my_phone.origin)
print(my_phone.color)
print(my_phone.duel_sim)
print()

my_camera = Camera('Canon', '70D', 1600, 'Japan', 64, '350 Zoom')
print(my_camera)
print(my_camera.brand)
print(my_camera.model)
print(my_camera.price)
print(my_camera.origin)
print(my_camera.pixel)
print(my_camera.lens)
print()

#-----------------------------------------------------------------------------------------------------------------------
"""
Now see the code above and see the printed output. Every classes like Laptop, Phone and Camera can use the attributes
from the Device class. Here Device is the Base/Parent class and the Laptop, Phone and Camera are the Derived/Child
classes.

Parent class and child classes are co-related and attributes are shared.
"""
#-----------------------------------------------------------------------------------------------------------------------
"""
So far what we have learned is Inheritance. But there are different types of Inheritance.
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance

// To Learn more, visit (https://www.geeksforgeeks.org/types-of-inheritance-python/).
"""
#-----------------------------------------------------------------------------------------------------------------------
