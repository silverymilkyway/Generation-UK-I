# Product names
product_list = ['Ham Grilled Cheese Sandwich', 'Chicken Salad Baguette','Rosette sandwich','Crab & Cucumber Sandwich','Veggie Falafel Sandwich','Harissa chilly sauce','Engine Oil','Lemonade','Coffee','Still water']

print('************************************************\n***Greetings! Welcome yo Cafe UI homescreen.***\n************************************************\n')

while True:
#Product Menu 
    main_menu = input("""
            Select one of the following options:
            
            1: Show product list
            2: Add new product to the list
            3: Replace at a certain index
            4: Delete items
            0: Exit product menu
            
            Please enter your choice: """)
    print(main_menu)
    
# Exit menu
    if "0" in main_menu:
            print('Thanks for using porduct list, Goodbye!')
            break 

# Show list
    elif "1" in main_menu:
        for i in product_list:
            print(i)
            continue 

# Add
    elif "2" in main_menu:
        for (i, item) in enumerate(product_list, start=0):
            print(i, item)
        new_value = input("What would you like to add to the list?")
        product_list.append(new_value)
        print(product_list)
        continue 

# Alter
    elif "3" in main_menu:
        for (i, item) in enumerate(product_list, start=0):
            print(i, item)
        new_index = int(input("Please enter an index of your choice:"))
        new_replacement_item =input("What would you like it to be?") 
        product_list[new_index] = new_replacement_item
        print(product_list)
        continue

# Delete
    elif "4" in main_menu:
        for (i, item) in enumerate(product_list, start=0):
            print(i, item)
        delete = int(input("Which one you would like to delete?"))
        del product_list[delete]
        print(product_list)
        continue

# Wrong input
    else:
        print("You must only select which provided. Please try again.")
        continue
