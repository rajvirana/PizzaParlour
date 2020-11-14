from typing import List
from order import Order
import time

class OrderBuilder:
    '''
    Builder for an Order object.

    ===Public Attributes===
    order:
        The order that the OrderBuilder builds.
    '''
    
    def __init__(self) -> None:
        '''
        Creates a new OrderBuilder.
        '''
        self.order = Order()
    
    def build_orderid(self) -> None:
        '''
        Generates an order id based on the time of the user's order, to the millisecond.
        '''
        now = time.time()
        localtime = time.localtime(now)
        milliseconds = '%03d' % int((now - int(now)) * 1000)

        orderid = time.strftime('%Y%m%d%H%M%S', localtime) + milliseconds

        self.order.set_order_id(orderid)
    
    def build_price(self, prices: dict) -> None:
        '''
        Calculates the price dynamically based off of menu.csv's prices.
        '''
        total = 0.0

        for k in prices:
            if k == self.order.get_size() or k == self.order.get_type() or k == self.order.get_drink() or k in self.order.get_toppings():
                total += float(prices[k])

        total = round(total, 2)

        self.order.set_price(total)

    def build_drink(self, drink: str) -> None:
        '''
        Builds the drink in the order.
        '''
        self.order.set_drink(drink)
    
    def build_type(self, type: str) -> None:
        '''
        Builds the type of pizza in the order.
        '''
        self.order.set_type(type)

    def build_size(self, size: str) -> None:
        '''
        Builds the size of the pizza in the order.
        '''
        self.order.set_size(size)

    def build_toppings(self, toppings: List[str]) -> None:
        '''
        Builds the drink type of the order.
        '''
        self.order.set_toppings(toppings)

    def build_update_orderid(self, orderid: str) -> None:
        '''
        Updates the order id.
        '''
        self.order.set_order_id(orderid)

    def build(self) -> Order:
        '''
        Returns the order that was built.
        '''
        return self.order