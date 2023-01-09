import mysql.connector as mysql

from AirplaneReservationSystem import *
from Subway import *

'''
declaring global variables of Airplane Seat Reservation ---------------------------------------------------------------
'''
signup = False
login = False
book_a_flight = False
today_date = ''
travel_date = ''
today_time = ''
username = ""
key = ''
source_city = ""
destination_city = ""
date_diff = ''
travel_date_string = ''
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

'''
GLOBAL VARIABLES OF SUBWAY ------------------------------------------------------------------------------------------
'''
food_list = list()
food_cost = list()
food = list()

'''
GLOBAL VARIABLES OF HOTEL ROOM RESERVATION ---------------------------------------------------------------------------
'''
single_bed = [1, 2, 3, 4, 5]
double_bed = [6, 7, 8, 9, 10]
cost_hotel_room_reservation = 0.0
room_choice = list()
room_cost = list()
room = list()

'''
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
                                                  M A I N 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
'''
# python, mysql connectivity
mycon = mysql.connect(host="localhost", user="root", port='3306', password="Akshat@2005", database="class12project")
cursor = mycon.cursor()

mycon_flights = mysql.connect(host="localhost", user="root", port='3306', password="Akshat@2005", database="flights")
cursor_flights = mycon_flights.cursor()

# displaying welcome message to the user and prompting for signup and login
while True:
    display_welcome()
    choice = int(input(f'{bcolors.OKBLUE}Please enter your choice: {bcolors.ENDC}'))
    if choice == 1:
        username, signup = create_user(mycon, cursor)
        break
    elif choice == 2:
        username, login = login_user(cursor)
        break
    else:
        print(f'{bcolors.FAIL}INVALID CHOICE{bcolors.ENDC}')

# menu for Booking a flight and checking for booked flights when the user has logged in
if login:
    print(f"{bcolors.WARNING}[1]{bcolors.ENDC} {bcolors.HEADER}BOOK A FLIGHT{bcolors.ENDC}\n"
          f"{bcolors.WARNING}[2]{bcolors.ENDC} {bcolors.HEADER}SEE BOOKED FLIGHTS{bcolors.ENDC}\n")
    c = input()
    if c == '1':
        book_a_flight = True
        source_city, destination_city = choose_city()
        key = source_city + "_to_" + destination_city
        date_diff, travel_date_string = date_choice(key, flights)
    elif c == '2':
        show_booked_flights(cursor, username)
        display_welcome()

# menu for booking a flight (user has just signed up and there are no prebooked flights)
elif signup:
    print(f'{bcolors.HEADER}BOOK A FLIGHT{bcolors.ENDC}')
    book_a_flight = True
    source_city, destination_city = choose_city()
    key = source_city + "_to_" + destination_city
    date_diff, travel_date_string = date_choice(key, flights)

# creating the airplane seat booking ----------------------------------------------------------------------------
if book_a_flight:
    occupied_seats = flight_table_creator(date_diff, key, mycon_flights, cursor_flights, travel_date_string)

    # seat booking -----------------------------------------------------------------------------------------------
    total_number_of_seats = input("Total number of reservations: ")
    available_number_of_seats = 0

    # finding the available number of seats and exception handling if the user has entered a wrong value
    for i in range(0, len(occupied_seats)):
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
    display_aeroplane_seat(occupied_seats, all_seats)
    accept_users_seat(number_of_seats_booked, users_seat,
                      occupied_seats, terminator, name, email, phone_number, current_user_number, all_seats,
                      room, room_cost, room_choice,
                      food, food_list, food_cost,
                      travel_date_string,
                      mycon_flights, cursor_flights,
                      travel_date_string, key)

    # inserting all the information into the database
    seeker_rooms = 0  # counter to track the number of iterations completed in rooms
    seeker_food = 0  # counter to track the number of iterations completed in food
    for i in range(0, len(name)):
        n = name[i]  # fetching the name of the user
        u = users_seat[i]  # fetching the seat of the user
        p = phone_number[i]  # fetching the phone number of the user
        e = email[i]  # fetching the email of the user
        insert_string = ''  # declaring insert string (string used to insert information into the database

        if room[i] and food[i]:  # insert statement when user has booked room and food
            f_choice = food_list[seeker_food][0] + ', '
            for j in range(1, len(food_list[seeker_food])):
                for k in range(0, len(food_list[seeker_food][j])):
                    f_choice = f_choice + food_list[seeker_food][j][k] + ', '
            f_cost = food_cost[seeker_food]
            r_choice = room_choice[seeker_rooms]
            r_cost = room_cost[seeker_rooms]
            insert_string = f"insert into booked_flight_details values('{username}', '{source_city}'," \
                            f" '{destination_city}', '{travel_date_string}', '{n}', '{u}', {p}, '{e}', NULL," \
                            f"'{r_choice}', {r_cost}, '{f_choice}', {f_cost})"
            seeker_food += 1
            seeker_rooms += 1

        elif not room[i] and not food[i]:  # insert statement when user has booked neither room nor food
            insert_string = f"insert into booked_flight_details values('{username}', '{source_city}'," \
                            f" '{destination_city}', '{travel_date_string}', '{n}', '{u}', {p}, '{e}', NULL, " \
                            f"'NO ROOM BOOKED', 0.0, 'NO FOOD ORDERED', 0.0)"

        elif room[i] and not food[i]:  # insert statement when user has booked room but not food
            r_choice = room_choice[seeker_rooms]
            r_cost = room_cost[seeker_rooms]
            insert_string = f"insert into booked_flight_details values('{username}', '{source_city}'," \
                            f" '{destination_city}', '{travel_date_string}', '{n}', '{u}', {p}, '{e}', NULL," \
                            f"'{r_choice}', {r_cost}, 'NO FOOD ORDERED', 0.0)"
            seeker_rooms += 1

        elif not room[i] and food[i]:  # insert statement when user has not booked a room but has ordered food
            f_choice = food_list[seeker_food][0] + ', '
            for j in range(1, len(food_list[seeker_food])):
                for k in range(0, len(food_list[seeker_food][j])):
                    f_choice = f_choice + food_list[seeker_food][j][k] + ', '
            f_cost = food_cost[seeker_food]
            print(f_choice, f_cost)
            insert_string = f"insert into booked_flight_details values('{username}', '{source_city}'," \
                            f" '{destination_city}', '{travel_date_string}', '{n}', '{u}', {p}, '{e}', NULL," \
                            f"'NO ROOM BOOKED', 0.0, '{f_choice}', {f_cost})"
            seeker_food += 1

        cursor.execute(insert_string)
        mycon.commit()
