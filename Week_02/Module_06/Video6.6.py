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
# To Learn more, visit (https://www.geeksforgeeks.org/abstract-classes-in-python/).
#-----------------------------------------------------------------------------------------------------------------------
