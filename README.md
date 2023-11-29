# Meltdown_Ice_Cream_Database
Managerial database to assist users in maintaining and ordering product stock
Created with the intent of sharing responsibilities with supervisors

## all.py
-Initializes three main arrays (ice_cream_inventory, topping_inventory, paper_inventory) to be populated by respective functions
-Initial user interface to allow users to select their choice of process to run

## IceCreamFlavor.py
-Creates IceCreamFlavor class with generic values populating attributes in the __init__ method
-Attributes include important information regarding properties, pricing information, and allergens

## Topping.py
-Creates Topping class with generic values populating attributes in the __init__ method
-Attributes include important information regarding properties, pricing information, and allergens

## Paper.py
-Creates Paper class with generic values populating attributes in the __init__ method
-Attributes include important information regarding properties and pricing information

## PopulateIceCream.py
-Creates instances of each flavor the shop stocks and sets values to applicable attributes
-Populates the ice_cream_inventory array (created in all.py) with each instance

## PopulateTopping.py
-Creates instances of each topping the shop stocks and sets values to applicable attributes
-Populates the topping_inventory array (created in all.py) with each instance

## PopulatePaper.py
-Creates instances of each paper product the shop stocks and sets values to applicable attributes
-Populates the paper_inventory array (created in all.py) with each instance

## method_allergies.py
### allergens_start method
-Provides initial directive to the user, allowing them to choose what product category they would like to see
### view_allergens method
-Reads user input to prompt from allergens_start method as an integer, catching the exception if it is not
-Iterates through either ice_cream_inventory or topping_inventory, checks if any allergen values set in the populate files are True, and prints applicable allergens for each item in the array
-Sends information to allergens_control method for further directives
### allergens_control method
-Allows the user to run the view_allergens method again if they would like to see the other array's allergens

## method_details.py
### details_start method
-Provides initial directive to the user, allowing them to choose what product category they would like to see the details of
-Input is run through a series of if statements to send the information to the appropriate function
### icecream method
-Allows the user to choose if they would like to see the details for a specific flavor or all flavors.
  -If the user wants to see a specific flavor, a list of each item in the ice_cream_inventory array is printed with a corresponding index value
  -The user enters the index of the flavor they would like to see, and the attributes of that requested flavor are printed
  -If the user wants to see all flavors' attributes, the program iterates through the array and prints the name of each product along with the other attributes
-If the user enters an invalid number, they are prompted to enter another
-Information is passed to the details_control method
### topping method
-Allows the user to choose if they would like to see the details for a specific topping or all toppings.
  -If the user wants to see a specific topping, a list of each item in the topping_inventory array is printed with a corresponding index value
  -The user enters the index of the topping they would like to see, and the attributes of that requested topping are printed
  -If the user wants to see all topping's attributes, the program iterates through the array and prints the name of each product along with the other attributes
-If the user enters an invalid number, they are prompted to enter another
-Information is passed to the details_control method
### paper method
-Allows the user to choose if they would like to see the details for a specific paper product or all paper product.
  -If the user wants to see a specific paper product, a list of each item in the paper_inventory array is printed with a corresponding index value
  -The user enters the number of the paper product they would like to see, and the attributes of that requested product are printed
  -If the user wants to see all paper product's attributes, the program iterates through the array and prints the name of each product along with the other attributes
-If the user enters an invalid number, they are prompted to enter another
-Information is passed to the details_control method
### details_control
-Asks the user if they would like to see the details of another product type, and passes to the corresponding array if so

## method_inventory.py
### take_inventory method
-Asks the user if the day is Monday and records the response as a boolean value
-Creates empty arrays full_sales and full_inventory
-Iterates through ice_cream_inventory, topping_inventory, and paper-inventory, prompting the user to enter the number of units currently in stock for each item
-Appends the array full_sales with each input subtracted from the standard_amount attribute and the array fullinventory with each product name
  -Keeps these in order, so full_sales[0] corresponds with fullinventory[0], etc.
-Asks the user if they are placing a specific order or if they would like to see a summary of products they need to order
  -If the first, it passes information to method_order.py
  -If the second, it iterates through both arrays using a zip method and displays the name of the product and how many units they need to order
-If the boolean value mon is True, the information is passed to method_export.py

## method_order.py
-Provides a menu for the user to select which vendor they would like to see information about, along with ordering deadlines and delivery days (names of the vendors have been edited for anonymity)
-The user's input is read and passes through a series of if statements
-The arrays ice_cream_inventory, topping_inventory, and paper_inventory are iterated through to find vendor attributes that are equal to the previously selected vendor
-The index of the name of the object is read from the fullinventory array and passed as an index into to the full_sales array, as the two are corresponding
-A list is printed with each item that needs to be ordered and exactly how many units need to be ordered

## method_export.py
-Uses pandas and datetime
-A dataframe is created with fullinventory and full_sales
-This dataframe is exported to a Microsoft Excel file (.xlsx), creating a new sheet with the current datetime as the title
  -Allows managers and owners to track trends through data analysis

## method_view.py
### view_start method
-Asks the user what inventory (ice_cream_inventory, topping_inventory, paper_inventory) they would like to see
-Passes to view_inventory method
### view_inventory method
-Reads user input to the previous question, catching exceptions
-Iterates through the corresponding array, printing the name attribute
-Passes to view_control
### view_control
-Asks the user if they would like to see another inventory
-Passes back to view_inventory method if so
