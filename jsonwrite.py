from json import JSONEncoder
from order import Order
import json
from typing import Dict

# the json files orders will be read from and written to
JSON = "orders.json"

def get_order_ids():
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


# if __name__ == "__main__":

#     a = get_order_ids()

#     print('20201112165232710' in a)
#     remove_from_json("20201109220810220")

    # new_order = order.Order('cheese', 'small', ['feta cheese'], 'coke', 'ubereats', '123 depression street' )

    # writetofile(new_order)

    # new_order2 = order.Order('cheese', 'small', [], 'coke', 'ubereats', '123 depression street' )

    # writetofile(new_order2)

    # OID = "20201109200700761"
    # s =  {"_order_id": "20201109200700761", "_type": "cheese", "_size": "large", "_extra_toppings": [], "_address": "123 depression street", "_drink": "coke", "_delivery": "ubereats", "_price": 16.55}

    # updated_order = order.Order('cheese', 'large', [], "coke", 'ubereats', '123 geric mertler st')
    # updated_order.set_order_id(OID)

    # writetofile(updated_order)

    # s = json.dumps(new_order.__dict__)
    # data = {}
    # data[new_order.get_order_id()] = s

    # print(data)

    # with open('orders.json') as indata:
    #     stuff = json.load(indata)

    # stuff.update(data)

    # with open('orders.json', 'w') as outdata:
    #     json.dump(stuff, outdata)

    # data = {}

    # new_order2 = order.Order('cheese', 'small', [], 'coke', 'ubereats', '123 depression street' )

    # s2 = json.dumps(new_order.__dict__)
    # data[new_order2.get_order_id()] = s2

    # with open('orders.json') as indata:
    #     stuff = json.load(indata)

    # stuff[new_order2.get_order_id()] = s2

    # with open('orders.json', 'w') as outdata:
    #     json.dump(stuff, outdata)

    # with open('orders.json', 'r') as f:
    #     stuff = json.load(f)
    #     print(stuff)

    # x = {'20201109195024816': '{"_order_id": "20201109195024816", "_type": "cheese", "_size": "small", "_extra_toppings": ["feta cheese"], "_address": "123 depression street", "_drink": "coke", "_delivery": "ubereats", "_price": 16.55}', '20201109195024824': '{"_order_id": "20201109195024816", "_type": "cheese", "_size": "small", "_extra_toppings": ["feta cheese"], "_address": "123 depression street", "_drink": "coke", "_delivery": "ubereats", "_price": 16.55}'}

    # res = json.loads(x['20201109195024816'])

    # print("BITHC BETTER WORK")
    # print(res)
    # print(res['_price'])
