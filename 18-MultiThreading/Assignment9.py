from threading import *
from time import *


class EvenNumbers():
    def __init__(self,t):
        self.even100 = list(range(2,t,2))
#         print(self.even100)
        self.lock = Condition()
    
    def display(self):
#         print(self.even100)
        self.lock.acquire()
        for i in self.even100 :
            print('Number',i,'from thread',current_thread().getName())
        print('')
        self.lock.notifyAll()
        self.lock.release()    

class OddNumbers():
    def __init__(self,t):
        self.odd100 = list(range(1,t,2))
#         print(self.odd100)
        self.lock = Condition()
    
    def display(self):
#         print(self.odd100)
        self.lock.acquire()
        self.lock.wait(timeout=1.5)
        for i in self.odd100 :
            print('Number',i,'from thread',current_thread().getName())
        self.lock.release()
        
          
target = 101

# print(list(range(2,target,2)))
# # print([range(2,101,2)])  ## it doesn't work

e = EvenNumbers(target)  
o = OddNumbers(target)

# e.display()  # if called by main thread
# o.display()  # if called by main thread

t1 = Thread(target=e.display)  # called by a thread
t2 = Thread(target=o.display)  # called by a thread

t1.start()  # turn on the thread!!!
t2.start()  # turn on the thread!!!

sleep(2)
print('')
for i in range(1,target,1) :
    print('Number',i,'from thread',current_thread().getName())
