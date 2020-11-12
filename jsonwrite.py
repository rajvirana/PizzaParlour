from json import JSONEncoder
from order import Order
import json
from typing import Dict

# the json files orders will be read from and written to
JSON = "orders.json"

def get_order_ids():
    '''
    Returns a list of all the order ids in the order.json file.
    '''

    with open(JSON) as indata:
        order_data = json.load(indata)

        indata.close()
    
    keys = order_data.keys()

    return keys

def write_to_json(new_order: Order):
    '''
    Writes the order, new_order, into orders.json

    Precondition: new_order.get_delivery() == "ubereats" or new_order.get_delivery() == "in-house"
    '''

    with open(JSON) as indata:
        order_data = json.load(indata)

        indata.close()

    order_dict = json.dumps(new_order.__dict__)

    order_data[new_order.get_order_id()] = order_dict

    with open(JSON, 'w') as outdata:
        json.dump(order_data, outdata)

        outdata.close()


def remove_from_json(order_id: str):
    '''
    Removes the order from orders.json given the order_id

    Precondition: order_id already exists in orders.json
    '''
    with open(JSON) as indata:
        order_data = json.load(indata)

        indata.close()

    if order_id in order_data:
        del order_data[order_id]

        with open(JSON, 'w') as outdata:
            json.dump(order_data, outdata)

            outdata.close()


def convert_to_csv(order_id: str):
    '''
    Converts the order into a csv-formatted string.
    '''
    data = get_order(order_id)
    keys = data.keys()

    output = "_order_id, _type, _extra_toppings, _drink, _price\n"

    for k in keys:
        if k == "_order_id":
            output = output + str(data[k])
        else:
            output = output + "," + str(data[k])

    return output

def get_order(order_id: str):
    '''
    Returns the order information associated with the order id.
    '''
    with open(JSON) as indata:
        order_data = json.load(indata)

        indata.close()

    data = json.loads(order_data[order_id])

    return data