from threading import *

class BookMyBus() :
    
    def buy(self):
        print('Confirming a seat...')
        print('Processing the payment...')
        print('Printing the ticket...')
        
        
        
bookobj = BookMyBus()

t1 = Thread(target=bookobj.buy)
t2 = Thread(target=bookobj.buy)
t3 = Thread(target=bookobj.buy)

t1.start()
t2.start()
t3.start()


