import csv
from typing import List

MENU = "menu.csv"

def get_reader() -> List[str]:
    '''
    Returns a list of the lines in menu.csv
    '''
    rows = []

    with open(MENU, newline="") as f:
        reader = csv.reader(f)

        for line in reader:
            rows.append(line)

        f.close()

    return rows

def get_prices():

    items = get_reader()
    items_dict = {}

    for i in items:
        name = i[0].lower()
        price = i[1]

        if name == "uoftears (extra salty)":
            name = "uoftears"

        if price != "":
            items_dict[name] = price
    
    return items_dict