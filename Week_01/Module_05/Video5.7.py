#-----------------------------------------------------------------------------------------------------------------------
# 5.7 Use multiple classes to create a school
#-----------------------------------------------------------------------------------------------------------------------
#Creating a multiple classes with instance attributes.
class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.teachers = []
        self.students = []

    def appoint_teacher(self, name, department, subject):
        idno = len(self.teachers) + 100
        teacher = Teacher(name, idno, department, subject)
        self.teachers.append(teacher)
        print(f'{name} is appointed successfully.')

    def enroll_student(self, name, standard, admission_fee):
        if admission_fee < 90:
            print(f'{name}\'s enrollment is not successful. Admission Fee is 90€. Please provide {90 - admission_fee}€ more.')
        else:
            roll = len(self.students) + 1
            student = Student(name, standard, roll)
            self.students.append(student)

            if admission_fee == 90:
                print(f'Admission Fee 90€ paid. {name}\'s enrollment is successful.')

            elif admission_fee > 90:
                print(f'Admission Fee 90€ paid. {name}\'s enrollment is successful. Remaining {admission_fee - 90}€ is refunded.')

    def __repr__(self):
        print(f'Welcome to your School {self.school_name}')
        print()
        print('---------- Our Respectful Teachers ----------')
        for teacher in self.teachers:
            print(teacher)
        print()
        print('---------- Our Talented Students ----------')
        for student in self.students:
            print(student)
        print()
        return f'------------'
#-----------------------------------------------------------------------------------------------------------------------

class Teacher:
    def __init__(self, name, idno, department, subject):
        self.name = name
        self.idno = idno
        self.department = department
        self.subject = subject

    def __repr__(self):
        return f'Teacher\'s Name: {self.name}, Id.No.: {self.idno}, Department: {self.department}, Subject: {self.subject}.'

#-----------------------------------------------------------------------------------------------------------------------

class Student:
    def __init__(self, name, standard, roll):
        self.name = name
        self.standard = standard
        self.roll = roll

    def __repr__(self):
        return f'Student\'s Name: {self.name}, Standard: {self.standard}, Roll number: {self.roll}.'

#-----------------------------------------------------------------------------------------------------------------------

#Creatin a student object, with some value initialization, and then print it.
tahiya = Student('Tahiya Islam', 9, 1)
print(tahiya)

#-----------------------------------------------------------------------------------------------------------------------

#Creatin a teacher object, with some value initialization, and then print it.
nahid = Teacher('Nahid Momen', 55, 'CSE', 'Networking')
print(nahid)
print()

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
"""
Teacher class creation is done, object creations is done, printing is done. And here is how it looks like.
Teacher's name is Nahid Momen, currently in CSE department and teaching Networking.
"""
#-----------------------------------------------------------------------------------------------------------------------
"""
Now we'll give it a new shape. We'll also create another class [School] with some functions [appoint_teacher] and
[enroll_student]. Now let's add a school, some teachers and some students. Then we'll print them.
"""
#-----------------------------------------------------------------------------------------------------------------------
villa_sunshine = School('Villa SunShine')

villa_sunshine.appoint_teacher('Nahid Momen', 'CSE', 'Networking')
villa_sunshine.appoint_teacher('Rahat Khan Pathan', 'CSE', 'Programming')
villa_sunshine.appoint_teacher('Riad Hasan', 'BBA', 'Digital Marketing')
print()

villa_sunshine.enroll_student('Tahiya Islam', 9, 50)
villa_sunshine.enroll_student('Farabi Hossain', 10, 90)
villa_sunshine.enroll_student('Inaya Nahid', 1, 100)
print()

print(villa_sunshine)
