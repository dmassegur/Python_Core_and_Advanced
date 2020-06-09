from threading import *
from time import sleep


## Multi-threading: invoke different threads.

class MyThread() :
    
    def displayNumbers(self):  ## this method requires self because is inside the class!!!!
        i = 0
        print(current_thread().getName())
        sleep(1)  ## put thread to sleep
        while(i<=10) :
            print(i)
            i+=1

threadobj = MyThread()  ## we create an object with the class

t1 = Thread(target=threadobj.displayNumbers)      ## create the thread class
t1.start()

t2 = Thread(target=threadobj.displayNumbers)      ## create the thread class
t2.start()

t3 = Thread(target=threadobj.displayNumbers)      ## create the thread class
t3.start()