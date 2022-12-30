from colors import bcolors


def hotel_room_reservation(cost_hotel_room_reservation):
    contd = True
    final_room_number = [1, 2, 2, 6, 5]
    counter = 0

    print("\f")
    print(f'{bcolors.HEADER}WELCOME TO HOTEL ROOM RESERVATION{bcolors.ENDC}')
    print()
    print("Do you want to book a room with")
    print(f"{bcolors.FAIL}(a){bcolors.ENDC} {bcolors.OKBLUE}1 King Size Bed{bcolors.ENDC}")
    print(f"{bcolors.FAIL}(b){bcolors.ENDC} {bcolors.OKBLUE}2 King Size Beds{bcolors.ENDC}")
    print(f"{bcolors.FAIL}(c){bcolors.ENDC} {bcolors.OKBLUE}1 Queen Size Bed{bcolors.ENDC}")
    print(f"{bcolors.FAIL}(d){bcolors.ENDC} {bcolors.OKBLUE}2 Queen Size Beds{bcolors.ENDC}")
    print(f"{bcolors.FAIL}(e){bcolors.ENDC} {bcolors.OKBLUE}dormantry{bcolors.ENDC}")

    while contd:
        room = input("Your choice please: ").lower()
        print("Your room has been booked on {insert date here} from 12:00 noon for 23 hours")
        print("Your room number is: ", final_room_number[counter])

        if room == 'a' or room == 'b' or room == 'c' or room == 'd' or room == 'e':
            # adding the cost
            if room == 'a':
                cost_hotel_room_reservation = cost_hotel_room_reservation + 849.99
            elif room == 'b':
                cost_hotel_room_reservation = cost_hotel_room_reservation + 1499.99
            elif room == 'c':
                cost_hotel_room_reservation = cost_hotel_room_reservation + 499.99
            elif room == 'd':
                cost_hotel_room_reservation = cost_hotel_room_reservation + 899.99
            elif room == 'e':
                cost_hotel_room_reservation = cost_hotel_room_reservation + 749.99
        else:
            print("ROOM SPECIFICATIONS NOT FOUND!! \n you can do the following and try again \n"
                  "1. check the spelling Ex. 2 King Size Bed instead of 2 King Size Bed(s)")
            continue

        # display statement
        print(f"{bcolors.OKCYAN}Room Specifications{bcolors.ENDC} ")
        print(f"{bcolors.OKCYAN}Room Service:{bcolors.ENDC} YES")
        print(f"{bcolors.OKCYAN}AC: +59.99 (optional){bcolors.ENDC} (extra amount to be paid at hotel) ")
        print(f"{bcolors.OKCYAN}Meals: (optional){bcolors.ENDC} (extra amount to be paid at hotel) ")

        counter = counter + 1
        ans = input(f'{bcolors.OKBLUE}Do you want to book another room{bcolors.ENDC}'
                    f'{bcolors.FAIL}(yes/no): {bcolors.ENDC}').lower().strip()
        if counter < 5 and ans == 'yes':
            contd = True
        elif counter == 5:
            print(f'{bcolors.FAIL}UNFORTUNATELY ALL THE SEATS ARE BOOKED{bcolors.ENDC}')
            break
        elif ans == 'no':
            break

    return cost_hotel_room_reservation
