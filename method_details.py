def details_start(ice_cream_inventory, topping_inventory, paper_inventory):
    print("\nWould you like to see\n1. Ice cream flavors\n2. Toppings\n3. Paper products")
    choice = input() #gets user input
    try:
        choice = int(choice) #converts input to int
    except ValueError:
        print("Please enter a number.")
    else:
        #calls corresponding function
        if choice == 1:
            icecream(ice_cream_inventory, topping_inventory, paper_inventory)
        elif choice == 2:
            topping(ice_cream_inventory, topping_inventory, paper_inventory)
        elif choice == 3:
            paper(ice_cream_inventory, topping_inventory, paper_inventory)

def details_control(ice_cream_inventory, topping_inventory, paper_inventory):
    print("\nWould you like to see another? Y/N")
    choice = input().strip()
    if choice.upper() == "Y":
        details_start(ice_cream_inventory, topping_inventory, paper_inventory)
    else:
        print("Thank you!")

def icecream(ice_cream_inventory, topping_inventory, paper_inventory):
    print("\nWould you like to see\n1. A specific flavor\n2. All flavors")
    choice = int(input().strip())
    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a number.")
        icecream(ice_cream_inventory, topping_inventory, paper_inventory)

    if choice == 1:
        count = 0
        for flavor_list in ice_cream_inventory:
            for flavor in flavor_list:
                count=count+1
                print(count,". ",flavor.name)
        print("Please enter the number: ")
        choice2 = int(input())
        count2=0
        for flavor_list in ice_cream_inventory:
            for flavor in flavor_list:
                count2=count2+1
                if count2==choice2:
                    print(f"\n{flavor.name}: ")
                    print(f"   Description: {flavor.description}")
                    print(f"   Vendor: {flavor.vendor}")
                    print(f"   In stock: {flavor.in_stock}")
                    print(f"   Baseline: {flavor.standard_amount}")
                    print(f"   Price per unit: {flavor.price}")
    elif choice == 2:
        for flavor_list in ice_cream_inventory:
            for flavor in flavor_list:
                print(f"\n{flavor.name}: ")
                print(f"   Description: {flavor.description}")
                print(f"   Vendor: {flavor.vendor}")
                print(f"   In stock: {flavor.in_stock}")
                print(f"   Baseline: {flavor.standard_amount}")
                print(f"   Price per unit: {flavor.price}")
    else:
        print("Please enter a valid number.")
        icecream(ice_cream_inventory,topping_inventory,paper_inventory)
    details_control(ice_cream_inventory, topping_inventory, paper_inventory)

def topping(ice_cream_inventory, topping_inventory, paper_inventory):
    print("\nWould you like to see\n1. A specific flavor\n2. All flavors")
    choice = int(input().strip())
    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a number.")
        topping(ice_cream_inventory, topping_inventory, paper_inventory)

    if choice == 1:
        count = 0
        for topping_list in topping_inventory:
            for topping in topping_list:
                count=count+1
                print(count,". ",topping.name)
        print("Please enter the number: ")
        choice2 = int(input())
        count2=0
        for topping_list in topping_inventory:
            for topping in topping_list:
                count2=count2+1
                if count2==choice2:
                    print(f"\n{topping.name}: ")
                    print(f"   Storage temperature: {topping.temp}")
                    print(f"   Vendor: {topping.vendor}")
                    print(f"   In stock: {topping.in_stock}")
                    print(f"   Baseline: {topping.standard_amount}")
                    print(f"   Price per unit: {topping.price}")
    elif choice == 2:
        for topping_list in topping_inventory:
            for topping in topping_list:
                print(f"\n{topping.name}: ")
                print(f"   Storage temperature: {topping.temp}")
                print(f"   Vendor: {topping.vendor}")
                print(f"   In stock: {topping.in_stock}")
                print(f"   Baseline: {topping.standard_amount}")
                print(f"   Price per unit: {topping.price}")
    else:
        print("Please enter a valid number.")
        icecream(ice_cream_inventory,topping_inventory,paper_inventory)
    details_control(ice_cream_inventory, topping_inventory, paper_inventory)

def paper(ice_cream_inventory, topping_inventory, paper_inventory):
    print("\nWould you like to see\n1. A specific product\n2. All products")
    choice = int(input().strip())
    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a number.")
        paper(ice_cream_inventory, topping_inventory, paper_inventory)

    if choice == 1:
        count = 0
        for paper_list in paper_inventory:
            for paper in paper_list:
                count=count+1
                print(count,". ",paper.name)
        print("Please enter the number: ")
        choice2 = int(input())
        count2=0
        for paper_list in paper_inventory:
            for paper in paper_list:
                count2=count2+1
                if count2==choice2:
                    print(f"\n{paper.name}: ")
                    print(f"   Details: {paper.details}")
                    print(f"   Vendor: {paper.vendor}")
                    print(f"   In stock: {paper.in_stock}")
                    print(f"   Baseline: {paper.standard_amount}")
                    print(f"   Price per unit: {paper.price}")
    elif choice == 2:
        for paper_list in paper_inventory:
            for paper in paper_list:
                print(f"\n{paper.name}: ")
                print(f"   Details: {paper.details}")
                print(f"   Vendor: {paper.vendor}")
                print(f"   In stock: {paper.in_stock}")
                print(f"   Baseline: {paper.standard_amount}")
                print(f"   Price per unit: {paper.price}")
    else:
        print("Please enter a valid number.")
        paper(ice_cream_inventory,topping_inventory,paper_inventory)
    details_control(ice_cream_inventory, topping_inventory, paper_inventory)
