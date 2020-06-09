from threading import *


# We use Semaphore, acquire and release to lock that object so no other thread calls it in the meantime

class BookMyBus() :
    
    def __init__(self,seats):
        self.availableSeats = seats
        self.lok = Semaphore()   ## Semaphore() is a class from the threading module 
        
    def buy(self,seatsrequested):

        self.lok.acquire()   ## to invoke the lock so no other threads call it!
        
        print('Total number of seats available:',self.availableSeats)
        print('Seats requested: ',seatsrequested)
        if(self.availableSeats>=seatsrequested) :
            print('Confirming seats...')
            print('Processing the payment...')
            print('Printing the ticket...')
            self.availableSeats -= seatsrequested
        else :
            print('Sorry. No seats available. Only', self.availableSeats,'available. :(')
            
        self.lok.release()   ## to release it again
 
 
        
bookobj = BookMyBus(10)  # to add the total available seats.

t1 = Thread(target=bookobj.buy,args=(3,))  ## to pass it 3 requested seats inside a non main thread
t2 = Thread(target=bookobj.buy,args=(4,))
t3 = Thread(target=bookobj.buy,args=(4,))

t1.start()
t2.start()
t3.start()