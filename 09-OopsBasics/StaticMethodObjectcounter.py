class ObjectCounter :
    
    numberOfObjects = 0   ## static field
    
    def __init__(self):
        ObjectCounter.numberOfObjects += 1
        
    @staticmethod    ## static method.  
    def displayCount():    ## static method doesn't require a self!
        print(ObjectCounter.numberOfObjects)
        
ob1 = ObjectCounter()
ob2 = ObjectCounter()        

ob1.displayCount()
ob2.displayCount()
ObjectCounter.displayCount()