#-----------------------------------------------------------------------------------------------------------------------
# Python Mid Term Exam
# https://docs.google.com/document/d/1OZH_1S1pcmloJz-PZWwLVbLcx0Zob1YVoWNTvVIXUNI/edit
# Problem 07:
"""
"""
#-----------------------------------------------------------------------------------------------------------------------
class StarCinema:
    hall_list = []
    counter_list = []
    show_list = []
    seats = {}

    def entry_hall(self, hall):                 # Here hall will be an object of class Hall.
        self.hall_list.append(hall)

    def entry_counter(self, counter):           # Here counter will be an object of class Counter.
        self.counter_list.append(counter)

#-----------------------------------------------------------------------------------------------------------------------
class Counter(StarCinema):
    def __init__(self):
        super().__init__()
        self.counter_list.append(self)
        self.hall_list = StarCinema.hall_list.copy()
        self.show_list = StarCinema.show_list.copy()
        self.seats = StarCinema.seats.copy()

    def view_show_list(self):
        for show in self.show_list:
            print(f'ID: {show[0]}     Show Name: {show[1]}     Show Time: {show[2]} o\'clock')

    def view_available_seats(self, desired_show_id):
        if desired_show_id not in self.seats:
            print(f'Show ID {desired_show_id} is invalid. Provide a valid show ID, please.')
        else:
            for seat_matrix in self.seats[desired_show_id]:
                print(seat_matrix, end="\n")

    # def book_seat(self, desired_show_id, desired_row, desired_column):
    #     if desired_show_id not in self.seats:
    #         print(f'Show ID {desired_show_id} is invalid. Provide a valid show ID, please.')
    #     else:
    #         if (desired_row <= 0 or desired_row > self.rows or desired_column <= 0 or desired_column > self.columns):
    #             print(f'Seat at row {desired_row} column {desired_column} is not existed. Please choose a valid seat.')
    #
    #         elif self.seats[desired_show_id][desired_row][desired_column] != '_Free_':
    #             print(f'Seat at row {desired_row} column {desired_column} is already booked. Please choose another seat.')
    #
    #         else:
    #             self.seats[desired_show_id][desired_row-1][desired_column-1] = 'Booked'
    #             print(f'Seat at row {desired_row} column {desired_column} is booked successfully. Have a nice showtime.')
    #     return


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
        #Creating a Tupple with show information, naming it 'show' and appending it into the show_list.
        show = (show_id, show_name, show_time)
        self.show_list.append(show)
        StarCinema.show_list.append(show)
        #
        #Creating a 2D matrix of rows and columns, and initializing all cells of the 2D matrix with 'Free'.
        #Naming it 'seat_matrix', putting it into the seats dictionary as KEY = show_id and VALUE = seat_matrix.
        seat_matrix = [['_Free_' for _ in range(self.columns)] for _ in range(self.rows)]
        self.seats[show_id] = seat_matrix
        StarCinema.seats[show_id] = seat_matrix


    def book_seat(self, desired_show_id, desired_row, desired_column):
        if desired_show_id not in self.seats:
            print(f'Show ID {desired_show_id} is invalid. Provide a valid show ID, please.')
        else:
            if (desired_row <= 0 or desired_row > self.rows or desired_column <= 0 or desired_column > self.columns):
                print(f'Seat at row {desired_row} column {desired_column} is not existed. Please choose a valid seat.')

            elif self.seats[desired_show_id][desired_row][desired_column] != '_Free_':
                print(f'Seat at row {desired_row} column {desired_column} is already booked. Please choose another seat.')

            else:
                self.seats[desired_show_id][desired_row-1][desired_column-1] = 'Booked'
                print(f'Seat at row {desired_row} column {desired_column} is booked successfully. Have a nice show time.')
        return


    def view_show_list(self):
        for show in self.show_list:
            print(f'ID: {show[0]}     Show Name: {show[1]}     Show Time: {show[2]} o\'clock')


    def view_available_seats(self, desired_show_id):
        if desired_show_id not in self.seats:
            print(f'Show ID {desired_show_id} is invalid. Provide a valid show ID, please.')
        else:
            for seat_matrix in self.seats[desired_show_id]:
                print(seat_matrix, end="\n")


#-----------------------------------------------------------------------------------------------------------------------


#Creating a cinema hall building. The name is CineStar.
cinestar = StarCinema()

#Creating a cinema hall named dolby_hall_01. Because of inheriting the Hall class from the StarCinema, and using the
#initializer of the StarCinema class, as soon as a hall object is created, it'll automatically be added in the list.
dolby_hall_11 = Hall(12, 20, 11)

#To check, let's print the length of the list. If the size is increased by 1, then insertion is successful.
print(len(cinestar.hall_list))

#-----------------------------------------------------------------------------------------------------------------------

#A new method 'entry_show' is created under the class Hall. Then a show is entered using that function.
dolby_hall_11.entry_show(2956, 'Prison Break', '18:00')

#To check, let's print the length of the list. If the size is increased by 1, then insertion is successful.
print(len(dolby_hall_11.show_list))

#Also creating a 2D matrix of rows and columns, and initializing all cells of the 2D matrix with 'Free'. Naming it
#'seat_matrix', putting it into the seats dictionary as KEY = show_id and VALUE = seat_matrix. As soon as a show is
#entered, a seat matrix, with all free seats, will be associated with the show id number.

#To check, let's print the length of the list. If the size is increased by 1, then insertion is successful.
print(len(dolby_hall_11.seats))

#-----------------------------------------------------------------------------------------------------------------------

#Now creating another method 'book_seat', under the class Hall. It takes a desired show ID number, a desired seat's row
#and column number, and book the seat for the show if available.

#Let's see the output.
print()
dolby_hall_11.book_seat(2956, 2, 13)

#-----------------------------------------------------------------------------------------------------------------------

#Now creating another method 'view_show_list', under the class Hall. It takes no argument, but return the complete list
#of a show running in this hall.

#Let's see the output.
print()
dolby_hall_11.view_show_list()

#-----------------------------------------------------------------------------------------------------------------------

#Now creating another method 'view_available_seats', under the class Hall. It takes the show id number as argument, and
#return the complete seat plan of the show in this hall.

#Let's see the output.
print()
dolby_hall_11.view_available_seats(2956)

#-----------------------------------------------------------------------------------------------------------------------

#Now creating another class 'Counter'. It will take not argument, but can create an object.

counter = Counter()
print()
print(len(cinestar.counter_list))
print(len(counter.hall_list))
print(len(counter.show_list))
counter.view_show_list()
counter.view_available_seats(2956)
#counter.book_seat(2956, 5, 10)
