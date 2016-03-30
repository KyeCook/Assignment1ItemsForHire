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


def main():
    items = load_items()
    print(items)


def load_items():
    loaded_items = open("items.csv", 'r')
    items = loaded_items.read()
    return items
main()