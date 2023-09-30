#-----------------------------------------------------------------------------------------------------------------------
# 5.1 Introduction to Simple Class
#-----------------------------------------------------------------------------------------------------------------------
#The class creates a user-defined data structure, which holds its own data members and member functions,
#which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.


#Creating a user defined class. And initializing some values in it.
class Phone:
    Brand = 'Samsung'
    Model = 'A71'
    ReleaseYear = 2022
    Price = 350

#Creating an object of that class.
myPhone = Phone()

#Printing the object.
print(myPhone)

#If we write [objectName.] then the attributes will show up.
#Printing the object attributes separately.
print(myPhone.Brand)
print(myPhone.Model)
print(myPhone.ReleaseYear)
print(myPhone.Price)


# To Learn more, visit (https://www.w3schools.com/python/python_classes.asp).
# To Learn more, visit (https://www.geeksforgeeks.org/python-classes-and-objects/).

#-----------------------------------------------------------------------------------------------------------------------
