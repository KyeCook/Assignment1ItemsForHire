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

    item_id, item_names, item_descriptions, item_costs, item_availability, items, item_id_count = load_items()

    print(MENU)
    menu_selection = input(">>> ").upper()
    while menu_selection != "Q":
        if menu_selection == "L":
            print("All items on file (* indicates item is currently out):")
            for line in items:
                print(line)

        elif menu_selection == "H":
            hire_items(item_id, item_names, item_availability, item_costs, items)
        elif menu_selection == "R":
            return_items(item_id, item_names, item_availability, item_costs, items)
        elif menu_selection == "A":
            add_items(item_id, item_names, item_descriptions, item_costs, item_availability, items, item_id_count)
        else:
            print("Error")
        print(MENU)
        menu_selection = input(">>> ").upper()
    update_csv(item_names, item_descriptions, item_costs, item_availability, items)
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
        item_costs.append(float(row[2]))

        if row[3] == "out":
            item_availability.append("*")
        else:
            item_availability.append("")
        string_for_formatting = "{} ({})".format(item_names[item_id_count], item_descriptions[item_id_count],)
        items.append("{} - {:<40s} = $ {:>7.2f}{}".format(item_id[item_id_count], string_for_formatting,
                                                          item_costs[item_id_count], item_availability[item_id_count]))
    return item_id, item_names, item_descriptions, item_costs, item_availability, items, item_id_count


def hire_items(item_id, item_names, item_availability, item_costs, items):
    valid_input = False

    for line in items:
        if line[-1] != "*":
            print(line)
    print("Enter number of item to hire")

    while not valid_input:
        try:
            item_to_hire = int(input(">>> "))
            if item_to_hire > (len(item_id) - 1):
                print("Invalid item number")
            elif item_to_hire in item_id and "*" not in items[item_to_hire]:
                item_availability[item_to_hire] = "*"

                items[item_to_hire] += '*'
                print("{} hired for ${}".format(item_names[item_to_hire], item_costs[item_to_hire]))

                valid_input = True

                return item_availability[item_to_hire]
            elif "*" in items[item_to_hire]:
                print("That item is not on hire")
            else:
                print("Invalid item number")
        except ValueError:
            print("Invalid input, enter a number")


def return_items(item_id, item_names, item_availability, item_costs, items):
    valid_input = False

    for line in items:
        if line[-1] == "*":
            print(line)
    print("Enter number of item to hire")

    while not valid_input:
        try:
            item_to_return = int(input(">>> "))
            if item_to_return > (len(item_id) - 1):
                print("Invalid item number")
            elif item_to_return in item_id and "*" in items[item_to_return]:
                item_availability[item_to_return] = ""

                items[item_to_return] = ("{} - {} = $ {}{}".format(item_id[item_to_return], item_names[item_to_return],
                                         item_costs[item_to_return], item_availability[item_to_return]))

                print("{} hired for ${}".format(item_names[item_to_return], item_costs[item_to_return]))

                valid_input = True

                return item_availability[item_to_return]
            elif "*" not in items[item_to_return]:
                print("That item is not on hire")
            else:
                print("Invalid item number")
        except ValueError:
            print("Invalid input, enter a number")


def add_items(item_id, item_names, item_descriptions, item_costs, item_availability, items, item_id_count):
    valid_input = False
    item_id_count += 1
    item_id.append(item_id_count)

    item_availability.append("")
# Error Checking Loops - Ensure no empty values are entered
    item_names_new = (input("Item name:"))
    while item_names_new == "":
        print("Input can not be empty")
        item_names_new = (input("Item name:"))
    item_names.append(item_names_new)

    item_descriptions_new = (input("Description:"))
    while item_descriptions_new == "":
        print("Input can not be empty")
        item_descriptions_new = (input("Description:"))
    item_descriptions.append(item_descriptions_new)
# Try statement to allow user to change input if not in float(numeric) format
    while not valid_input:
        try:
            item_costs_new = (float(input("Price per day: $")))
            if item_costs_new < 0:
                print("Price must be >= $0")
            else:
                item_costs.append(item_costs_new)
                valid_input = True
        except ValueError:
            print("Enter a valid number")

    print("{} ({}), ${:.2f} now available for hire".format(item_names[item_id_count], item_descriptions[item_id_count],
                                                           item_costs[item_id_count]))

    items.append("{} - {} ({}) = $ {:>7.2f}{}".format(item_id[item_id_count], item_names[item_id_count],
                                                      item_descriptions[item_id_count], item_costs[item_id_count],
                                                      item_availability[item_id_count]))
    return items, item_names, item_costs, item_id_count, item_descriptions, item_availability


def update_csv(item_names, item_descriptions, item_costs, item_availability, items):
    f = open('items2.csv', 'w')
    count = -1
    item_list_update = []
    item_availability_old = []
    for line in items:
        count += 1
        if item_availability[count] == "*":
            item_availability_old.append("out")
        else:
            item_availability_old.append("in")
        item_list_update.append([item_names[count], item_descriptions[count], str(item_costs[count]),
                                item_availability_old[count]])
    for line in item_list_update:
        f.write(','.join(line) + '\n')
    f.close()
main()
