#-----------------------------------------------------------------------------------------------------------------------
# 6.2 Common and uncommon things and Inheritance
#-----------------------------------------------------------------------------------------------------------------------
"""
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
"""
#-----------------------------------------------------------------------------------------------------------------------
"""
class Phone:
    def __init__(self, brand, model, price, color, duel_sim):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.duel_sim = duel_sim

    def run(self):
        return f'The phone is running Properly.'

    def call(self, number, text):
        return f'Sending SMS to {number}, and the text is {text}.'
"""
#-----------------------------------------------------------------------------------------------------------------------

"""
class Camera:
    def __init__(self, brand, model, price, pixel, lens):
        self.brand = brand
        self.model = model
        self.price = price
        self.pixel = pixel
        self.lens = lens

    def run(self):
        pass

    def capture(self, number, text):
        pass
"""
#-----------------------------------------------------------------------------------------------------------------------
"""
See the three classes above, Laptop, Phone and Camera. In all three classes some attributes are common. They are [brand,
model, price]. Also the [run] function is common in all classes. While creating three classes, we had to repeat the code
3 times. It's clearly a waste or time, space and resource, It's also not well organized.

To save time, space and resource, and to make it more organized, there is [Inheritance] is introduced.
Inheritance is the capability of one class to derive or inherit the properties from another class.

Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

// To Learn more, visit (https://www.geeksforgeeks.org/inheritance-in-python/).
// To Learn more, visit (https://www.w3schools.com/python/python_inheritance.asp).
"""
#-----------------------------------------------------------------------------------------------------------------------
"""
Not let's create another class [Device] to hold all the common attributes and functions.
"""
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
"""
Now see, all duplicates are removed. Here Device is the [Parent Class] and the [Laptop, Phone, Camera] are the child
classes.

Every Child class have some common attributes, which is also present in Parent class.
Every Child class have some uncommon attributes, which is not present in Parent class.
Vise versa
Every Parent class have some common attributes, which is also present in Child class.
Every Parent class have some uncommon attributes, which is not present in Child class.

After that we'll have to establish connections in between parent and child classes. 
"""
#-----------------------------------------------------------------------------------------------------------------------
