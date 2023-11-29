def allergens_start(ice_cream_inventory, topping_inventory, paper_inventory):
    print("\nWhat would you like to see the allergens for?")
    print("1. Ice cream flavors")
    print("2. Toppings/cones")
    view_allergens(ice_cream_inventory, topping_inventory, paper_inventory)

def allergens_control(ice_cream_inventory, topping_inventory, paper_inventory):
    print("Would you like to see another? Y/N")
    choice = input().strip()
    if choice.upper() == "Y":
        allergens_start(ice_cream_inventory, topping_inventory, paper_inventory)
    else:
        print("Thank you!")

def view_allergens(ice_cream_inventory, topping_inventory, paper_inventory):
    choice = input()
    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a number.")
    else:
        if choice == 1:
            for  flavor_list in ice_cream_inventory:
                for flavor in flavor_list:
                    # Check if any allergens are present
                    if any([flavor.peanut, flavor.milk, flavor.treenut, flavor.wheat, flavor.soy]):
                        print(f"\n{flavor.name}")
                        # Print individual allergens if present
                        if flavor.peanut:
                            print("   Contains peanuts")
                        if flavor.milk:
                            print("   Contains milk")
                        if flavor.treenut:
                            print("   Contains tree nuts")
                        if flavor.wheat:
                            print("   Contains wheat/gluten")
                        if flavor.soy:
                            print("   Contains soy")
                    else:
                        print(f"\n{topping.name} - No allergens")
        allergens_control(ice_cream_inventory, topping_inventory, paper_inventory)
        if choice == 2:
            for topping_list in topping_inventory:
                for topping in topping_list:
                    # Check if any allergens are present
                    if any([topping.peanut, topping.milk, topping.treenut, topping.wheat, topping.soy]):
                        print(f"\n{topping.name}")

                        # Print individual allergens if present
                        if topping.peanut:
                            print("   Contains peanuts")
                        if topping.milk:
                            print("   Contains milk")
                        if topping.treenut:
                            print("   Contains tree nuts")
                        if topping.wheat:
                            print("   Contains wheat/gluten")
                        if topping.soy:
                            print("   Contains soy")
                    else:
                        print(f"\n{topping.name} - No allergens")
        allergens_control(ice_cream_inventory, topping_inventory, paper_inventory)