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
import csv

MENU = "Menu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"


def main():
    print("Welcome to the Items For Hire Program")
    print("Written by Kye Cook, March 2016")

    item_id, item_names, item_descriptions, item_costs, item_availability, items = load_items()

    print(MENU)
    menu_selection = input(">>> ").upper()
    while menu_selection != "Q":
        if menu_selection == "L":
            print("All items on file (* indicates item is currently out):")
            for line in items:
                print(line)

        elif menu_selection == "H":
            hire_items(item_id ,item_names, item_availability, item_costs, items)
        elif menu_selection == "R":
            return_items(item_id, item_names, item_availability, item_costs, items)
        else:
            print("Error")
        print(MENU)
        menu_selection = input(">>> ").upper()
    print("{} items saved to items.csv\nHave a nice day :)".format(len(item_id)))


def load_items():
    f = open('items.csv')
    csv_f = csv.reader(f)

    item_names = []
    item_descriptions = []
    item_costs = []
    item_availability = []
    item_id = []
    items = []

    item_id_count = -1

    for row in csv_f:
        item_id_count += 1

        item_id.append(item_id_count)
        item_names.append(row[0])
        item_descriptions.append(row[1])
        item_costs.append(row[2])

        if row[3] == "out":
            item_availability.append("*")
        else:
            item_availability.append("")
        items.append("{} - {} ({}) = $ {}{}".format(item_id[item_id_count], item_names[item_id_count],
                                                    item_descriptions[item_id_count], item_costs[item_id_count],
                                                    item_availability[item_id_count]))

    return item_id, item_names, item_descriptions, item_costs, item_availability, items


def hire_items(item_id,item_names, item_availability, item_costs, items):
    for line in items:
        print(line)
    print("Enter number of item to hire")
    item_to_hire = int(input(">>> "))
    if item_to_hire in item_id:
        item_availability[item_to_hire] = "*"

        items[item_to_hire] += '*'
        print("{} hired for ${}".format(item_names[item_to_hire], item_costs[item_to_hire]))
        return item_availability[item_to_hire]
    else:
        print("That item is not available for hire")


def return_items(item_id,item_names, item_availability, item_costs, items):
    for line in items:
        print(line)
    print("Enter number of item to return")
    item_to_return = int(input(">>> "))
    if item_to_return in item_id:
        item_availability[item_to_return] = ""

        items[item_to_return] += " "
        print("{} - {} = $ {}{}".format(item_id[item_to_return], item_names[item_to_return],
                                        item_costs[item_to_return], item_availability[item_to_return]))
        print(item_names[item_to_return], "returned")
        return item_availability[item_to_return]
    else:
        print("That item is not on hire")
main()
