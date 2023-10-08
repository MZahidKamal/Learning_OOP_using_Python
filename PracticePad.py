import sys


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


    def book_ticket(self, desired_show_id, desired_row, desired_column):
        rows = len(self.seats[desired_show_id])
        columns = len(self.seats[desired_show_id][0])
        if desired_show_id not in self.seats:
            print(f'Show ID {desired_show_id} is invalid. Provide a valid show ID, please.')
        else:
            if (desired_row <= 0 or desired_row > rows) or (desired_column <= 0 or desired_column > columns):
                print(f'Seat at row {desired_row} column {desired_column} is not existed. Please choose a valid seat.')

            elif self.seats[desired_show_id][desired_row][desired_column] != ' Free ':
                print(f'Seat at row {desired_row} column {desired_column} is already booked. Please choose another seat.')

            else:
                self.seats[desired_show_id][desired_row-1][desired_column-1] = 'Booked'
                print(f'Seat at row {desired_row} column {desired_column} is booked successfully. Have a nice showtime.')
        return


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


    def entry_show(self, show_id, show_name, show_time, hall_no):
        #Creating a Tupple with show information, naming it 'show' and appending it into the show_list.
        show = (show_id, show_name, show_time, hall_no)
        self.show_list.append(show)
        StarCinema.show_list.append(show)
        #
        #Creating a 2D matrix of rows and columns, and initializing all cells of the 2D matrix with 'Free'.
        #Naming it 'seat_matrix', putting it into the seats dictionary as KEY = show_id and VALUE = seat_matrix.
        seat_matrix = [[' Free ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.seats[show_id] = seat_matrix
        StarCinema.seats[show_id] = seat_matrix


    def book_seat(self, desired_show_id, desired_row, desired_column):
        show_exist = False
        for show in self.show_list:
            if show[0] == desired_show_id:
                show_exist = True
                break

        if not show_exist:
            print(f'Show ID {desired_show_id} is invalid. Provide a valid show ID, please.')
        else:
            print(type(desired_row))
            if (desired_row <= 0 or desired_row > self.rows) or (desired_column <= 0 or desired_column > self.columns):
                print(f'Seat at row {desired_row} column {desired_column} is not existed. Please choose a valid seat.')

            elif self.seats[desired_show_id][desired_row][desired_column] != ' Free ':
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
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#Adding some hard coded halls by default, including some shows in each hall.
hall_101 = Hall(12, 20, 101)
hall_101.entry_show('1972', 'The Godfather', '11:00', 101)
hall_101.entry_show('1939', 'Gone with the Wind', '14:00', 101)


hall_102 = Hall(12, 20, 102)
hall_102.entry_show('1942', 'Casablanca', '12:00', 102)
hall_102.entry_show('1994', 'Pulp Fiction', '15:00', 102)


hall_103 = Hall(12, 20, 103)
hall_103.entry_show('1993', 'Schindler\'s List', '13:00', 103)
hall_103.entry_show('1994', 'The Shawshank Redemption', '16:00', 103)


#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

print()
print('Hello. Welcome to Star Cinema Complex.')
while True:
    print()
    print('----- Choose your roll: -----')
    print('', '1. Business Owner/Administrator', '\n', '2. Hall Supervisor', '\n', '3. Counter Manager', '\n', '4. Logout')
    print()
    userInput1 = int(input('Your selection: '))

    if userInput1 == 1:
        print('----- Administrative privileges given:.....')
        while True:
            print()
            print('Choose an option:')
            print('', '1. Create a new hall', '\n', '2. Logout')
            print()
            userInput2 = int(input('Your selection: '))

            if userInput2 == 1:
                previousHallCount = len(StarCinema.hall_list)
                hallNumber = int(input('Choose a hall number: '))

                hall_exists = any(hall.hall_no == hallNumber for hall in StarCinema.hall_list)
                if hall_exists is True:
                    print(f'Hall number {hallNumber} already exists.')

                else:
                    hallRows = int(input('How many rows of seats you want to construct: '))
                    hallColumns = int(input('How many columns of seats you want to construct: '))
                    hallObject = Hall(hallRows, hallColumns, hallNumber)
                    newHallCount = len(StarCinema.hall_list)
                    if previousHallCount + 1 == newHallCount:
                        print(f'Hall {hallNumber} consisting {hallRows} rows and {hallColumns} columns is successful.')
                        print()
                    continue

            elif userInput2 == 2:
                print('Logged out from Administrative privileges.')
                break

            else:
                print('Invalid option. Try again.')


    elif userInput1 == 2:
        print('----- Hall Supervisory privileges given:.....')

        totalHall = len(StarCinema.hall_list)
        if totalHall == 0:
            print('No hall exists. Please get administrative privileges and add a hall.')

        else:
            print('Currently available hall list:')
            for hall in StarCinema.hall_list:
                print(f'Hall ID: {hall.hall_no}: Total available seats: {hall.rows * hall.columns}.')

            chosenHallNumber = int(input('Choose a hall to get the access: '))

            hall_exists = any(hall.hall_no == chosenHallNumber for hall in StarCinema.hall_list)
            if hall_exists is False:
                print(f'Hall number {chosenHallNumber} not exists.')
                continue

            else:
                chosenHallObject = None
                for hall in StarCinema.hall_list:
                    if hall.hall_no == chosenHallNumber:
                        chosenHallObject = hall

                while True:
                    print()
                    print('Choose an option:')
                    print('', '1. Complete show list of this hall', '\n', '2. Enter a new show to this hall', '\n', '3. Available seats of a show', '\n', '4. Book a seat for a show', '\n', '5. Logout')
                    print()
                    userInput3 = int(input('Your selection: '))

                    if userInput3 == 1:
                        print('Complete show list of this hall')
                        for show in StarCinema.show_list:
                            if show[3] == chosenHallNumber:
                                print(f'ID: {show[0]},    Name: {show[1]},      Start Time: {show[2]}')

                    elif userInput3 == 2:
                        show_id = input('Provide show ID: ')
                        show_name = input('Provide show Name: ')
                        show_time = input('Provide show Time: ')
                        chosenHallObject.entry_show(show_id, show_name, show_time, chosenHallNumber)
                        print(
                            f'Show "{show_name}" with ID {show_id} added to Hall {chosenHallObject.hall_no} at {show_time} o\'clock.')

                    elif userInput3 == 3:
                        print('Available seats of a show')
                        show_id = input('Provide show ID: ')
                        print()
                        chosenHallObject.view_available_seats(show_id)

                    elif userInput3 == 4:
                        print('Book a seat for a show')
                        show_id = int(input('Provide show ID: '))
                        desired_row = input('Row of your preferred seat: ')
                        desired_column = input('Column of your preferred seat: ')
                        chosenHallObject.book_seat(show_id, desired_row, desired_column)

                    elif userInput3 == 5:
                        print('Logged out from Hall Supervisory privileges.')
                        break

                    else:
                        print('Invalid option. Try again.')


    elif userInput1 == 3:
        print('Show counter  functions')


    elif userInput1 == 4:
        print('Logged out successfully.')
        sys.exit()


    else:
        print('Invalid option. Try again.')








#-----------------------------------------------------------------------------------------------------------------------
"""
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

#Some more tests and outputs.
print(len(counter.hall_list))
print(len(counter.show_list))

#Accessing the show list and the available seats from the counter.
counter.view_show_list()
counter.view_available_seats(2956)

#Booking a ticket from the counter.
print()
counter.book_ticket(2956, 5, 10)
counter.view_available_seats(2956)

#-----------------------------------------------------------------------------------------------------------------------
"""
