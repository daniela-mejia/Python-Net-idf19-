# cashRegister.py
import retail
import cashRegister


class CashRegister:

    # initialize an empty list to hold purchased items
    def __init__(self):

        self.__items = []

    # method that clears the contents of the cash register
    def clear(self):

        self.__items = []

    # method that simulates adding an item to the cash register.
    # receives a RetailItem object as an argument. 
    def purchase_item(self, retail_item):

        self.__items.append(retail_item)
        print("The item was added to the cash register.")

    # method returning the total cost of items at the cash register.
    def get_total(self):

        total = 0.0
        for item in self.__items:
            total = total + item.get_price()

        return total

    # method that prints a list of items at the cash register.
    def show_items(self):

        print("The items in the cash register are:")
        print()
        for item in self.__items:
            print(item)
            print()
 
# 11-7.py



# constants to hold the options of purchase items
PANTS = 1
SHIRT = 2
DRESS = 3
SOCKS = 4
SWEATER = 5


def main():

    #create sale items
    pants = retail.RetailItem("Pants", 10, 19.99)
    shirt = retail.RetailItem("Shirt", 15, 12.50)
    dress = retail.RetailItem("Dress", 3, 79.00)
    socks = retail.RetailItem("Socks", 50, 1.00)
    sweater = retail.RetailItem("Sweater", 5, 49.99)

    # create dictionary of sale items
    sale_items = {PANTS:pants, SHIRT:shirt, \
                  DRESS:dress, SOCKS:socks, SWEATER:sweater}

    # create a cash register
    register = cashRegister.CashRegister()

    # initialize loop test
    checkout = 'N'

    # user wants to purchase more items
    while checkout=='N':

        user_choice = get_user_choice()
        item = sale_items[user_choice]
        if item.get_inventory() == 0:
            print("The item is out of stock.")
        else:
            register.purchase_item(item)

            # update item
            new_item = retail.RetailItem(item.get_description(),\
                                         item.get_inventory()-1,\
                                         item.get_price())
            sale_items[user_choice] = new_item

            checkout = input("Are you ready to check out (Y/N)? ")

    print()
    print("Your purchase total is: ", format(register.get_total(), '.2f'))
    print()
    register.show_items()
    register.clear()

def get_user_choice():

    print("Menu")
    print("---------------------------------")
    print("1. Pants")
    print("2. Shirt")
    print("3. Dress")
    print("4. Socks")
    print("5. Sweater")
    print()

    choice = int(input("Enter the menu number of the item " +\
                       "you would like to purchase: "))
    print()

    while choice > SWEATER or choice < PANTS:

        choice = int(input("Please enter a valid item number: "))
        print()

    return choice


main()
class RetailItem:

    # __int__ method initializes the attributes.
    def __init__(self, description, units, price):
        self.__item_description = description
        self.__units_in_inventory = units
        self.__price = price

    # The set_item_description method gets the item type.
    def set_item_description(self, description):
        self.__item_description = description

    # The set_units_in_inventory method gets number of items available.
    def set_units_in_inventory(self, units):
        self.__units_in_inventory = units

    # The set_price method gets the cost of item.
    def set_price(self, price):
        self.__price = price

    # The get_item_description method returns the item type.
    def get_item_description(self):
        return self.__item_description

    # The get_units_in_inventory returns the number of items available.
    def get_units_in_inventory(self):
        return self.__units_in_inventory

    # The get_price method returns the cost of item.
    def get_price(self):
        return self.__price


# This program will test the RetailItem class and return information
# using the mutator method.

import sys

# This defines the main function.
def main():
    # Get a list of RetailItem objects.
    inventory = make_list()

    # Display the data in the list.
    print('Here is the data you entered:')
    list_display(inventory)

    # The make_list will get data for three items. It will
    #return a list of available items.

def make_list():
    # Create an empty list.
    item_list = []

    # Add three item to the list.
    print('Enter data for three items.')
    for count in range(1, 4):
        # Get item data.
        print('Item number ' + str(count) + ':')
        item = input('Enter description of item: ')
        units = float(input('Enter number of units in inventory: '))
        price = float(input('Enter price per item: '))
        print()

        # Creat new RetailItem and assign items variable.
        items = RetailItem(item, units, price)
        # Add items to list.
        item_list.append(items)

        return item_list

    #Display the items information.
    def display_list(item_list):
        for item in item_list:
            print(item.get_item_description())
            print(item.get_units_in_inventory())
            print(item.get_price())
            print()