import csv
from tempfile import NamedTemporaryFile
import shutil

CSV = "orders.csv"


def write_to_csv(new_order):
    with open('orders.csv', 'w', newline='') as csvfile:
        fieldnames = ['order_id', 'type', 'size', 'extra_toppings',
                      'drink', 'delivery', 'address', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'order_id': new_order.get_order_id(), 'type': new_order.get_type(), 'size': new_order.get_size(),
                         'extra_toppings': new_order.get_toppings(), 'drink': new_order.get_drink(), 'delivery': new_order.get_delivery(),
                         'address': new_order.get_address(), 'price': new_order.get_price()})

        csvfile.close()


def update_order_csv(order):
    tempfile = NamedTemporaryFile('w', newline='', delete=False)

    fieldnames = ['order_id', 'type', 'size', 'extra_toppings',
                  'drink', 'delivery', 'address', 'price']

    with open('orders.csv', 'r', newline='') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)
        writer = csv.DictWriter(tempfile, delimiter=',', fieldnames=fieldnames)

        for row in reader:

            if row['order_id'] == order.get_order_id():

                row['order_id'] = order.get_order_id()
                row['type'] = order.get_type()
                row['size'] = order.get_size()
                row['extra_toppings'] = order.get_toppings()
                row['drink'] = order.get_drink()
                row['delivery'] = order.get_delivery()
                row['address'] = order.get_address()
                row['price'] = order.get_price()

            row = {'order_id': row['order_id'],
                   'type': row['type'],
                   'size': row['size'],
                   'extra_toppings': row['extra_toppings'],
                   'drink': row['drink'],
                   'delivery': row['delivery'],
                   'address': row['address'],
                   'price': row['price']}

            writer.writerow(row)

    shutil.move(tempfile.name, 'orders.csv')
