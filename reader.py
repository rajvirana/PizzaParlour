import csv

with open('orders.csv', newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == '':
            print("YEET")
        else:
            if row[0] == '19347293874':
                print("Order found")
                print(row[2])
            
            # print(row)
