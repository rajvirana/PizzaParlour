from typing import List

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

    def __init__(self):
        '''
        Creates a new order.
        '''
        self._order_id = 0
        self._type = ""
        self._size = ""
        self._extra_toppings = []
        self._drink = ""
        self._price = 0

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

    def set_type(self, type) -> str:
        '''
        Sets the type of the pizza in the order.
        '''
        self._type = type

    def set_size(self,size) -> str:
        '''
        Sets the size of the pizza in the order.
        '''
        self._size = size

    def set_toppings(self, toppings) -> List[str]:
        '''
        Sets the list of toppings in the order.
        '''
        self._extra_toppings = toppings

    def set_drink(self, drink) -> str:
        '''
        Sets the drinks specified in the order.
        '''
        self._drink = drink

    def set_price(self, price) -> int:
        '''
        Sets the price of the order.
        '''
        self._price = price

    def get_type(self) -> str:
        '''
        Returns the type of the pizza in the order.
        '''
        return self._type

    def get_size(self) -> str:
        '''
        Returns the size of the pizza in the order.
        '''
        return self._size

    def get_toppings(self) -> List[str]:
        '''
        Returns the list of toppings in the order.
        '''
        return self._extra_toppings

    def get_drink(self) -> str:
        '''
        Returns the drinks specified in the order.
        '''
        return self._drink