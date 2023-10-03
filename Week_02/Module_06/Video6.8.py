#-----------------------------------------------------------------------------------------------------------------------
# 6.8 Polymorphism
#-----------------------------------------------------------------------------------------------------------------------
#The word polymorphism means having many forms.
#In programming, polymorphism means the same function name (but different signatures) being used for different types.
#The key difference is the data types and number of arguments used in function.

# To Learn more, visit (https://www.geeksforgeeks.org/polymorphism-in-python/).

#-----------------------------------------------------------------------------------------------------------------------
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f'{self.name} is making sound.')

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name)


tom = Cat('TomCat')
tom.make_sound()
"""
#-----------------------------------------------------------------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f'{self.name} is making sound.')

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def make_sound(self):
        print(f'{self.name} is making meow meow sound.')

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def make_sound(self):
        print(f'{self.name} is making gheu gheu sound.')

class Goat(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def make_sound(self):
        print(f'{self.name} is making meeh meeh sound.')


tom = Cat('TomCat')
tom.make_sound()

piklu = Dog('Piklu')
piklu.make_sound()

schuko = Goat('Schuko')
schuko.make_sound()

animals = [tom, piklu, schuko]

for animal in animals:
    animal.make_sound()

#-----------------------------------------------------------------------------------------------------------------------

class Shape:
    def __init__(self, name):
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)

    def area(self):
        return 3.1416 * self.radius ** 2

#-----------------------------------------------------------------------------------------------------------------------
