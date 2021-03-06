from abc import abstractclassmethod  ## import this module for abstract methods
from abc import ABC

print('## An interface is a class with all the methods abstract!!')
print('## If all the methods in a class are abstract, that class becomes an interface!!!')
print('## Consequently, all the child classes must also include all those methods in them!!!')
print('## Yet, the child classes can have additional methods.')

class BMW(ABC):   ## add module ABC import
    def __init__(self, make, mod, y):
        self.make = make
        self.model = mod
        self.year = y
    
    @abstractclassmethod   
    def start(self):  ## method is transfered to the lower-level classes
    ##    print('Starting the car')
        pass

    @abstractclassmethod    
    def stop(self):  ## method is transfered to the lower-level classes
    ##    print('Stop the car')
        pass   
        
    @abstractclassmethod      ## to assign an abstractmehod   this abstract will be mandatory
    def drive(self):   ## we can use pass if we don't want to pass any parameter
        pass


     
class ThreeSeries(BMW):
    def __init__(self, cruiseControl, mak, model, y):  ## because it's a class that inherites a parent class, we have to pass the fields of the other class here too
        super().__init__(mak, model, y)   ## the way to pass the inherited fields to the higher class
        self.cruiseControlEnabled = cruiseControl
        
    def displ(self):   ## this method (or instance) is only available for this class
        print(self.cruiseControlEnabled)

    def displ2(self):   ## this method (or instance) is only available for this class
        print('hello')
     
    print('\n## All the sub-classes need to have the same methods as the parent interface!!!') 
    def start(self):  ## method is transfered to the lower-level classes
        super().start()   ## calls the method from the parent class (BMW)
        print('Button start')
        
    def stop(self):  ## method is transfered to the lower-level classes
        super().start()   ## calls the method from the parent class (BMW)
        print('Button stop')

    def drive(self):
        print('Three Series is being driven.')
        
   
class FiveSeries(BMW):
    def __init__(self, parkingAssist, mak, mod, yea):
        super().__init__(mak, mod, yea)   # in this case it's not actually necessary because ThreeSeries (called below) also calls BMW
        self.parkingAssistEnabled = parkingAssist

    ## all the sub-classes need to have the same methods as the parent interface!!!
    def stop(self):  ## this method overwrite the one from BMW
        print('car won\'t stop.')

    def start(self):  ## this method overwrite the one from BMW
        super().start()  ## calls the method from the higher-level class (BMW)
        print('-> Remote start')
        
        
    def drive(self):
        print('Three Series is being driven.')


        
class FiveSeriesMod(ThreeSeries):
    def __init__(self, parkAssist, mak, model, y, cruiseContr):
#         super().__init__(mak, model, y)   # in this case it's not actually necessary because ThreeSeries (called below) also calls BMW
        ThreeSeries.__init__(self, cruiseContr, mak, model, y)
        self.parkingAssistEnabled = parkAssist

    def displ3(self):   ## this method (or instance) is only available for this class
        print('hi again')


print('')        
        
c = ThreeSeries(True,'BMW', '328i',2019)
print('Car one:')
print(c.make)
print(c.model)
print(c.year)
print(c.cruiseControlEnabled)
c.start()
c.stop()
c.displ()
c.displ2()
c.drive()

print('')

c2 = FiveSeries(False,'BMW', '518d',2017)
print('Car two:')
print(c2.make)
print(c2.model)
print(c2.year)
print(c2.parkingAssistEnabled)
c2.start()
c2.stop()
c2.drive()  ## abstract class

print('')

c3 = FiveSeriesMod(True,'BMW', '530e',2018,True)
print('Car three:')
print(c3.make)
print(c3.model)
print(c3.year)
print(c3.parkingAssistEnabled)
print(c3.cruiseControlEnabled)
c3.start()  ## it inherited the one from BMW and not the one from threseries!
c3.stop()
c3.displ3()
c3.displ()  ## I don't know why it doesn't inherit this method from the other class.


