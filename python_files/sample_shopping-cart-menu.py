# clear the screen
# import os
import time
# os.system("cls")
time.sleep(1)

# Define the menu as a function
def menu():
    print()
    print('Welcome to the Shopping Cart Program!')
    print()
    print('Please select one of the following:')
    print('1.  Add item')
    print('2.  View cart')
    print('3.  Remove item')
    print('4.  Compute total')
    print('5.  Quit')
    print()

# print the shopping cart list
def print_lists():
    print()
    print('The contents of the shopping cart are:')
    indx = 1
    for item in range(len(cart_list)):
        indx = item + 1
        item_name = cart_list[item]
        item_price = cart_list_price[item]
        print(f'{indx}.  {item_name.capitalize()} - ${item_price:.2f}')

# create a list for the shopping cart and for prices of items
cart_list = []
cart_list_price = []

# display menu option; evaluate options
menu_opt = 0
while menu_opt != 5:
    menu()

    valid_menu = False
    while not valid_menu:
        try:
            menu_opt = int(input('Please enter an action (1-5): '))
            if menu_opt > 0 and menu_opt < 6:
                valid_menu = True
        except ValueError:
            print('\033[1;33;40mSorry, incorrect entry. Please try again.\033[0;37;48m')
            continue

    # menu option 1 -- add items to the shopping cart list
    if menu_opt == 1:
        more_items = True
        print()
        while more_items:
            new_item = input('What item would you like to add? Type "end" to exit:  ')
            if new_item.lower() != 'end':
                price_invalid = True
                while price_invalid:
                    try:
                        new_item_price = float(input('What is the price of ' + new_item + '?  '))
                        price_invalid = False
                    except ValueError:
                        print('\033[1;33;40mSorry, invalid price entry. Please try again.\033[0;37;48m')
                        continue
                cart_list.append(new_item)
                cart_list_price.append(new_item_price)
                print(f'\033[1;32;40m{new_item}\033[0;37;48m at \033[1;32;40m${new_item_price:.2f}\033[0;37;48m has been added to the list.')
                print()
            else:
                more_items = False

    # menu option 2 -- view cart items
    elif menu_opt == 2:
        if cart_list != []:
            print_lists()
        else:
            print('\033[1;33;40mYour shopping cart list is empty.\033[0;37;48m')

    # menu option 3 -- remove cart items
    elif menu_opt == 3:
        if cart_list != []:
            print_lists()
            print()
            
            # request option to amend; validate input
            input_not_valid = True
            while input_not_valid:
                try:
                    upd_indx = int(input('Which item would you like to remove? '))
                    upd_indx -= 1
                    if upd_indx not in range(len(cart_list)):
                        print('\033[1;33;40mSorry, that is not a valid item number.\033[0;37;48m')
                    input_not_valid = False
                    # delete items from lists
                    del_name = cart_list[upd_indx]
                    cart_list.pop(upd_indx)
                    cart_list_price.pop(upd_indx)
                    print(f'{del_name.capitalize()} has been \033[1;31;40m deleted \033[0;37;48m')
                    print()
                except ValueError:
                    print('\033[1;33;40mSorry, invalid entry. Please try again.\033[0;37;48m')
                    continue
        else:
            print('\033[1;33;40mYour shopping cart list is empty.\033[0;37;48m')

    # menu option 4 -- checkout the cart
    elif menu_opt == 4:
        if cart_list != []:
            print()
            list_total = sum(cart_list_price)
            print(f'The total price of the items in the shopping cart is ${list_total:.2f}')
        else:
            print('\033[1;33;40mYour shopping cart list is empty.\033[0;37;48m')
        print()

    elif menu_opt ==5:
        # menu option 5 -- exit the program
        print()
        print('Thank you. Goodbye.')

    else:
        print('\033[1;33;40mInvalid option. Select 1 through 5.\033[0;37;48m')
