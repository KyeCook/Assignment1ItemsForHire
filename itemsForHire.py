"""
CP1404 - Assignment 1 : 2016
Items For Hire
Kye Cook
29/03/2016
GitHub Repository Link : https://github.com/KyeCook

Pseudocode:

Function Main()
    call load_items()
    set load_items() as tuple variable called items
    display welcome message
    display MENU
    get choice
    while choice is not 'Q'
        if choice is 'L'
            display items
        else if choice is 'H'
            call hire_items()
        else if choice is 'R'
            call return_items()
        else if choice = 'A'
            call add_items()
        else
            display error message
        display MENU
        get choice
    print thank you message and number of items saved into list


Function load_items()
    load items.csv document
    convert into tuple (?here or in main?)
    return loaded document


Function hire_items()
    get choice
    if choice is in stock
        display item hired
        return item hired
    else:
        print item is not currently in stock


Function return_items(items)
    while items are hired
        get choice
        if choice is in items
            make item returned on list
            return items
        else
            print error message
    print no items are hired


Function add_items(items)
    get choice for item name
    get choice for description
    get choice for price per day
    print item name(description), price per day now available for hire
    concatenate to items tuple
    return items
"""
MENU = "Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd enw item to stock\n(Q)uit"


def main():
    print("Welcome to the Items For Hire Program")
    print("Written by Kye Cook, March 2016")

    items = load_items()

    print(MENU)
    menu_selection = input(">>> ").upper()
    while menu_selection != "Q":
        if menu_selection == "L":
            print("All items on file (* indicates item is currently out):\n", items, sep='')
        elif menu_selection == "H":
            print(hire_items(items))
        else:
            print("Error")
        print(MENU)
        menu_selection = input(">>> ").upper()
    print("{} items saved to items.csv\nHave a nice day :)")


def load_items():
    loaded_items = open("items.csv", 'r')
    items = loaded_items.read()
    return items

# Refer to practice py file for better way to load in .csv file


def hire_items(items):
    print(items)
    print("Enter the number of an item to hire:")
    hired_item = input(">>> ")
    if items[-2] != '*':
        print(items[-2])
        if hired_item in items:
            hired_item_msg = "wunderbra"
            return hired_item_msg
        else:
            hired_item_msg = "Nicht gut"
            return hired_item_msg

    # Refer to practice py file
main()
