from colors import bcolors


def hotel_room_reservation():
    final_room_number = [1, 2, 2, 6, 5]
    counter = 0
    cost_hotel_room_reservation = 0

    print("\f")
    print(f'{bcolors.HEADER}WELCOME TO HOTEL ROOM RESERVATION{bcolors.ENDC}')
    print()
    print("Do you want to book a room with")
    print(f"{bcolors.FAIL}(a){bcolors.ENDC} {bcolors.OKBLUE}1 King Size Bed{bcolors.ENDC}")
    print(f"{bcolors.FAIL}(b){bcolors.ENDC} {bcolors.OKBLUE}2 King Size Beds{bcolors.ENDC}")
    print(f"{bcolors.FAIL}(c){bcolors.ENDC} {bcolors.OKBLUE}1 Queen Size Bed{bcolors.ENDC}")
    print(f"{bcolors.FAIL}(d){bcolors.ENDC} {bcolors.OKBLUE}2 Queen Size Beds{bcolors.ENDC}")
    print(f"{bcolors.FAIL}(e){bcolors.ENDC} {bcolors.OKBLUE}dormantry{bcolors.ENDC}")

    room = input("Your choice please: ").lower()
    print("Your room has been booked on {insert date here} from 12:00 noon for 23 hours")
    print("Your room number is: ", final_room_number[counter])

    while True:
        if room == 'a' or room == 'b' or room == 'c' or room == 'd' or room == 'e':
            # adding the cost
            if room == 'a':
                cost_hotel_room_reservation = 849.99
                room = "1 King Size Bed"
            elif room == 'b':
                cost_hotel_room_reservation = 1499.99
                room = "2 King Size Beds"
            elif room == 'c':
                cost_hotel_room_reservation = 499.99
                room = "1 Queen Size Bed"
            elif room == 'd':
                cost_hotel_room_reservation = 899.99
                room = "2 Queen Size Beds"
            elif room == 'e':
                cost_hotel_room_reservation = 749.99
                room = "dormantry"
            break
        else:
            print("ROOM SPECIFICATIONS NOT FOUND!!")
            continue

    # display statement
    print(f"{bcolors.OKCYAN}Room Specifications{bcolors.ENDC} ")
    print(f"{bcolors.OKCYAN}Room Service:{bcolors.ENDC} YES")
    print(f"{bcolors.OKCYAN}AC: +59.99 (optional){bcolors.ENDC} (extra amount to be paid at hotel) ")
    print(f"{bcolors.OKCYAN}Meals: (optional){bcolors.ENDC} (extra amount to be paid at hotel) ")

    return room, cost_hotel_room_reservation
