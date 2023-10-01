#Creating a class with instance attributes.
class ClassName:

    # Creating the constructor of the class.
    def __int__(self, attributes):
        self.attributes = attributes
        self.instanceAttributes = []

    # Creating a function/method under the class.
    def __init__(self, parameters):
        self.parameters = parameters

objectName = ClassName('xyz')