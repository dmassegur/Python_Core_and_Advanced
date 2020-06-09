from threading import *
from time import *

class Producer() :  # class responsible for producing the work
    def __init__(self):
        self.products = []  # an empty list to initialise it
        self.cond = Condition()   # class available from threading, it includes synchronisation lock too!
        
    def produce(self):
        self.cond.acquire()  ## we lock this obj
        
        for i in range(1,5) :
            self.products.append('Product'+str(i))   # we add it to the list
            sleep(1)
            print('Item added.')
        print('Order completed.')
        
        self.cond.notify()  ## we notify the other thread that it has finished. you can use notifyAll
        self.cond.release()  ## we unlock this obj

        

class Consumer() :  ## class responsible of the consumer taking the order from the producer
    def __init__(self,prod):
        self.prod = prod   ## we have actually passed an object of class Producer!!! it's another way of inheriting!!!
        
    def consume(self):
        self.prod.cond.acquire()  ## we lock it so no other thread uses it
        self.prod.cond.wait(timeout=0)  ## we wait until notify is called from the other thread. it does it immediately 0s
            
        print('Order placed by Producer!! Orders shipped ',self.prod.products)
        
        self.prod.cond.release()  ## we unlock it so another thread can use it now
 
        
p = Producer()

c = Consumer(p)   ## consumer object passes another object class named p. This is how they communicate: object inside and object! 


t1 = Thread(target=p.produce)   # one thread acts as a produced
t2 = Thread(target=c.consume)   # the other trhead does the consumer, which received communication from p


t1.start()
t2.start()