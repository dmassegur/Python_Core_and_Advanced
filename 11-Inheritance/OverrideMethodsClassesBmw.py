
class BMW:
    def __init__(self, make, mod, y):
        self.make = make
        self.model = mod
        self.year = y
       
    def start(self):  ## method is transfered to the lower-level classes
        print('Starting the car')
        
    def stop(self):  ## method is transfered to the lower-level classes
        print('Stop the car')
     
class ThreeSeries(BMW):  ## we need to add the parent class here too!!!!!
    def __init__(self, cruiseControl, mak, model, y):  ## because it's a class that inherites a higher class, we have to pass the fields of the other class here too
        BMW.__init__(self, mak, model, y)   ## the way to pass the inherited fields to the higher class
        self.cruiseControlEnabled = cruiseControl
        
    def displ(self):   ## this method (or instance) is only available for this class
        print(self.cruiseControlEnabled)

    def displ2(self):   ## this method (or instance) is only available for this class
        print('hello')
     
    def start(self):  ## method is transfered to the lower-level classes
        print('Button start')
   
class FiveSeries(BMW):  ## we need to add the parent class here too!!!!!
    def __init__(self, parkingAssist, mak, mod, yea):
        BMW.__init__(self, mak, mod, yea)   # in this case it's not actually necessary because ThreeSeries (called below) also calls BMW
        self.parkingAssistEnabled = parkingAssist

    def stop(self):  ## this method overwrite the one from BMW
        print('car won\'t stop.')

    def start(self):  ## this method overwrite the one from BMW
        print('Remote start')
        
# class FiveSeriesMod(BMW):
class FiveSeriesMod(ThreeSeries):  ## we need to add the parent class here too!!!!!
    def __init__(self, parkAssist, mak, model, y, cruiseContr):
#         BMW.__init__(self, mak, model, y)   # in this case it's not actually necessary because ThreeSeries (called below) also calls BMW
        ThreeSeries.__init__(self, cruiseContr, mak, model, y)
        self.parkingAssistEnabled = parkAssist

    def displ3(self):   ## this method (or instance) is only available for this class
        print('hi again')

        
        
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

print('')

c2 = FiveSeries(False,'BMW', '518d',2017)
print('Car two:')
print(c2.make)
print(c2.model)
print(c2.year)
print(c2.parkingAssistEnabled)
c2.start()
c2.stop()

print('')

bmw = FiveSeriesMod(True,'BMW', '530e',2018,True)
print('Car three:')
print(bmw.make)
print(bmw.model)
print(bmw.year)
print(bmw.parkingAssistEnabled)
print(bmw.cruiseControlEnabled)
bmw.start()  ## it inherited the one from Threeseries!
bmw.stop()
bmw.displ3()
bmw.displ()  ## I don't know why it doesn't inherit this method from the other class <-- it's because you had (BMW) in the class definition above and not (ThreeSeries) !!!!
