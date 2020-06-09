from threading import * ##Thread


### Creating a Thread via a Class

class MyThread(Thread):   ## we pass Thread function into this class
    
    def run(self):
        i = 0
        print(current_thread().getName())   ## not necessary
        while(i<=10) :
            print(i)
            i+=1

t = MyThread()

t.start()  ## you have to invoke the start method to call the thread. If you invoke run(), it will do it on the main thread!!!