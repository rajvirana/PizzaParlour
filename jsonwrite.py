from json import JSONEncoder
import order
import json
from typing import Dict

JSON = "orders.json"


def write_to_json(new_order: Dict[str, float]):

    with open('orders.json') as indata:
        order_data = json.load(indata)

        indata.close()

    order_data[new_order["_order_id"]] = new_order

    with open('orders.json', 'w') as outdata:
        json.dump(order_data, outdata)

        outdata.close()


# if __name__ == "__main__":

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
