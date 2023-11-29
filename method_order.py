def order_control(ice_cream_inventory, topping_inventory, paper_inventory, fullinventory, full_sales):
    print("Would you like to place another order? Y/N")
    choice = input.strip()
    if choice.upper == "Y":
        place_order(ice_cream_inventory, topping_inventory, paper_inventory, fullinventory, full_sales)
    else:
        print("Thank you!")
        
def place_order(ice_cream_inventory, topping_inventory, paper_inventory, fullinventory, full_sales):
    print("Here is the order and delivery schedule:")
    print("1. Vendor1:")
    print("   Order by: Sunday/Wednesday")
    print("   Delivery : Monday/Thursday")
    print("2. Vendor2:")
    print("   Order by: Friday")
    print("   Delivery: Monday")
    print("3. Vendor3:")
    print("   Order By: Monday")
    print("   Delivery: Wednesday")
    print("4. Vendor4:")
    print("   Order By: Saturday")
    print("   Delivery: Monday")
    
    print("What are we placing an order for? (1,2,3,4)")
    choice = input()

    if choice == "1":
        for flavor_list in ice_cream_inventory:
            for flavor in flavor_list:
                if flavor.vendor == "Vendor1":
                    #temp = fullinventory.index(flavor.name)
                    print(f"{flavor.name} : {full_sales[fullinventory.index(flavor.name)]}")
        for topping_list in ice_cream_inventory:
            for topping in topping_list:
                if flavor.vendor == "Vendor1":
                    print(f"{topping.name} : {full_sales[fullinventory.index(topping.name)]}")
        for paper_list in paper_inventory:
            for paper in paper_list:
                if paper.vendor == "Vendor1":
                    print(f"{paper.name} : {full_sales[fullinventory.index(paper.name)]}")
        order_control(ice_cream_inventory, topping_inventory, paper_inventory, fullinventory, full_sales)

    if choice == "2":
        for flavor_list in ice_cream_inventory:
            for flavor in flavor_list:
                if flavor.vendor == "Vendor2":
                    #temp = fullinventory.index(flavor.name)
                    print(f"{flavor.name} : {full_sales[fullinventory.index(flavor.name)]}")
        for topping_list in ice_cream_inventory:
            for topping in topping_list:
                if flavor.vendor == "Vendor2":
                    print(f"{topping.name} : {full_sales[fullinventory.index(topping.name)]}")
        for paper_list in paper_inventory:
            for paper in paper_list:
                if paper.vendor == "Vendor2":
                    print(f"{paper.name} : {full_sales[fullinventory.index(paper.name)]}")
        order_control(ice_cream_inventory, topping_inventory, paper_inventory, fullinventory, full_sales)

    if choice == "3":
        for flavor_list in ice_cream_inventory:
            for flavor in flavor_list:
                if flavor.vendor == "Vendor3":
                    #temp = fullinventory.index(flavor.name)
                    print(f"{flavor.name} : {full_sales[fullinventory.index(flavor.name)]}")
        for topping_list in ice_cream_inventory:
            for topping in topping_list:
                if flavor.vendor == "Vendor3":
                    print(f"{topping.name} : {full_sales[fullinventory.index(topping.name)]}")
        for paper_list in paper_inventory:
            for paper in paper_list:
                if paper.vendor == "Vendor3":
                    print(f"{paper.name} : {full_sales[fullinventory.index(paper.name)]}")
        order_control(ice_cream_inventory, topping_inventory, paper_inventory, fullinventory, full_sales)

    if choice == "4":
        for flavor_list in ice_cream_inventory:
            for flavor in flavor_list:
                if flavor.vendor == "Vendor4":
                    #temp = fullinventory.index(flavor.name)
                    print(f"{flavor.name} : {full_sales[fullinventory.index(flavor.name)]}")
        for topping_list in ice_cream_inventory:
            for topping in topping_list:
                if flavor.vendor == "Vendor4":
                    print(f"{topping.name} : {full_sales[fullinventory.index(topping.name)]}")
        for paper_list in paper_inventory:
            for paper in paper_list:
                if paper.vendor == "Vendor4":
                    print(f"{paper.name} : {full_sales[fullinventory.index(paper.name)]}")
        order_control(ice_cream_inventory, topping_inventory, paper_inventory, fullinventory, full_sales)
