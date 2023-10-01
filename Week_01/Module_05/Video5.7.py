#-----------------------------------------------------------------------------------------------------------------------
# 5.7 Use multiple classes to create a school
#-----------------------------------------------------------------------------------------------------------------------
#Creating a multiple classes with instance attributes.
class Teacher:
    def __init__(self, name, department, subject):
        self.name = name
        self.department = department
        self.subject = subject

    def __repr__(self):
        return f'Teacher\'s name is {self.name}, currently in {self.department} department and teaching {self.subject}.'

class Student:
    def __init__(self, name, standard, roll):
        self.name = name
        self.standard = standard
        self.roll = roll

    def __repr__(self):
        return f'Student name is {self.name}, currently in standard {self.standard} with roll number {self.roll}.'

#Creatin an object of the class, with some value initialization.
tahiya = Student('Tahiya Islam', 9, 1)

#Printing the object.
print(tahiya)

#-----------------------------------------------------------------------------------------------------------------------
"""
See the output.
<__main__.Student object at 0x0000025DA2A97550>

This output is obviously not expected. In this situation we'll create a separate function to represent the output.
Let's see how to do it.
"""
#-----------------------------------------------------------------------------------------------------------------------
"""
Now see the output.
Student name is Tahiya Islam, currently in standard 9 with roll number 1.
Seems nice.

Now let's create another class of Teacher. Let's see how to do it.
"""
#-----------------------------------------------------------------------------------------------------------------------
nahid = Teacher('Nahid Momen', 'CSE', 'Networking')
print(nahid)
