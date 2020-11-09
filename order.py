from typing import List
import time
 
class Order:
    '''
    '''

    def __init__(self):
        self.order_id = self.timestamp()
        self.price = 10000
        self.toppings = ['salt', 'tears', 'cheese']
        
    def timestamp(self) -> int:
        '''
        '''
        now = time.time()
        localtime = time.localtime(now)
        milliseconds = '%03d' % int((now - int(now)) * 1000)

        return time.strftime('%Y%m%d%H%M%S', localtime) + milliseconds

    def get_price(self) -> int:
        '''
        '''
        return self.price
    
    def get_order_id(self) -> int:
        '''
        '''
        return self.order_id
    
    def get_toppings(self) -> List:
        '''
        '''
        return self.toppings
    
    def set_price(self, new_price) -> None:
        '''
        '''
        self.price = new_price


if __name__ == "__main__":
    order = Order()

    print(order.get_order_id())