## Class inside a Class

class Car :   ## this is the outer class
    def __init__(self,make,year):
        self.make = make
        self.year = year
        
    class Engine :   ## this is the inner class
        def __init__(self, number):
            self.number = number
            
        def start(self):    ## instance (or method) of the inner class
            print('Engine started')


## displaying outer Class
outerC = Car('bmw',1971)
print(outerC.make)
print(outerC.year)

## displaying inner Class
innerC = outerC.Engine(123)
print(innerC.number)
innerC.start()