from threading import *  ##Thread


### Creating a Thread via a function

def displayNumbers():  ## any function
    i = 0
    print(current_thread().getName())
    while(i<=10) :
        print(i)
        i+=1
        

print(current_thread().getName())  ## printing the current thread
        
t = Thread(target=displayNumbers)  ## we create a new thread that calls that function

t.start()  # run the thread with start.


