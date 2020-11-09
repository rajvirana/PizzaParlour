import csv
from tempfile import NamedTemporaryFile
import shutil

def writetofile(new_order):
    with open('orders.csv', 'w', newline='') as csvfile:
        fieldnames = ['order id','price','toppings']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'order id': new_order.get_order_id(), 
        'price': new_order.get_price(), 'toppings': new_order.get_toppings()})

        csvfile.close()


def updateorder(order):
    order.set_price(3424783932)

    tempfile = NamedTemporaryFile('w', newline='', delete=False)

    fieldnames = ['order id','price','toppings']

    with open('orders.csv', 'r', newline='') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)
        writer = csv.DictWriter(tempfile, delimiter=',', fieldnames=fieldnames)

        for row in reader:
            
            if row['order id'] == '19347293874':
                print('updating row', row['order id'])
                row['order id'], row['price'], row['toppings'] = order.get_order_id(), order.get_price(), order.get_toppings()
            
            row = {'order id': row['order id'], 'price': row['price'], 'toppings': row['toppings']}
            writer.writerow(row)

    shutil.move(tempfile.name, 'orders.csv')
