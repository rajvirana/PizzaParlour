from typing import List
import csv
import time

CSV = "menu.csv"


class Order:
    '''
    An order for the Pizza Parlour.

    Precondition: All instance variables that are of the str type are all lowercase.

    === Private Attributes ===
    order_id:
        The order's unique ID that the customer uses to change order or cancel order
    type:
        The type of pizza
    size:
        The size of the pizza
    extra_toppings:
        A list of extra toppings (prices calculated separately)
    drink:
        The drink accompanying the pizza
    delivery:
        The delivery method (ubereats / foodora / in-house)
    address:
        The address to deliver the pizza to

    '''
    _order_id: int
    _type: str
    _size: str
    _extra_toppings: List[str]
    _drink: str

    def __init__(self, type, size, extra_toppings, drink):
        '''
        Creates a new order.
        '''
        self._order_id = self._timestamp()
        self._type = type
        self._size = size
        self._extra_toppings = extra_toppings
        self._drink = drink
        self._price = self._calculate_price()

    def _calculate_price(self) -> float:
        '''
        Calculates the price dynamically based off of menu.csv's prices.
        '''
        total = 0.0

        with open(CSV, newline="") as f:
            reader = csv.reader(f)

            for row in reader:
                if row[0].lower() == self._size or row[0].lower() == self._type or row[0].lower() == self._drink or row[0].lower() in self._extra_toppings:

                    total += float(row[1])

        return round(total, 2)

    def _timestamp(self) -> int:
        '''
        Generates an order id based on the time of the user's order, to the millisecond.
        '''
        now = time.time()
        localtime = time.localtime(now)
        milliseconds = '%03d' % int((now - int(now)) * 1000)

        return time.strftime('%Y%m%d%H%M%S', localtime) + milliseconds

    def get_order_id(self) -> int:
        '''
        Returns the order id of the order.
        '''
        return self._order_id

    def set_order_id(self, id: str) -> int:
        '''
        Sets this order's id to id.
        '''
        self._order_id = id
