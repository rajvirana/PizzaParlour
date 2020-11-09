import csv

with open('menu.csv', newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])



# Sizes
# Small        1.99
# Medium      10.99
# Large

# Pizza
# Pepperoni