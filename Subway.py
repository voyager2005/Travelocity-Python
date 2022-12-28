from colors import bcolors

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


def add_bread():
    global cost
    global food
    global bread_list
    global bread_cost

    # displaying all the items in the list bread
    for i, item in enumerate(bread_list, start=1):
        print(f"{i}. {bcolors.OKBLUE}{item}{bcolors.ENDC} - {bcolors.OKGREEN}{bread_cost[i-1]}{bcolors.ENDC}")

    # prompting and accepting the bread type from the user
    bread_choice = input(f"Choose the type of bread {bcolors.FAIL}(enter S.NO){bcolors.ENDC}: ")
    index_bread_list = int(bread_choice) - 1
    cost = cost + bread_cost[index_bread_list]
    food.append(bread_list[index_bread_list])

    # adding meat
    add_meat()


def add_meat():
    global cost
    global food_meat
    global meat_list
    global meat_cost

    # displaying all the items in the list bread
    for i, item in enumerate(meat_list, start=1):
        print(f"{i}. {bcolors.OKBLUE}{item}{bcolors.ENDC} - {bcolors.OKGREEN}{meat_cost[i-1]}{bcolors.ENDC}")

    # prompting and accepting the meat type from the user
    meat_choice = input(f"Choose the type of meat {bcolors.FAIL}(enter S.NO){bcolors.ENDC}: ")
    index_meat_list = int(meat_choice) - 1
    cost = cost + meat_cost[index_meat_list]
    food_meat.append(meat_list[index_meat_list])

    if int(meat_choice) == int(len(meat_list)):
        print(f"{bcolors.OKBLUE}This step has been skipped{bcolors.ENDC}")
    else:
        print(f"Do you want to {bcolors.OKBLUE}add{bcolors.ENDC} any other item?"
              f" {bcolors.FAIL}[1]add, [2]skip{bcolors.ENDC}")
        if input() == '1':
            add_meat()

    # adding veggies
    add_veggies()


def add_veggies():
    global cost
    global food_veggies
    global veggies_list
    global veggies_cost

    # displaying all the items in the list bread
    for i, item in enumerate(veggies_list, start=1):
        print(f"{i}. {bcolors.OKBLUE}{item}{bcolors.ENDC} - {bcolors.OKGREEN}{veggies_cost[i-1]}{bcolors.ENDC}")

    # prompting and accepting the veggies type from the user
    veggies_choice = input(f"Choose the type of veggies {bcolors.FAIL}(enter S.NO){bcolors.ENDC}: ")
    index_veggies_list = int(veggies_choice) - 1
    cost = cost + veggies_cost[index_veggies_list]
    food_veggies.append(veggies_list[index_veggies_list])

    if veggies_choice == int(len(veggies_list)):
        print(f"{bcolors.OKBLUE}This step has been skipped{bcolors.ENDC}")
    else:
        print(f"Do you want to {bcolors.OKBLUE}add{bcolors.ENDC} any other item?"
              f" {bcolors.FAIL}[1]add, [2]skip{bcolors.ENDC}")
        if input() == '1':
            add_veggies()

    # adding seasoning
    add_seasoning()


def add_seasoning():
    global cost
    global food_seasoning
    global seasoning_list
    global seasoning_cost

    # displaying all the items in the list bread
    for i, item in enumerate(seasoning_list, start=1):
        print(f"{i}. {bcolors.OKBLUE}{item}{bcolors.ENDC} - {bcolors.OKGREEN}{seasoning_cost[i-1]}{bcolors.ENDC}")

    # prompting and accepting the seasoning type from the user
    seasoning_choice = input(f"Choose the type of seasoning {bcolors.FAIL}(enter S.NO){bcolors.ENDC}: ")
    index_seasoning_list = int(seasoning_choice) - 1
    cost = cost + seasoning_cost[index_seasoning_list]
    food_seasoning.append(seasoning_list[index_seasoning_list])

    if seasoning_choice == int(len(seasoning_list)):
        print(f"{bcolors.OKBLUE}This step has been skipped{bcolors.ENDC}")
    else:
        print(f"Do you want to {bcolors.OKBLUE}add{bcolors.ENDC} any other item?"
              f" {bcolors.FAIL}[1]add, [2]skip{bcolors.ENDC}")
        if input() == '1':
            add_seasoning()

    # adding drinks
    add_drinks()


def add_drinks():
    global cost
    global food_drinks
    global drinks_list
    global drinks_cost

    # displaying all the items in the list bread
    for i, item in enumerate(drinks_list, start=1):
        print(f"{i}. {bcolors.OKBLUE}{item}{bcolors.ENDC} - {bcolors.OKGREEN}{drinks_cost[i-1]}{bcolors.ENDC}")

    # prompting and accepting the drink type from the user
    drinks_choice = input(f"Choose the type of drink {bcolors.FAIL}(enter S.NO){bcolors.ENDC}: ")
    index_drinks_list = int(drinks_choice) - 1
    cost = cost + drinks_cost[index_drinks_list]
    food_drinks.append(drinks_list[index_drinks_list])

    if drinks_choice == int(len(drinks_list)):
        print(f"{bcolors.OKBLUE}This step has been skipped{bcolors.ENDC}")
    else:
        print(f"Do you want to {bcolors.OKBLUE}add{bcolors.ENDC} any other item?"
              f" {bcolors.FAIL}[1]add, [2]skip{bcolors.ENDC}")
        if input() == '1':
            add_drinks()

    # adding others
    add_others()


def add_others():
    global cost
    global food_others
    global others_list
    global others_cost

    # displaying all the items in the list bread
    for i, item in enumerate(others_list, start=1):
        print(f"{i}. {bcolors.OKBLUE}{item}{bcolors.ENDC} - {bcolors.OKGREEN}{others_cost[i-1]}{bcolors.ENDC}")

    # prompting and accepting the others??? type from the user
    others_choice = input(f"Choose the item {bcolors.FAIL}(enter S.NO){bcolors.ENDC}: ")
    index_others_list = int(others_choice) - 1
    cost = cost + others_cost[index_others_list]
    food_others.append(others_list[index_others_list])

    if others_choice == int(len(others_list)):
        print(f"{bcolors.OKBLUE}This step has been skipped{bcolors.ENDC}")
    else:
        print(f"Do you want to {bcolors.OKBLUE}add{bcolors.ENDC} any other item?"
              f" {bcolors.FAIL}[1]add, [2]skip{bcolors.ENDC}")
        if input() == '1':
            add_others()

    # displaying the bill
    display_bill()


def display_bill():
    global cost
    global food

    food.append(food_meat)
    food.append(food_veggies)
    food.append(food_seasoning)
    food.append(food_drinks)
    food.append(food_others)

    print(food)

    print(f''' {bcolors.HEADER}BILL AMOUNT{bcolors.ENDC}
    Bill Amount: {bcolors.OKCYAN}{cost}{bcolors.ENDC}
    Bill Amount (18% GST): {bcolors.OKCYAN}{cost * 118/100}{bcolors.ENDC}
    ''')


add_bread()
