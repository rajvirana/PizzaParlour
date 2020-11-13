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
