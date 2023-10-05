#-----------------------------------------------------------------------------------------------------------------------
# Python Mid Term Exam
# https://docs.google.com/document/d/1DxHEw2Ij6FTqMijlkn4NH6U1BdxeesyLWOjINiKFtR0/edit?usp=sharing
# Problem 02:
"""
Make a class named Hall which will have 5 instance attributes given below
    seats which is a dictionary of seats information
    show_list which is a list of tuples
    rows which is the row of the seats in that hall
    cols which is the column of the seats in that hall
    hall_no which is the unique no. of that hall
Initialize an object of class Hall with rows, cols and hall_no. And insert that object to the Star_Cinema class
attribute named hall_list inside the initializer using inheritance. seats and show_list will be empty initially.
"""
#-----------------------------------------------------------------------------------------------------------------------
class StarCinema:
    hall_list = []

    def entry_hall(self, hall):                 # Here hall will be an object of class Hall.
        self.hall_list.append(hall)

#-----------------------------------------------------------------------------------------------------------------------
class Hall:
    def __init__(self, rows, columns, hall_no):
        self.seats = {}                  # Dictionary of seat's information
        self.show_list = []              # [()()()] List of Tuples
        self.rows = rows                 # The row of the seats in that hall
        self.columns = columns           # The column of the seats in that hall
        self.hall_no = hall_no           # The unique no. of that hall


#Creating a cinema hall building. The name is CineStar.
cinestar = StarCinema()

#Creating a cinema hall named dolby_hall_01. With 12 rows, 20 columns and hall no will be 11.
dolby_hall_11 = Hall(12, 20, 11)

#Now entering the hall inside the CineStart building complex using entry_hall function.
cinestar.entry_hall(dolby_hall_11)

#To check, let's print the length of the list. If 1, then insertion successful.
print(len(cinestar.hall_list))

#-----------------------------------------------------------------------------------------------------------------------
