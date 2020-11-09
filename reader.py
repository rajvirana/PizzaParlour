import csv

with open('menu.csv', newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])
