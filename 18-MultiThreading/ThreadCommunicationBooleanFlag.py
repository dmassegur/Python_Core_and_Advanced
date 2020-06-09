from threading import *
from time import *

class Producer() :  # class responsible for producing the work
    def __init__(self):
        self.products = []  # an empty list to initialise it
        self.ordersplaced = False # initially this will be false
        
    def produce(self):
        for i in range(1,5) :
            self.products.append('Product'+str(i))   # we add it to the list
            sleep(1)
            print('Item added.')
        print('Order completed.')
        self.ordersplaced = True  ## we flag it as True
        

class Consumer() :  ## class responsible of the consumer taking the order from the producer
    def __init__(self,prod):
        self.prod = prod   ## we have actually passed an object of class Producer!!! it's another way of inheriting!!!
        
    def consume(self):
        while self.prod.ordersplaced == False :
            print('Waiting for an order to be placed...')
            sleep(0.5)  ## is waiting every 0.5s for the flag to be turned to True
            
        print('Order placed by Producer!! Orders shipped ',self.prod.products)
        
        
p = Producer()

c = Consumer(p)   ## consumer object passes another object class named p. This is how they communicate: object inside and object! 


t1 = Thread(target=p.produce)   # one thread acts as a produced
t2 = Thread(target=c.consume)   # the other trhead does the consumer, which received communication from p


t1.start()
t2.start()