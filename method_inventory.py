import datetime
import pandas as pd
import numpy as np
from method_export import write_to_excel
from method_order import place_order

def inventory_start(ice_cream_inventory, topping_inventory, paper_inventory):
    take_inventory(ice_cream_inventory, topping_inventory, paper_inventory)

def inventory_control(ice_cream_inventory, topping_inventory, paper_inventory):
    print("Would you like to place another order? Y/N")
    choice = input.strip()
    if choice.upper == "Y":
        place_order(ice_cream_inventory, topping_inventory, paper_inventory)
    else:
        print("Thank you!")
        
def take_inventory(ice_cream_inventory, topping_inventory, paper_inventory):
    print("Is today Monday? Y/N")
    monday = input().strip()

    full_sales = []
    current = []

    print("Okay! Let's start with ice cream flavors")
    for flavor_list in ice_cream_inventory:
        for flavor in flavor_list:
            print(f"{flavor.name}: ")
            count = int(input())
            full_sales.append(flavor.standard_amount - count)

    print("\nNow toppings")
    for topping_list in topping_inventory:
        for topping in topping_list:
            print(f"{topping.name}: ")
            count = int(input())
            full_sales.append(topping.standard_amount - count)

    print("\nNow paper products")
    for paper_list in paper_inventory:
        for paper in paper_list:
            print(f"{paper.name}: ")
            count = int(input())
            full_sales.append(paper.standard_amount - count)

    fullinventory = []
    for flavor_list in ice_cream_inventory:
        for flavor in flavor_list:
            fullinventory.append(flavor.name)
    for topping_list in topping_inventory:
        for topping in topping_list:
            fullinventory.append(topping.name)
    for product_list in paper_inventory:
        for product in product_list:
            fullinventory.append(product.name)

    print("\nAre you\n1. Placing an order today\n2. Wanting an overall summary")
    choice = input()
    if choice == "1":
        place_order(ice_cream_inventory, topping_inventory, paper_inventory, fullinventory, full_sales)
    if choice == "2":
        for fullinventory, full_sales in zip(fullinventory, full_sales):
            print(fullinventory, full_sales)

    if monday.upper() == "Y":
        write_to_excel(fullinventory,full_sales)
        print("Data has been recorded.")
