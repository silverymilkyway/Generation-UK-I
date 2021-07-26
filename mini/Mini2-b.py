import sys, os, csv

# Product names
product_list = ['Ham Grilled Cheese Sandwich', 'Chicken Salad Baguette','Rosette sandwich','Crab & Cucumber Sandwich','Veggie Falafel Sandwich','Harissa chilly sauce','Engine Oil','Lemonade','Coffee','Still water']
courier_list = ['Mandy Greer', 'Bonita Witt', 'Octavia Rice', 'Sonya Liu', 'Albi Paine', 'Elleanor Bone', 'Amaya Adamson', 'Iyla Nava', 'Ruby Book']

# Start up greeting
print('************************************************\n***Welcome to the Cafe UI homescreen.***\n************************************************\n')

def main_menu(): # Level 1
    while True: 
        main_menu = input("""
                        ***Main Menu***
                Select one of the following options:
                
                1: Go to product menu
                2: Go to courier menu
                Q: Exit Cafe UI
                
                Please enter your choice: """)
        print(main_menu) 
        
        if main_menu == '1': # Product Menu (lv2)
        
            print('Go to product menu')
            return (product_menu())
        if main_menu == '2': # Courier Menu (lv2)
            
            print('Go to courier menu')
            return (courier_menu())
            
        elif main_menu == 'q'and 'Q': # Exit confirm
            print('                See you next time!!')
            os.system('pause') # Let user have time to read the exit message
            return sys.exit() # Exit Menu
        
        else: # Wrong input
            print('                Invalid input. Please try again!')
            continue

    Continue

def product_menu(): # Level 2
    while True:
        product_menu = input('''
                        ***Produce Menu***
                Select one of the following options:
                
                1: Show product list
                2: Add new product to the list
                3: Replace at a certain index
                4: Delete items
                B: Exit Oroduct menu and back to Main menu
                
                Please enter your choice:''')
        print(product_menu)
        
        if product_menu == '1': # Show list (lv 3)
            print('\nThis is the latest product list:\n')
            for i in product_list:
                print(i)
            continue 
        elif product_menu == '2': # add_product function (lv 3)
            return add_product()
            continue
        elif product_menu == '3': # alter_product function(lv 3)
            return alter_product()
            continue
        elif product_menu == '4': # delete_product function(lv 3)
            return delete_product()
            continue

        elif product_menu == 'b'and 'B': # Go back to main menu
            print('                       Go back to main menu.')
            main_menu()

        else: # Wrong input
            print("                       Invalid input. Please try again!!")
            continue

def add_product(): # Level 3
    for (i, item) in enumerate(product_list, start=0):
        print(i, item)
    new_value = input("\nWhat would you like to add to the list?\n")
    product_list.append(new_value) # add prompt
    
    # show updated list
    print('\nProduct list has been updated:\n') 
    for i in product_list:
        print(i)
        
    #add another product option
    add_more_product = input(""""
                Would you like to add more? 
                Enter Y to add more.
                Enter N to back to Product Menu.
                Your choice:""")
    if add_more_product.lower() == 'y' and 'Y':
        add_product()
        print('\nProduct list has been updated:\n')
        for i in product_list:
            print(i)
            break
        
    elif add_more_product.lower() == 'n' and 'N':
        print('\n                Going back to Product menu.\n')
        os.system('pause') # Let user have time to read the exit message
        return (product_menu()) # lv2 Menu
    
    else: # Wrong input
        print('\n                Invalid input. Going back to Product menu.\n')
        os.system('pause') # Let user have time to read the exit message
        return (product_menu())

def alter_product(): # Level 3
    count=3
    for (i, item) in enumerate(product_list, start=0):
        print(i, item)
    select_index = int(input('                        Please enter an index of your choice.'))
    
    if type(select_index) == int:
        alter_item = input('                        What would you like it to be?') 
        product_list[select_index] = alter_item
        
    # if not integer
    else: 
        if(count==0):
            print('\n                You have failed to input a index. Going back to Product menu.\n')
            os.system('pause') # Let user have time to read the exit message
            return (product_menu()) # lv2 Menu
        else:
            print('Invalid input. Please try again, you have '+str(count)+'more chance to try.');




    # show updated list
    print('\nThis is the latest product list:\n') 
    for i in product_list:
        print(i)

        
    #add another product option
    alter_another = input(""""
                Would you like to replace another one? 
                Enter Y to do so.
                Enter N to back to Product Menu.
                Your choice:""")

    if alter_another.lower() == 'y' and 'Y':
        alter_product()
        print('\nProduct list has been updated:\n')
        for i in product_list:
            print(i)
            break

    elif alter_another.lower() == 'n' and 'N':
        print('\n                Going back to Product menu.\n')
        os.system('pause') # Let user have time to read the exit message
        return (product_menu()) # lv2 Menu

    else: # Wrong input
        print('\n                Invalid input. Going back to Product menu.\n')
        os.system('pause') # Let user have time to read the exit message
        return (product_menu())

def delete_product(): # Level 3
    for (i, item) in enumerate(product_list, start=0):
        print(i, item)
    delete = int(input('                        Which one you would like to delete?.'))
    del product_list[delete]
    print('\nProduct list has been updated.\n')
    print(product_list)
    
    if product_menu == 'b'and 'B':
        print('Go back to main menu.')
    main_menu()


def courier_menu(): #Level 2 
    while True: 
        courier_menu = input("""
                        ***Courier Menu***
                Select one of the following options:
                
                1: Show courier list
                2: Add new courier to the list
                3: Replace at a certain index
                4: Delete item in the list
                Q: Exit courier menu
                
                Please enter your choice: """)
        print(courier_menu)
        
        if courier_menu == '1': # Show list (lv 3)
            print('\nThis is the latest courier list:\n')
            for i in courier_list:
                print(i)
            continue 
        elif courier_menu == '2': # add_courier function (lv 3)
            return add_courier()
            continue
        elif courier_menu == '3': # alter_courier function(lv 3)
            return alter_courier()
            continue
        elif courier_menu == '4': # delete_courier function(lv 3)
            return delete_courier()
            continue

        elif courier_menu == 'b'and 'B': # Go back to main menu
            print('                       Go back to main menu.')
            main_menu()

        else: # Wrong input
            print("                       Invalid input. Please try again!!")
            continue

def add_courier(): # Level 3
    
    for (i, item) in enumerate(courier_list, start=0):
        print(i, item)
    new_value = input("Who would you like to add to the list?)\n")
    courier_list.append(new_value)
    print('\nCourier list has been updated.\n')
    print(courier_list)

def alter_courier(): # Level 3
    for (i, item) in enumerate(courier_list, start=0):
        print(i, item)
    new_index = int(input('                        Please enter an index of your choice.'))
    new_replacement_item = input('                        What would you like it to be?') 
    courier_list[new_index] = new_replacement_item
    print('\nCourier list has been updated.\n')
    print(courier_list)

def delete_courier(): # Level 3
    for (i, item) in enumerate(courier_list, start=0):
        print(i, item)
    delete = int(input('                        Who you would like to delete?.'))
    del courier_list[delete]
    print('\nCourier list has been updated.\n')
    print(courier_list)
    
    if courier_menu == 'b'and 'B':
        print('Go back to main menu.')
    main_menu()


main_menu() # Call main menu function