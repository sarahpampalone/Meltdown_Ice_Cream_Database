import pandas as pd
import numpy as np
from PopulateIceCream import *
from PopulateTopping import *
from PopulatePaper import *
from method_view import *
from method_inventory import *
from method_allergies import *
from method_details import *

if __name__ == "__main__":
    ice_cream_inventory = []
    pop_ice_cream(ice_cream_inventory)
    topping_inventory = []
    pop_topping(topping_inventory)
    paper_inventory = []
    pop_paper(paper_inventory)

    print("What would you like to do?\n1. View inventory\n2. Take inventory, place orders, and export data\n3. View allergens\n4. View details")
    choice = input()
    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a number.")
    else:
        if choice == 1:
            view_start(ice_cream_inventory, topping_inventory, paper_inventory) #works!
        elif choice == 2:
            inventory_start(ice_cream_inventory, topping_inventory, paper_inventory) #check out control in this fil2e?
        elif choice == 3:
            allergens_start(ice_cream_inventory, topping_inventory, paper_inventory) #works!
        elif choice == 4:
            details_start(ice_cream_inventory, topping_inventory, paper_inventory)
        else:
            print("That is an invalid input. Here is a list of all of our items!")
            view_start(ice_cream_inventory, topping_inventory, paper_inventory)