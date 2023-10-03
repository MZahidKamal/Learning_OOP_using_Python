#-----------------------------------------------------------------------------------------------------------------------
# 6.6 Abstract Classes and abstractmethod
#-----------------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        print('I need food.')

    @abstractmethod
    def move(self):
        print('I want to play.')

class Monkey(Animal):
    def __init__(self, name):
        self.category = 'Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print('Eating banana.')

    def move(self):
        print('Hanging on the branches.')


lyca = Monkey('Lyca')
lyca.eat()

#-----------------------------------------------------------------------------------------------------------------------
"""
An abstract class in Python is typically created to declare a set of methods that must be created in any child class 
built on top of this abstract class.
"""
# To Learn more, visit (https://www.geeksforgeeks.org/abstract-classes-in-python/).
#-----------------------------------------------------------------------------------------------------------------------
