# importing inbuilt functions
import mysql.connector as mysql
from datetime import date, timedelta
from random import randint
import time

# importing files
from colors import bcolors


# global variables
signup = False
login = False
today_date = ''
travel_date = ''
today_time = ''
date_diff = "2"
username = ""
source_city = ""
destination_city = ""
flights = {"Bengaluru_to_Delhi": 9,
           "Bengaluru_to_Kolkata": 10,
           "Bengaluru_to_Mumbai": 11,
           "Bengaluru_to_Chennai": 12,

           "Delhi_to_Kolkata": 7,
           "Delhi_to_Mumbai": 8,
           "Delhi_to_Chennai": 16,
           "Delhi_to_Bengaluru": 15,

           "Kolkata_to_Mumbai": 15,
           "Kolkata_to_Chennai": 18,
           "Kolkata_to_Delhi": 12,
           "Kolkata_to_Bengaluru": 16,

           "Mumbai_to_Chennai": 12,
           "Mumbai_to_Delhi": 13,
           "Mumbai_to_Bengaluru": 17,
           "Mumbai_to_Kolkata": 21,

           "Chennai_to_Bengaluru": 18,
           "Chennai_to_Delhi": 22,
           "Chennai_to_Mumbai": 18,
           "Chennai_to_Kolkata": 0}

percentage = 10
current_user_number = 0

if date_diff == '0':
    percentage = 3
elif date_diff == '1':
    percentage = 5
elif date_diff == '2':
    percentage = 7
else:
    percentage = 10

occupied_seats = list()
all_seats = ["1A", "1F", "2A", "2F", "3A", "3B", "3E", "3F", "4A", "4B", "4E", "4F", "5A", "5B", "5E", "5F",
             "6A", "6B", "6C", "6D", "6E", "6F", "7A", "7B", "7C", "7D", "7E", "7F", "8A", "8B", "8C", "8D", "8E", "8F",
             "9A", "9B", "9C", "9D", "9E", "9F", "10A", "10B", "10C", "10D", "10E", "10F",
             "11A", "11B", "11C", "11D", "11E", "11F"]

# declaring global variables to accept the seat from the user --------------------------------------------
number_of_seats_booked = 0
users_seat = list("")
all_seats_index = 0
terminator = 0
name = list()
email = list()
phone_number = list()
current_user_number = 0

for i in range(0, len(all_seats)):
    x = randint(0, 10)
    if 0 < x < percentage:
        occupied_seats.append(False)
    else:
        occupied_seats.append(True)

occupied = 0
vacant = 0
for i in range(0, len(occupied_seats)):
    if occupied_seats[i]:
        occupied = occupied + 1
    else:
        vacant = vacant + 1
print("vacant: ", vacant)
print("occupied: ", occupied)


# __user defined functions__
'''display_welcome():
user defined function to display welcome'''


def display_welcome():
    # displaying the welcome sign
    print(" *       *   * * * *   *         * * *    * * * *    *     *   * * * * ")
    print(" *       *   *         *        *        *       *   * * * *   *       ")
    print(" *   *   *   * * * *   *       *        *         *  *  *  *   * * * * ")
    print(" * *   * *   *         *        *        *       *   *     *   *       ")
    print(" *       *   * * * *   * * * *   * * *    * * * *    *     *   * * * * ")
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
    global username
    global signup

    # reading usernames and storing them in l
    sql_cursor.execute("SELECT * FROM USERS")
    data = sql_cursor.fetchall()
    username_list = list()
    for k in range(0, len(data)):
        username_list.append(data[k][1])

    # reading name from the user
    while True:
        username = input("please enter your desired username: ")
        if username in username_list:
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
    s = f"insert into users values('{users_name}', '{username}', '{password}', '{users_email}', {str_number})"
    sql_cursor.execute(s)
    sql_mycon.commit()
    signup = True


'''
login_user(cursor):
user defined function for logging in
accepting the values of username and the password to then verify with those in the database'''


def login_user(sql_cursor):
    global username
    global login

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
        username = input(f"Please Enter your {bcolors.BOLD}Username:{bcolors.ENDC} ")
        if username not in username_list:
            print(f"{bcolors.FAIL}Invalid username{bcolors.ENDC}")
        else:
            user_index = username_list.index(username)
            user_password = input(f"Please Enter your {bcolors.BOLD}Password:{bcolors.ENDC} ")
            if user_password != password_list[user_index]:
                print(f"{bcolors.FAIL}Invalid Password{bcolors.ENDC}")
            else:
                print(f"\n{bcolors.UNDERLINE}{bcolors.OKBLUE}{bcolors.BOLD}Welcome to you Air servers account"
                      f"{bcolors.ENDC}{bcolors.ENDC}{bcolors.BOLD}\n")
                break

    login = True


'''
show_booked_flights():
this user defined function accepts the username, from -> to and date of travel and checks the database to see if there 
is a matching record for the same and then displays the record
'''


def show_booked_flights(mysql_cursor):
    global username

    date_of_flight = input("Please enter the date of the flight: ")
    source_of_travel = input("Source: ")
    destination_of_travel = input("Destination: ")
    s = f'select * from booked_flight_details where username = "{username}" and' \
        f' source_of_travel = "{source_of_travel}" and destination_of_travel = "{destination_of_travel}" and' \
        f' date_of_travel = "{date_of_flight}"'
    mysql_cursor.execute(s)
    y = mysql_cursor.fetchall()

    print()
    if len(y) == 0:
        print(f'There are no seats booked under your {bcolors.OKCYAN}username: {username}{bcolors.ENDC} '
              f'from {bcolors.OKCYAN}{source_of_travel}{bcolors.ENDC} to'
              f' {bcolors.OKCYAN}{destination_of_travel}{bcolors.ENDC} on'
              f' {bcolors.OKCYAN}{date_of_flight}{bcolors.ENDC}')
    else:
        for k in range(0, len(y)):
            current_user = y[k]
            print(f'{bcolors.HEADER}username:{bcolors.ENDC} {current_user[0]} \n'
                  f'{bcolors.HEADER}source of travel:{bcolors.ENDC} {current_user[1]} \n'
                  f'{bcolors.HEADER}destination of travel:{bcolors.ENDC} {current_user[2]} \n'
                  f'{bcolors.HEADER}date of travel:{bcolors.ENDC} {current_user[3]} \n'
                  f'{bcolors.HEADER}booking name:{bcolors.ENDC} {current_user[4]} \n'
                  f'{bcolors.HEADER}seat booked:{bcolors.ENDC} {current_user[5]} \n'
                  f'{bcolors.HEADER}phone number:{bcolors.ENDC} {current_user[6]} \n'
                  f'{bcolors.HEADER}email: {bcolors.ENDC}{current_user[7]} \n')


'''
choose_city():
user defined function to choose the source and destination cities from the user
A meny is displayed for the source city, this value is stored in a variable and the remaining cities are displayed as
the destination cities in the form of a menu. The choice is stored in a variable and is returned to the function call'''


def choose_city():
    global source_city
    global destination_city

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


def date_choice(source_destination_pair):
    global flights
    global date_diff
    global travel_date, today_date, today_time

    # getting current time from the users computer
    from datetime import datetime
    today_time = datetime.now().strftime("%H:%M")  # getting today's time and formatting it

    # getting current date from the users computer
    today_date = date.today()

    # reading the date of the flight from the user
    dt, mt, yt = [int(k) for k in input("Enter Travel Date (dd/mm/yyyy): ").split('/')]

    try:
        travel_date = date(yt, mt, dt)
        s = str(travel_date - today_date)
        date_diff = s.split()[0]

        if int(date_diff) < 0:
            print("Date Has passed")

        elif date_diff == "0:00:00":
            # find difference between the users time and the time of the flight
            hour = today_time.split(":")[0]
            if (flights[source_destination_pair] - int(hour)) <= 2:
                print("INVALID FLIGHT TIMINGS")
                reschedule_flight = input("Would you like to book the same flight for tomorrow. Type Yes to confirm")
                if reschedule_flight == "Yes":
                    tomorrow_date = date.today() + timedelta(1)
                    tomorrow_date = tomorrow_date.strftime('%d-%m-%Y')

                    final_key = source_destination_pair.split("_")
                    source_of_travel = final_key[0]
                    destination_of_travel = final_key[2]
                    print(f'Your flight is from {bcolors.HEADER}{source_of_travel}{bcolors.ENDC} to'
                          f' {bcolors.HEADER}{destination_of_travel}{bcolors.ENDC} on '
                          f'{bcolors.HEADER}{tomorrow_date}{bcolors.ENDC} at '
                          f'{bcolors.HEADER}{flights[source_destination_pair]}:00 hrs{bcolors.ENDC}')
                    return tomorrow_date

        elif int(date_diff) <= 3:
            final_key = source_destination_pair.split("_")
            source_of_travel = final_key[0]
            destination_of_travel = final_key[2]
            print(f'Your flight is from {bcolors.HEADER}{source_of_travel}{bcolors.ENDC} to'
                  f' {bcolors.HEADER}{destination_of_travel}{bcolors.ENDC} on '
                  f'{bcolors.HEADER}{travel_date}{bcolors.ENDC} at '
                  f'{bcolors.HEADER}{flights[source_destination_pair]}:00 hrs{bcolors.ENDC}')
            return travel_date

        else:
            print(f"Reservations not available for {travel_date}")

    except ValueError:
        print("INVALID DATE")


'''
display_aeroplane_seat():
Based on the date of travel and time of travel a unique airplane layout is created for the user and is displayed 
using the display_aeroplane_seat() function

the proper formatting of the display is done by this function including adding red color to the seats that have already 
been booked and green colour to the seats that are yet to be booked'''


def display_aeroplane_seat():
    # global variables
    global occupied_seats
    global all_seats

    # displaying First Class
    print("              " + f"{bcolors.BOLD}First Class{bcolors.ENDC}" + "              ")

    for k in range(0, 4):
        # displaying 1A and 2A with colour code
        if occupied_seats[k] and (k == 0 or k == 2):
            print("▢ " + f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}" + "                             ", end="")
        elif not occupied_seats[k] and (k == 0 or k == 2):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}" + "                             ", end="")

        # displaying 1F and 2F with colour code
        if occupied_seats[k] and (k == 1 or k == 3):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[k] and (k == 1 or k == 3):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")

    # displaying Business Class
    print("             " + f"{bcolors.BOLD}Business Class{bcolors.ENDC}" + "           ")

    for k in range(4, 16):
        # displaying 3A, 4A and 5A with colour code
        if occupied_seats[k] and (k == 4 or k == 8 or k == 12):
            print("▢ " + f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[k] and (k == 4 or k == 8 or k == 12):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 3B, 4B and 5B with colour coding
        if occupied_seats[k] and (k == 5 or k == 9 or k == 13):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="                   ")
        elif not occupied_seats[k] and (k == 5 or k == 9 or k == 13):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="                   ")

        # displaying 3E, 4E and 5E with colour coding
        if occupied_seats[k] and (k == 6 or k == 10 or k == 14):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[k] and (k == 6 or k == 10 or k == 14):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 3F, 4F and 5F with colour coding
        if occupied_seats[k] and (k == 7 or k == 11 or k == 15):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[k] and (k == 7 or k == 11 or k == 15):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")

    # displaying Economy Class
    print("             " + f"{bcolors.BOLD}Economy Class{bcolors.ENDC}" + "            ")

    for k in range(16, 52):
        # displaying 6A, 7A, 8A and 9A with colour code
        if occupied_seats[k] and (k == 16 or k == 22 or k == 28 or k == 34):
            print("▢ " + f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[k] and (k == 16 or k == 22 or k == 28 or k == 34):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 6B, 7B, 8B and 9B with colour code
        if occupied_seats[k] and (k == 17 or k == 23 or k == 29 or k == 35):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[k] and (k == 17 or k == 23 or k == 29 or k == 35):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 6C, 7C, 8C and 9C with colour code
        if occupied_seats[k] and (k == 18 or k == 24 or k == 30 or k == 36):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="         ")
        elif not occupied_seats[k] and (k == 18 or k == 24 or k == 30 or k == 36):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="         ")

        # displaying 6D, 7D, 8D and 9D with colour coding
        if occupied_seats[k] and (k == 19 or k == 25 or k == 31 or k == 37):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[k] and (k == 19 or k == 25 or k == 31 or k == 37):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 6E, 7E, 8E and 9E with colour coding
        if occupied_seats[k] and (k == 20 or k == 26 or k == 32 or k == 38):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[k] and (k == 20 or k == 26 or k == 32 or k == 38):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 6F, 7F, 8F and 9F with colour coding
        if occupied_seats[k] and (k == 21 or k == 27 or k == 33 or k == 39):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[k] and (k == 21 or k == 27 or k == 33 or k == 39):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")

    for k in range(40, 52):
        # displaying 10A and 11A with colour code
        if occupied_seats[k] and (k == 40 or k == 46):
            print("▢ " + f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="   ")
        elif not occupied_seats[k] and (k == 40 or k == 46):
            print("▢ " + f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="   ")

        # displaying 6B, 7B, 8B and 9B with colour code
        if occupied_seats[k] and (k == 41 or k == 47):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats[k] and (k == 41 or k == 47):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="  ")

        # displaying 6C, 7C, 8C and 9C with colour code
        if occupied_seats[k] and (k == 42 or k == 48):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="      ")
        elif not occupied_seats[k] and (k == 42 or k == 48):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="      ")

        # displaying 6D, 7D, 8D and 9D with colour coding
        if occupied_seats[k] and (k == 43 or k == 49):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats[k] and (k == 43 or k == 49):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="  ")

        # displaying 6E, 7E, 8E and 9E with colour coding
        if occupied_seats[k] and (k == 44 or k == 50):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}", end="  ")
        elif not occupied_seats[k] and (k == 44 or k == 50):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}", end="  ")

        # displaying 6F, 7F, 8F and 9F with colour coding
        if occupied_seats[k] and (k == 45 or k == 51):
            print(f"{bcolors.WARNING}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")
        elif not occupied_seats[k] and (k == 45 or k == 51):
            print(f"{bcolors.OKGREEN}{all_seats[k]}{bcolors.ENDC}" + " ▢", end="\n")

    accept_users_seat()


"""
accept_users_seat():
accepts the seat that user wants to book and changes the reservation status of that seat (colour) in display
"""


def accept_users_seat():  # accepting the users seat number ---------------------------------------------------
    global username, number_of_seats_booked, users_seat, all_seats_index,\
        occupied_seats, terminator, name, email,\
        phone_number, current_user_number

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

            # printing 40 lines of space:
            time.sleep(2)
            print("\n" * 40)

        if current_user_number <= terminator:
            display_aeroplane_seat()
        else:
            break


# __main__
# python, mysql connectivity
mycon = mysql.connect(host="localhost", user="root", port='3306', password="Akshat@2005", database="class12project")
cursor = mycon.cursor()

# displaying welcome message to the user and prompting for signup and login
while True:
    display_welcome()
    choice = int(input(f'{bcolors.OKBLUE}Please enter your choice: {bcolors.ENDC}'))
    if choice == 1:
        create_user(mycon, cursor)
    elif choice == 2:
        login_user(cursor)
        break
    else:
        print(f'{bcolors.FAIL}INVALID CHOICE{bcolors.ENDC}')

# menu for Booking a flight and checking for booked flights
if login:
    print(f"{bcolors.WARNING}[1]{bcolors.ENDC} {bcolors.HEADER}BOOK A FLIGHT{bcolors.ENDC}\n"
          f"{bcolors.WARNING}[2]{bcolors.ENDC} {bcolors.HEADER}SEE BOOKED FLIGHTS{bcolors.ENDC}\n")
    c = input()
    if c == '1':
        source_city, destination_city = choose_city()
        key = source_city + "_to_" + destination_city
        date_choice(key)
    elif c == '2':
        show_booked_flights(cursor)
        # i need to use a goto here to take this back to the beginning of the menu (book flight and see booked flights)
elif signup:
    print(f'{bcolors.HEADER}BOOK A FLIGHT{bcolors.ENDC}')
    source_city, destination_city = choose_city()
    key = source_city + "_to_" + destination_city
    date_choice(key)


total_number_of_seats = input("Total number of reservations: ")
available_number_of_seats = 0

for i in range(0, len(occupied_seats)):  # finding the available number of seats
    if occupied_seats[i]:
        available_number_of_seats += 1
while True:
    if int(total_number_of_seats) == 0:
        total_number_of_seats = input(f"{bcolors.WARNING}ZERO? Please enter the proper value: {bcolors.ENDC}")
    elif 0 >= int(total_number_of_seats):
        total_number_of_seats = input(f"{bcolors.WARNING}You have entered a negative value... Please enter the "
                                      f"number of reservations as a positive value: {bcolors.ENDC}")
    elif int(total_number_of_seats) >= available_number_of_seats:
        total_number_of_seats = input(f"{bcolors.WARNING}We don't have that many seats available... "
                                      f"Please enter a lower value: {bcolors.ENDC}")
    else:
        break

# declaring the value of terminator
terminator = int(total_number_of_seats)
terminator = terminator - 1
display_aeroplane_seat()

# inserting the information into the database
print("username: ", username)
print("source of travel: ", source_city)
print("destination of travel: ", destination_city)
print("date of travel: ", travel_date)
print("booking name: ", name)
print("seat booked: ", users_seat)
print("phone number: ", phone_number)
print("email: ", email)

for i in range(0, len(name)):
    n = name[i]
    u = users_seat[i]
    p = phone_number[i]
    e = email[i]
    insert_string = f"insert into booked_flight_details values('{username}', '{source_city}', '{destination_city}'," \
                    f" '{travel_date}', '{n}', '{u}', {p}, '{e}', NULL)"
    cursor.execute(insert_string)
    mycon.commit()
