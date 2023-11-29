def view_start(ice_cream_inventory, topping_inventory, paper_inventory):
    print("\nWhich inventory?\n1. Ice Cream flavors\n2. Toppings\n3. Paper products")
    view_inventory(ice_cream_inventory, topping_inventory, paper_inventory)

def view_control(ice_cream_inventory, topping_inventory, paper_inventory):
    print("Would you like to see another? Y/N")
    choice = input().strip()
    if choice.upper() == "Y":
        view_inventory(ice_cream_inventory, topping_inventory, paper_inventory)
    else:
        print("Thank you!")

def view_inventory(ice_cream_inventory, topping_inventory, paper_inventory):
    choice2 = input().strip()  # Read user input
    print("")
    try:
        choice2 = int(choice2)
    except ValueError:
        print("Please enter a number.")
        return

    if choice2 == 1:
        for  flavor_list in ice_cream_inventory:
            for flavor in flavor_list:
                print(flavor.name)
    elif choice2 == 2:
        for  topping_list in topping_inventory:
            for topping in topping_list:
                print(topping.name)
    elif choice2 == 3:
        for  paper_list in paper_inventory:
            for paper in paper_list:
                print(paper.name)
    else:
        print("Please enter a valid option.")
        view_inventory(ice_cream_inventory, topping_inventory, paper_inventory)

    view_control(ice_cream_inventory, topping_inventory, paper_inventory)