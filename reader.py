import csv

with open('menu.csv', newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == '':
            print("YEET")
        else:
            print(row[1])
