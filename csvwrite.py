import csv
from tempfile import NamedTemporaryFile
import shutil


def writetofile(new_order):
    with open('orders.csv', 'w', newline='') as csvfile:
        fieldnames = ['order_id', 'type', 'size', 'extra_toppings',
                      'drink', 'delivery', 'address', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'order_id': new_order.get_order_id(), 'type': new_order.get_type(), 'size': new_order.get_size(),
                         'extra_toppings': new_order.get_toppings(), 'drink': new_order.get_drink(), 'delivery': new_order.get_delivery(),
                         'address': new_order.get_address(), 'price': new_order.get_price()})

        csvfile.close()


def updateorder(order):
    tempfile = NamedTemporaryFile('w', newline='', delete=False)

    fieldnames = ['order_id', 'type', 'size', 'extra_toppings',
                  'drink', 'delivery', 'address', 'price']

    with open('orders.csv', 'r', newline='') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)
        writer = csv.DictWriter(tempfile, delimiter=',', fieldnames=fieldnames)

        for row in reader:

            if row['order_id'] == order.get_order_id():
                print('updating row', row['order id'])
                row['order_id'], row['price'], row['extra_toppings'] = order.get_order_id(
                ), order.get_price(), order.get_toppings()

            row = {'order id': row['order id'],
                   'price': row['price'], 'toppings': row['toppings']}
            writer.writerow(row)

    shutil.move(tempfile.name, 'orders.csv')
