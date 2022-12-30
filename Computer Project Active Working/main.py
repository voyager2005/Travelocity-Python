import mysql.connector as mysql

from AirplaneReservationSystem import *
from HotelRoomReservation import *

'''
declaring global variables of Airplane Seat Reservation ---------------------------------------------------------------
'''
# global variables
signup = False
login = False
book_a_flight = False
today_date = ''
travel_date = ''
today_time = ''
username = ""
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
# declaring global variables [lists]
bread_list = ["White Loaf", "Garlic and Parmesan", "Sesame", "Brown loaf"]
bread_cost = [20, 25, 25, 20]
meat_list = ["Egg Mayo", "Roasted Beef", "Turkey", "Cold Cut Trio", "Italian Bmt", "Skip"]
meat_cost = [20, 40, 30, 50, 50, 0]
veggies_list = ["Olives", "Jalapenos", "Onion", "baby tomatoes", "lettuce", "tofu",
                "bell peppers", "skip"]
veggies_cost = [5, 5, 10, 10, 10, 30, 30, 0]
seasoning_list = ["shrimp paste", "ranch", "mayo", "cheese", "Salt and pepper", "skip"]
seasoning_cost = [10, 10, 10, 10, 10, 0]
drinks_list = ["water", "iced tea", "coke", "skip"]
drinks_cost = [15, 20, 20, 0]
others_list = ["choco chip cookie", "butter cookie", "chicken wings", "skip"]
others_cost = [50, 50, 50, 0]

# declaring global variables
cost = 0
food, food_meat, food_veggies, food_seasoning, food_drinks, food_others = list(), list(), list(), list(), list(), list()

'''
GLOBAL VARIABLES OF HOTEL ROOM RESERVATION ---------------------------------------------------------------------------
'''
# declaring global variables
single_bed = [1, 2, 3, 4, 5]
double_bed = [6, 7, 8, 9, 10]
cost_hotel_room_reservation = 0.0

'''
MAIN ----------------------------------------------------------------------------------------------------------------
'''

# ----- AIRPLANE SEAT RESERVATION -----
# __main__
# python, mysql connectivity
mycon = mysql.connect(host="localhost", user="root", port='3306', password="Akshat@2005", database="class12project")
cursor = mycon.cursor()

# displaying welcome message to the user and prompting for signup and login
while True:
    display_welcome()
    choice = int(input(f'{bcolors.OKBLUE}Please enter your choice: {bcolors.ENDC}'))
    if choice == 1:
        username, signup = create_user(mycon, cursor)
    elif choice == 2:
        username, login = login_user(cursor)
        break
    else:
        print(f'{bcolors.FAIL}INVALID CHOICE{bcolors.ENDC}')

# menu for Booking a flight and checking for booked flights
if login:
    print(f"{bcolors.WARNING}[1]{bcolors.ENDC} {bcolors.HEADER}BOOK A FLIGHT{bcolors.ENDC}\n"
          f"{bcolors.WARNING}[2]{bcolors.ENDC} {bcolors.HEADER}SEE BOOKED FLIGHTS{bcolors.ENDC}\n"
          f"{bcolors.WARNING}[3]{bcolors.ENDC} {bcolors.HEADER}BOOK A HOTEL{bcolors.ENDC}\n"
          f"{bcolors.WARNING}[4]{bcolors.ENDC} {bcolors.HEADER}SEE BOOKED HOTELS{bcolors.ENDC}\n")
    c = input()
    if c == '1':
        book_a_flight = True
        source_city, destination_city = choose_city()
        key = source_city + "_to_" + destination_city
        date_diff, travel_date_string = date_choice(key, flights)
    elif c == '2':
        show_booked_flights(cursor, username)
        # I need to use a goto here to take this back to the beginning of the menu (book flight and see booked flights)
elif signup:
    print(f'{bcolors.HEADER}BOOK A FLIGHT{bcolors.ENDC}')
    book_a_flight = True
    source_city, destination_city = choose_city()
    key = source_city + "_to_" + destination_city
    date_diff, travel_date_string = date_choice(key, flights)

# creating the airplane seat booking
if book_a_flight:
    if date_diff == '0':
        percentage = 3
    elif date_diff == '1':
        percentage = 5
    elif date_diff == '2':
        percentage = 7
    else:
        percentage = 10

    for i in range(0, len(all_seats)):
        x = randint(0, 10)
        if 0 < x < percentage:
            occupied_seats.append(False)
        else:
            occupied_seats.append(True)

    # seat booking
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
    display_aeroplane_seat(occupied_seats, all_seats)
    accept_users_seat(number_of_seats_booked, users_seat, all_seats_index,
                      occupied_seats, terminator, name, email, phone_number, current_user_number, all_seats)

    for i in range(0, len(name)):
        n = name[i]
        u = users_seat[i]
        p = phone_number[i]
        e = email[i]
        insert_string = f"insert into booked_flight_details values('{username}', '{source_city}'," \
                        f" '{destination_city}', '{travel_date_string}', '{n}', '{u}', {p}, '{e}', NULL)"
        cursor.execute(insert_string)
        mycon.commit()
