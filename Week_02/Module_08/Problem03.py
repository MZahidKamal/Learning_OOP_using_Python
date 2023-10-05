#-----------------------------------------------------------------------------------------------------------------------
# Python Mid Term Exam
# https://docs.google.com/document/d/1DxHEw2Ij6FTqMijlkn4NH6U1BdxeesyLWOjINiKFtR0/edit?usp=sharing
# Problem 03:
"""
Make a method in Hall class named entry_show() which will take id, movie_name and time in string format. Make a tuple
with all the information and append it to the show_list attribute. Allocate seats with rows and cols using 2d list,
initially all seats will be free. Make a key with id to the attribute seats and value will be the 2d list.
"""
#-----------------------------------------------------------------------------------------------------------------------
class StarCinema:
    hall_list = []

    def entry_hall(self, hall):                 # Here hall will be an object of class Hall.
        self.hall_list.append(hall)

#-----------------------------------------------------------------------------------------------------------------------
class Hall(StarCinema):
    def __init__(self, rows, columns, hall_no):
        self.seats = {}                  # Dictionary of seat's information
        self.show_list = []              # [()()()] List of Tuples
        #
        self.rows = rows                 # The row of the seats in that hall
        self.columns = columns           # The column of the seats in that hall
        self.hall_no = hall_no           # The unique no. of that hall
        #
        super().__init__()
        self.entry_hall(self)

    def entry_show(self, show_id, show_name, show_time):
        show = (show_id, show_name, show_time)
        self.show_list.append(show)

#Creating a cinema hall building. The name is CineStar.
cinestar = StarCinema()

#Creating a cinema hall named dolby_hall_01. Because of inheriting the Hall class from the StarCinema, and using the
#initializer of the StarCinema class, as soon as a hall object is created, it'll automatically be added in the list.
dolby_hall_11 = Hall(12, 20, 11)

#cinestar.entry_hall(dolby_hall_11)

#To check, let's print the length of the list. If the size is increased by 1, then insertion successful.
print(len(cinestar.hall_list))

#A new method 'entry_show' is created under the class Hall. Then a show is entered using that function.
dolby_hall_11.entry_show('2956', 'Prison Break', '18:00')

#To check, let's print the length of the list. If the size is increased by 1, then insertion successful.
print(len(dolby_hall_11.show_list))
#-----------------------------------------------------------------------------------------------------------------------
