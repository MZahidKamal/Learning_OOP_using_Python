#-----------------------------------------------------------------------------------------------------------------------
# 7.6 Class Composition. inheritance vs composition
#-----------------------------------------------------------------------------------------------------------------------
class Animal:
    pass

class Deer(Animal):
    pass

class Tiger(Animal):
    pass

class Cat(Animal):
    pass

"""
See the above example. Here Deer, Tiger and Cat are inherited from Animal class. We also can say, Inheritance give us
"is a" type relation in between two classes.

In case of inheritance, we usually we go from larger class to smaller classes.
"""
#-----------------------------------------------------------------------------------------------------------------------
class Engine:
    def __init__(self):
        pass

    def start(self):
        return "Engine started."

class Driver:
    def __init__(self):
        pass

class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()



"""
But, in case of composition, we usually we go from smaller classes to larger class. We also can say, Composition give us
"has a" type relation in between two classes.
#To Learn more, visit (https://www.geeksforgeeks.org/inheritance-and-composition-in-python/).
"""
#-----------------------------------------------------------------------------------------------------------------------
#Let's see another example.

class CPU:
    def __init__(self, cores):
        self.cores = cores

class RAM:
    def __init__(self, size):
        self.size = size

class HardDrive:
    def __init__(self, capacity):
        self.capacity = capacity

class Computer:
    def __init__(self, cores, size, capacity):
        self.cpu = CPU(cores)
        self.ram = RAM(size)
        self.hard_drive = HardDrive(capacity)

my_pc = Computer(9, '64 GB', '4 TB')
print(my_pc.cpu.cores)
print(my_pc.ram.size)
print(my_pc.hard_drive.capacity)

#-----------------------------------------------------------------------------------------------------------------------




























