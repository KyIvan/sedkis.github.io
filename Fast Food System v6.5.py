customers_order = []


def restaurant_menu():
    while True:
        print('1. Food Menu \n2. Drink Menu \n3. Combo Menu\n')
        menu_choice = int(input('Pick your menu number (1, 2, 3). Enter 5 if you are finished ordering: '))
        if menu_choice == 1:
            customers_order.append(food_choice())
        elif menu_choice == 2:
            customers_order.append(drink_choice())
        elif menu_choice == 3:
            customers_order.append(combo_choice())
        else:
            for bug in customers_order:
                if bug is None:
                    customers_order.remove(bug)
                    total = (sum(customers_order))
                    print(f'Your receipt is ₱{total}')
                    while True:
                        user_cash = float(input('Payment: '))
                        if user_cash < total:
                            print(f'Not enough cash, please try again')
                            continue
                        else:
                            print(f'You have payed {user_cash}, and the total order cash of your order is {total}. '
                                  f'Your receipt {user_cash - total}')
                            exit()


def fast_menu():
    print('\n' * 5, '-' * 10, f'Good day customer, what would you like to buy? These are in our menu:', '-' * 10)
    menu = [['1: Food Menu', ['1: Burger = ₱30.10', '2: Fries = ₱15.50', '3: Fried Chicken = ₱40']],
            ['2: Drink Menu', ['1: Cola = ₱17.25', '2: Sprite = ₱15.50', '3: Water = Free']],
            ['3: Combos Menu', ['1: Chicken Bucket w/Cola = 105', '2: 3 Burgers w/Sprite = 75.10', '3: Double Burger '
                                                                                                   'and Fries w/Cola '
                                                                                                   '= 55.30']]]

    for available in menu:
        print(available[0])
        for food in available[1]:
            print('*', food)
        print('=' * 50)


def food_choice():
    print('=' * 50, '\n' * 5)
    food_menu = [['1: Food Menu', ['1: Burger = ₱30.10', '2: Fries = ₱15.50', '3: Fried Chicken = ₱40']]]
    for available in food_menu:
        print(available[0])
        for food in available[1]:
            print('*', food)
        print('=' * 50, '\n' * 2)
    pick_food = int(input('Enter your choice of food  from the Food Menu (1, 2, 3) or (5) to go back: \n'))

    print()
    if pick_food in (1, 2, 3, 4):
        if pick_food == 1:
            print(f'Burger costs ₱30.10')
            print('=' * 50, '\n' * 5)
            return customers_order.append(30.10)
        elif pick_food == 2:
            print(f'Fries costs ₱25.30')
            print('=' * 50, '\n' * 5)
            return customers_order.append(25.30)
        elif pick_food == 3:
            print(f'Fried chicken costs ₱40')
            print('=' * 50, '\n' * 5)
            return customers_order.append(40)
        else:
            print('=' * 50, '\n' * 5)
            return 0


def drink_choice():
    print('=' * 50, '\n' * 5)
    drink_menu = [['2: Drink Menu', ['1: Cola = ₱17.25', '2: Sprite = ₱15.50', '3: Water = Free']]]
    for available in drink_menu:
        print(available[0])
        for food in available[1]:
            print('*', food)
        print('=' * 50, '\n' * 2)
    pick_drink = int(input('Enter your choice of drink from the Drinks Menu next (1, 2, 3) or (5) to go back'
                           'to finish your order: '))

    print()
    if pick_drink in (1, 2, 3):
        if pick_drink == 1:
            print(f'Cola costs ₱17.25')
            drink_result = 17.25
            drink_size = input('Pick Drink Size, type (L) for large or (N) if you dont want any changes')
            if drink_size.casefold() == 'l':
                drink_result += 2
                print(drink_result)
                print('=' * 50, '\n' * 5)
                return customers_order.append(drink_result)

            else:
                drink_result += 0
                print(drink_result)
                print('=' * 50, '\n' * 5)
                return customers_order.append(drink_result)

        elif pick_drink == 2:
            print(f'Sprite costs ₱15.50')
            drink_result = 15.50
            drink_size = input('Pick Drink Size, type (L) for large or (M) if you dont want any changes')
            if drink_size.casefold() == 'l':
                drink_result += 2
                print(drink_result)
                print('=' * 50, '\n' * 5)
                return customers_order.append(drink_result)

            else:
                drink_result += 0
                print(drink_result)
                return customers_order.append(drink_result)
        else:
            print(f'Water is for costs ₱0')
            drink_result = 0
            print('=' * 50, '\n' * 5)
            return customers_order.append(drink_result)


def combo_choice():
    print('=' * 50, '\n' * 5)
    combo_menu = [['3: Combos Menu', ['1: Chicken Bucket w/Cola = 105', '2: 3 Burgers w/Sprite = 75.10', '3: Double '
                                                                                                         'Burger '
                                                                                                         'and Fries '
                                                                                                         'w/Cola '
                                                                                                         '= 55.30']]]
    for available in combo_menu:
        print(available[0])
        for food in available[1]:
            print('*', food)
        print('=' * 50, '\n' * 2)
    pick_combo = int(input('Enter your choice of drink from the Combos Menu next (1, 2, 3) or (5) to go back '
                           'to finish your order: '))
    print()
    if pick_combo in (1, 2, 3):
        if pick_combo == 1:
            print(f'Bucket full of Chicken costs ₱105', '\n', '=' * 50, '\n' * 5)
            return customers_order.append(105)
        elif pick_combo == 2:
            print(f'Fries costs ₱75.10', '\n', '=' * 50, '\n' * 5)
            return customers_order.append(75.10)
        elif pick_combo == 3:
            print(f'Fried chicken costs ₱55.30', '\n', '=' * 50, '\n' * 5)
            return customers_order.append(55.30)
        else:
            return 0
    print('=' * 50, '\n' * 5)


# Account
name = 'ivan'
passcode = '123'

# Account confirmation
while True:
    username = input('Enter your username: ')
    if username != name:
        print('Incorrect username, try again')
    else:
        while True:
            password = input('Enter password: ')
            if password != passcode:
                print(f'Incorrect password, try again')
            else:
                print('\t' * 10, '-' * 10, 'Successfully Logged In', '-' * 10, '\n' * 5)
                restaurant_menu()
                fast_menu()
