from typing import List
import csv
import time
 
CSV = "menu.csv"

class Order:
    '''
    '''

    def __init__(self, type, size, extra_toppings, drink, delivery) :
        self._order_id = self.timestamp()

        self._type = type
        self._size = size

        self._extra_toppings = extra_toppings


        self._drink = drink
        self._delivery = delivery
        self._price = self.calculate_price()

    def calculate_price(self) -> float:

        total = 0.0

        with open(CSV, newline="") as f:
            reader = csv.reader(f)

            for row in reader:
                if row[0].lower() == self._size or row[0].lower() == self._type or row[0].lower() == self._drink or row[0].lower() in self._extra_toppings:
                    
                    total += float(row[1])
        
        return total

    def timestamp(self) -> int:
        '''
        NOBODY'S GONNA KNOW ;)
        they'er gonna knoW
        hOw wOUlD thEY knoW????
        '''
        now = time.time()
        localtime = time.localtime(now)
        milliseconds = '%03d' % int((now - int(now)) * 1000)

        return time.strftime('%Y%m%d%H%M%S', localtime) + milliseconds

    def get_price(self) -> int:
        '''
        '''
        return self._price
    
    def get_order_id(self) -> int:
        '''
        '''
        return self._order_id
    
    def get_toppings(self) -> List:
        '''
        '''
        return self._extra_toppings
    
    def set_price(self, new_price) -> None:
        '''
        '''
        self._price = new_price


if __name__ == "__main__":
    order = Order('cheese', 'small', ['feta cheese'], 'coke', 'ubereats')

    print(order.get_price()) # 16.55