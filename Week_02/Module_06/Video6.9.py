#-----------------------------------------------------------------------------------------------------------------------
# 6.9 Module summary
#-----------------------------------------------------------------------------------------------------------------------
class Book:
    def __init__(self, name):
        self.name = name

    def read(self):
        #pass
        raise NotImplementedError

class Physics(Book):
    def __init__(self, name, lab):
        self.lab = lab
        super().__init__(name)

    def read(self):
        print('Reading physics book.')

topon = Physics('Topon Sir', True)

print(issubclass(Physics, Book))
print(isinstance(topon, Physics))
print(isinstance(topon, Book))

topon.read()

#-----------------------------------------------------------------------------------------------------------------------
