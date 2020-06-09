from threading import *


### Create a thread via a Class

class MyThread() :
    
    def displayNumbers(self):  ## this method requires self because is inside the class!!!!
        i = 0
        print(current_thread().getName())
        while(i<=10) :
            print(i)
            i+=1

threadobj = MyThread()  ## we create an object with the class

t = Thread(target=threadobj.displayNumbers)      ## create the thread class
t.start()