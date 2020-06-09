from threading import *

class BookMyBus() :
    
    def __init__(self,seats):
        self.availableSeats = seats
        
    def buy(self,seatsrequested):
        print('Total number of seats available:',self.availableSeats)
        print('Seats requested: ',seatsrequested)
        if(self.availableSeats>=seatsrequested) :
            print('Confirming seats...')
            print('Processing the payment...')
            print('Printing the ticket...')
            self.availableSeats -= seatsrequested
        else :
            print('Sorry. No seats available. Only', self.availableSeats,'available. :(')
   
        
        
bookobj = BookMyBus(10)  # to add the total available seats.

t1 = Thread(target=bookobj.buy,args=(3,))  ## to pass it 3 requested seats inside a non main thread
t2 = Thread(target=bookobj.buy,args=(4,))
t3 = Thread(target=bookobj.buy,args=(4,))

t1.start()
t2.start()
t3.start()