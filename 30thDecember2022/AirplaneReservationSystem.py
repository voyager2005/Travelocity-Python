# importing inbuilt functions
from datetime import date, timedelta
import time

# importing files
from colors import bcolors
from HotelRoomReservation import hotel_room_reservation
from Subway import add_bread


# __user defined functions__
'''display_welcome():
user defined function to display welcome'''


def display_welcome():
    # displaying the welcome sign
    print(f"{bcolors.HEADER} *       *   * * * *   *         * * *    * * * *    *     *   * * * * {bcolors.ENDC}")
    print(f"{bcolors.HEADER} *       *   *         *        *        *       *   * * * *   *       {bcolors.ENDC}")
    print(f"{bcolors.HEADER} *   *   *   * * * *   *       *        *         *  *  *  *   * * * * {bcolors.ENDC}")
    print(f"{bcolors.HEADER} * *   * *   *         *        *        *       *   *     *   *       {bcolors.ENDC}")
    print(f"{bcolors.HEADER} *       *   * * * *   * * * *   * * *    * * * *    *     *   * * * * {bcolors.ENDC}")
    print('\n\n')

    # menu for login and signup
    print(f"{bcolors.OKGREEN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}~                         LOGIN OPTIONS                               ~{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}~                          1. SIGN UP                                 ~{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}~                           2. LOGIN                                  ~{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{bcolors.ENDC}")


'''
create_user(mycon, cursor):
user defined function to accept information such as
1. username
2. name
3. password for the account being created
4. email address
5. phone number , etc 
to store them into the database 
'''


def create_user(sql_mycon, sql_cursor):
    # reading usernames and storing them in l
    sql_cursor.execute("SELECT * FROM USERS")
    data = sql_cursor.fetchall()
    username_list = list()
    for k in range(0, len(data)):
        username_list.append(data[k][1])

    # reading name from the user
    while True:
        username_of_user = input("please enter your desired username: ")
        if username_of_user in username_list:
            print(f'{bcolors.FAIL}username already taken{bcolors.ENDC}')
            continue
        else:
            break
    while True:
        users_name = input("Please enter your name: ")
        if len(users_name) > 20 or len(users_name) == 0:
            print(f'{bcolors.FAIL}name should be less than 20 characters long{bcolors.ENDC}')
            continue
        else:
            break

    # Reading the password from the user
    while True:
        password = input("Create password\nPlease enter your password: ")
        if password != input("Please confirm the password: "):
            continue
        else:
            break

    # Reading the email address from the user
    while True:
        users_email = input("Please enter your email id: ")
        if "@" not in users_email:
            print(f'{bcolors.FAIL}invalid email{bcolors.ENDC}')
        else:
            break

    # Reading the phone number from the user
    while True:
        str_number = input("Please enter your phone number: ")
        if len(str_number) != 10:
            print(f'{bcolors.FAIL}invalid phone number{bcolors.ENDC}')
        else:
            break

    # inserting all the values given by the user into the table <users> in <class12project> database
    s = f"insert into users values('{users_name}', '{username_of_user}', '{password}', '{users_email}', {str_number})"
    sql_cursor.execute(s)
    sql_mycon.commit()

    signup = True
    return username_of_user, signup


'''
login_user(cursor):
user defined function for logging in
accepting the values of username and the password to then verify with those in the database'''


def login_user(sql_cursor):
    sql_cursor.execute("SELECT * FROM USERS")
    data = sql_cursor.fetchall()

    # fetching all the usernames stored in the database
    username_list = list()
    for k in range(0, len(data)):
        username_list.append(data[k][1])

    # fetching all the passwords corresponding to the usernames in the database
    password_list = list()
    for k in range(0, len(data)):
        password_list.append(data[k][2])

    # check weather the username and password match the records (login condition)
    while True:
        username_of_user = input(f"Please Enter your {bcolors.BOLD}Username:{bcolors.ENDC} ")
        if username_of_user not in username_list:
            print(f"{bcolors.FAIL}Invalid username{bcolors.ENDC}")
        else:
            user_index = username_list.index(username_of_user)
            user_password = input(f"Please Enter your {bcolors.BOLD}Password:{bcolors.ENDC} ")
            if user_password != password_list[user_index]:
                print(f"{bcolors.FAIL}Invalid Password{bcolors.ENDC}")
            else:
                print(f"\n{bcolors.UNDERLINE}{bcolors.OKBLUE}{bcolors.BOLD}Welcome to you Air servers account"
                      f"{bcolors.ENDC}{bcolors.ENDC}{bcolors.BOLD}\n")
                break

    login = True
    return username_of_user, login


'''
show_booked_flights():
this user defined function accepts the username, from -> to and date of travel and checks the database to see if there 
is a matching record for the same and then displays the record
'''


def show_booked_flights(mysql_cursor, username_of_user):
    # display statement
    date_of_flight = input("Please enter the date of the flight: ")  # reading the date of travel from the user
    source_of_travel = input("Source: ")  # reading the source of travel from the user
    destination_of_travel = input("Destination: ")  # reading the destination of travel from the user
    s = f'select * from booked_flight_details where username = "{username_of_user}" and' \
        f' source_of_travel = "{source_of_travel}" and destination_of_travel = "{destination_of_travel}" and' \
        f' date_of_travel = "{date_of_flight}"'
    mysql_cursor.execute(s)
    y = mysql_cursor.fetchall()

    print()
    if len(y) == 0:
        print(f'There are no seats booked under your {bcolors.OKCYAN}username: {username_of_user}{bcolors.ENDC} '
              f'from {bcolors.OKCYAN}{source_of_travel}{bcolors.ENDC} to'
              f' {bcolors.OKCYAN}{destination_of_travel}{bcolors.ENDC} on'
              f' {bcolors.OKCYAN}{date_of_flight}{bcolors.ENDC}')
    else:
        for k in range(0, len(y)):
            current_user = y[k]
            # displaying the booked seats for the specific date and source and destination
            print(f'{bcolors.HEADER}username:{bcolors.ENDC} {current_user[0]} \n'
                  f'{bcolors.HEADER}source of travel:{bcolors.ENDC} {current_user[1]} \n'
                  f'{bcolors.HEADER}destination of travel:{bcolors.ENDC} {current_user[2]} \n'
                  f'{bcolors.HEADER}date of travel:{bcolors.ENDC} {current_user[3]} \n'
                  f'{bcolors.HEADER}booking name:{bcolors.ENDC} {current_user[4]} \n'
                  f'{bcolors.HEADER}seat booked:{bcolors.ENDC} {current_user[5]} \n'
                  f'{bcolors.HEADER}phone number:{bcolors.ENDC} {current_user[6]} \n'
                  f'{bcolors.HEADER}email: {bcolors.ENDC}{current_user[7]} \n'
                  f'{bcolors.HEADER}room booked:{bcolors.ENDC} {current_user[9]}\n', end='')

            if current_user[9] != "NO ROOM BOOKED":
                print(f'{bcolors.HEADER}cost of room: {bcolors.ENDC}{current_user[10]} \n', end='')

            print(f'{bcolors.HEADER}Food ordered: {bcolors.ENDC}{current_user[11]} \n', end='')

            if current_user[11] != 'NO FOOD ORDERED':
                print(f'{bcolors.HEADER}cost of food: {bcolors.ENDC}{current_user[12]} \n', end='')


'''
choose_city():
user defined function to choose the source and destination cities from the user
A meny is displayed for the source city, this value is stored in a variable and the remaining cities are displayed as
the destination cities in the form of a menu. The choice is stored in a variable and is returned to the function call'''


def choose_city():
    city_list = ["Bengaluru", "Mumbai", "Kolkata", "Chennai", "Delhi"]

    # displaying all the cities we fly from
    print(f'                      {bcolors.OKCYAN}THE CITIES WE FLY FROM{bcolors.ENDC}')
    print_string = ''
    for j in range(0, 5):
        for k in range(0, 71 - len(city_list[j])):
            if k < 25:
                print_string = print_string + ' '
            elif k == 25:
                print_string = print_string + str(j+1) + ". " + city_list[j]
        print_string = print_string + '\n'
    print(print_string)

    # Reading the source city from the user
    while True:
        source_city_num = int(input("Enter the source city of your choice: "))
        if source_city_num not in [1, 2, 3, 4, 5]:
            print(f'{bcolors.FAIL}invalid choice{bcolors.ENDC}')
        else:
            source_of_travel = city_list[source_city_num - 1]
            city_list.remove(source_of_travel)
            print(f"The Source of your flight is {bcolors.HEADER}{source_of_travel}{bcolors.ENDC}")
            break
    print()

    # displaying all the destinations we fly to
    print_string = ""
    print(f'                   {bcolors.OKCYAN}THE DESTINATIONS WE FLY TO{bcolors.ENDC}')
    for j in range(0, 4):
        for k in range(0, 71 - len(city_list[j])):
            if k < 25:
                print_string = print_string + ' '
            elif k == 25:
                print_string = print_string + str(j+1) + ". " + city_list[j]
        print_string = print_string + '\n'
    print(print_string)

    # Reading the destination city from the user
    while True:
        destination_city_num = int(input("Enter the destination of your choice: "))
        if destination_city_num not in [1, 2, 3, 4]:
            print(f'{bcolors.FAIL}invalid choice{bcolors.ENDC}')
        else:
            destination_of_travel = city_list[destination_city_num - 1]
            city_list.remove(destination_of_travel)
            print(f"The Destination of your flight is {bcolors.HEADER}{destination_of_travel}{bcolors.ENDC}")
            break
    print()

    # returning the source city and the destination city to the function call
    return source_of_travel, destination_of_travel


'''
date_choice(key):
user defined function to accept the date of travel from the user
various checks are help on the date passed to make sure that this date is in proper formatting, 
ie. that there is no value of date exceeding these dates 28/29/30/31 based on the month of travel
the month of travel is not > 12 
and the date of travel is not from the past

The value of time of travel is also accepted from the user and similar checks are help on that'''


def date_choice(source_destination_pair, flights):
    from datetime import datetime
    today_time = datetime.now().strftime("%H:%M")  # getting today's time and formatting it

    # getting current date from the users computer
    today_date = date.today()

    # reading the date of the flight from the user
    dt, mt, yt = [int(k) for k in input("Enter Travel Date (dd/mm/yyyy): ").split('/')]
    date_diff = ''
    travel_date = date(yt, mt, dt)

    try:
        travel_date = date(yt, mt, dt)
        s = str(travel_date - today_date)
        date_diff = s.split()[0]

        if date_diff == "0:00:00":
            # find difference between the users time and the time of the flight
            hour = today_time.split(":")[0]
            if (flights[source_destination_pair] - int(hour)) <= 2:
                print("INVALID FLIGHT TIMINGS")
                reschedule_flight = input("Would you like to book the same flight for tomorrow. Type Yes to confirm")
                if reschedule_flight.lower() == "yes":
                    tomorrow_date = date.today() + timedelta(1)
                    tomorrow_date = tomorrow_date.strftime('%d-%m-%Y')

                    final_key = source_destination_pair.split("_")
                    source_of_travel = final_key[0]
                    destination_of_travel = final_key[2]
                    print(f'Your flight is from {bcolors.HEADER}{source_of_travel}{bcolors.ENDC} to'
                          f' {bcolors.HEADER}{destination_of_travel}{bcolors.ENDC} on '
                          f'{bcolors.HEADER}{tomorrow_date}{bcolors.ENDC} at '
                          f'{bcolors.HEADER}{flights[source_destination_pair]}:00 hrs{bcolors.ENDC}')
                else:
                    print(f"{bcolors.FAIL}terminated{bcolors.ENDC}")

        elif int(date_diff) < 0:
            print("Date Has passed")

        elif int(date_diff) <= 3:
            final_key = source_destination_pair.split("_")
            source_of_travel = final_key[0]
            destination_of_travel = final_key[2]
            print(f'Your flight is from {bcolors.HEADER}{source_of_travel}{bcolors.ENDC} to'
                  f' {bcolors.HEADER}{destination_of_travel}{bcolors.ENDC} on '
                  f'{bcolors.HEADER}{travel_date}{bcolors.ENDC} at '
                  f'{bcolors.HEADER}{flights[source_destination_pair]}:00 hrs{bcolors.ENDC}')

        else:
            print(f"Reservations not available for {travel_date}")

    except ValueError:
        print("INVALID DATE")

    return date_diff, str(travel_date)


'''
display_aeroplane_seat():
Based on the date of travel and time of travel a unique airplane layout is created for the user and is displayed 
using the display_aeroplane_seat() function

the proper formatting of the display is done by this function including adding red color to the seats that have already 
been booked and green colour to the seats that are yet to be booked'''


def display_aeroplane_seat(occupied_seats_2, all_seats):
    # displaying First Class
    print("              " + f"{bcolors.BOLD}First Class{bcolors.ENDC}" + "              ")

    for k in range(0, 4):
        # displaying 1A and 2A with colour code
        if occupied_seats_2[k] and (k == 0 or k == 2):
            print("▢ " + f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}" + "                             ", end="")
        elif not occupied_seats_2[k] and (k == 0 or k == 2):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}" + "                             ", end="")

        # displaying 1F and 2F with colour code
        if occupied_seats_2[k] and (k == 1 or k == 3):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats_2[k] and (k == 1 or k == 3):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")

    # displaying Business Class
    print("             " + f"{bcolors.BOLD}Business Class{bcolors.ENDC}" + "           ")

    for k in range(4, 16):
        # displaying 3A, 4A and 5A with colour code
        if occupied_seats_2[k] and (k == 4 or k == 8 or k == 12):
            print("▢ " + f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats_2[k] and (k == 4 or k == 8 or k == 12):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 3B, 4B and 5B with colour coding
        if occupied_seats_2[k] and (k == 5 or k == 9 or k == 13):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="                   ")
        elif not occupied_seats_2[k] and (k == 5 or k == 9 or k == 13):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="                   ")

        # displaying 3E, 4E and 5E with colour coding
        if occupied_seats_2[k] and (k == 6 or k == 10 or k == 14):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats_2[k] and (k == 6 or k == 10 or k == 14):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 3F, 4F and 5F with colour coding
        if occupied_seats_2[k] and (k == 7 or k == 11 or k == 15):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats_2[k] and (k == 7 or k == 11 or k == 15):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")

    # displaying Economy Class
    print("             " + f"{bcolors.BOLD}Economy Class{bcolors.ENDC}" + "            ")

    for k in range(16, 52):
        # displaying 6A, 7A, 8A and 9A with colour code
        if occupied_seats_2[k] and (k == 16 or k == 22 or k == 28 or k == 34):
            print("▢ " + f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats_2[k] and (k == 16 or k == 22 or k == 28 or k == 34):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 6B, 7B, 8B and 9B with colour code
        if occupied_seats_2[k] and (k == 17 or k == 23 or k == 29 or k == 35):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats_2[k] and (k == 17 or k == 23 or k == 29 or k == 35):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 6C, 7C, 8C and 9C with colour code
        if occupied_seats_2[k] and (k == 18 or k == 24 or k == 30 or k == 36):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="         ")
        elif not occupied_seats_2[k] and (k == 18 or k == 24 or k == 30 or k == 36):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="         ")

        # displaying 6D, 7D, 8D and 9D with colour coding
        if occupied_seats_2[k] and (k == 19 or k == 25 or k == 31 or k == 37):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats_2[k] and (k == 19 or k == 25 or k == 31 or k == 37):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 6E, 7E, 8E and 9E with colour coding
        if occupied_seats_2[k] and (k == 20 or k == 26 or k == 32 or k == 38):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats_2[k] and (k == 20 or k == 26 or k == 32 or k == 38):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 6F, 7F, 8F and 9F with colour coding
        if occupied_seats_2[k] and (k == 21 or k == 27 or k == 33 or k == 39):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats_2[k] and (k == 21 or k == 27 or k == 33 or k == 39):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")

    for k in range(40, 52):
        # displaying 10A and 11A with colour code
        if occupied_seats_2[k] and (k == 40 or k == 46):
            print("▢ " + f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats_2[k] and (k == 40 or k == 46):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 6B, 7B, 8B and 9B with colour code
        if occupied_seats_2[k] and (k == 41 or k == 47):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats_2[k] and (k == 41 or k == 47):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="  ")

        # displaying 6C, 7C, 8C and 9C with colour code
        if occupied_seats_2[k] and (k == 42 or k == 48):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="      ")
        elif not occupied_seats_2[k] and (k == 42 or k == 48):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="      ")

        # displaying 6D, 7D, 8D and 9D with colour coding
        if occupied_seats_2[k] and (k == 43 or k == 49):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats_2[k] and (k == 43 or k == 49):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="  ")

        # displaying 6E, 7E, 8E and 9E with colour coding
        if occupied_seats_2[k] and (k == 44 or k == 50):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats_2[k] and (k == 44 or k == 50):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="  ")

        # displaying 6F, 7F, 8F and 9F with colour coding
        if occupied_seats_2[k] and (k == 45 or k == 51):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats_2[k] and (k == 45 or k == 51):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")


"""
accept_users_seat():
accepts the seat that user wants to book and changes the reservation status of that seat (colour) in display
"""


def accept_users_seat(number_of_seats_booked, users_seat, all_seats_index,
                      occupied_seats, terminator, name, email, phone_number, current_user_number, all_seats,
                      room, room_cost, room_choice,
                      food, food_list, food_cost):
    while True:
        if current_user_number <= terminator:
            # accepting the name of the user ----------------------------------------------------------------
            name.append(input("Your name please: "))  # accepting the users name
            name[current_user_number].strip()  # removing unwanted spaces before and after the name
            name[current_user_number] = name[current_user_number].title()

            # accepting the phone number of the user --------------------------------------------------------
            s = input("Enter your phone number: ")

            while True:
                if not s.isdigit():
                    s = input(f"{bcolors.WARNING}Looks like your phone number has alphabets... "
                              f"Please enter the correct value: {bcolors.ENDC}")
                else:
                    break

            while len(s) != 10:
                print("Please make sure that the phone number that you have entered is 10 digits long")
                print("The phone number you entered was " + str(len(s)) + " digits long ")
                s = input("Please enter the phone number: ")

            phone_number.append(int(s))

            # Reading the email address from the user
            s = input("Please enter your email id: ")
            while True:
                if "@" not in s:
                    print(f'{bcolors.FAIL}invalid email{bcolors.ENDC}')
                    s = input("Please enter your email id: ")
                else:
                    break
            email.append(s)

            # accepting users seat
            users_seat.append(input(f"{bcolors.BOLD}Please enter the seat that you want to book: {bcolors.ENDC}"))

            # finding index of all seats
            for j in range(0, len(all_seats)):
                if all_seats[j] == users_seat[number_of_seats_booked]:
                    all_seats_index = j

            if occupied_seats[all_seats_index]:
                print(f"{bcolors.WARNING}{bcolors.BOLD}That seat has already been booked/reserved"
                      f"{bcolors.ENDC}{bcolors.ENDC}")
                continue
            elif not occupied_seats[all_seats_index]:
                occupied_seats[all_seats_index] = True
                number_of_seats_booked += 1
                print(
                    f"{bcolors.OKCYAN}Your seat {users_seat[number_of_seats_booked - 1]} has been booked{bcolors.ENDC}")
                current_user_number = current_user_number + 1

            # START OF HOTEL ROOM RESERVATION
            check = input(f'{bcolors.HEADER}Do you want to book a hotel room? {bcolors.ENDC}'
                          f'{bcolors.FAIL}yes/no{bcolors.ENDC}: ').lower().strip()

            if check == 'yes':
                a, b = hotel_room_reservation()
                room.append(True)
                room_choice.append(a)
                room_cost.append(b)
            else:
                room.append(False)  # END OF HOTEL ROOM RESERVATION

            # START OF SUBWAY (FOOD)
            check = input(f'{bcolors.HEADER}Do you want preorder your meal {bcolors.ENDC}'
                          f'{bcolors.FAIL}yes/no{bcolors.ENDC}: ').lower().strip()
            if check == 'yes':
                a, b = add_bread()
                food.append(True)
                food_list.append(a)
                food_cost.append(b)
            else:
                food.append(False)  # END OF SUBWAY (FOOD

            # printing 40 lines of space:
            time.sleep(2)
            print("\n" * 40)

        if current_user_number <= terminator:
            display_aeroplane_seat(occupied_seats, all_seats)
        else:
            break
