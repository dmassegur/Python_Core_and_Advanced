class BMW:
    def __init__(self, make, mod, y):
        self.make = make
        self.model = mod
        self.year = y
        
class ThreeSeries(BMW):  ## we need to add the parent class here too!!!!!
    def __init__(self, cruiseControl, mak, model, y):  ## because it's a class that inherites a higher class, we have to pass the fields of the other class here too
        BMW.__init__(self, mak, model, y)   ## the way to pass the inherited fields to the higher class
        self.cruiseControlEnabled = cruiseControl
        
class FiveSeries(BMW):  ## we need to add the parent class here too!!!!!
    def __init__(self, parkingAssist, mak, mod, yea):
        BMW.__init__(self, mak, mod, yea)   # in this case it's not actually necessary because ThreeSeries (called below) also calls BMW
        self.parkingAssistEnabled = parkingAssist
        
class FiveSeriesMod(BMW):  ## we need to add the parent class here too!!!!!
    def __init__(self, parkAssist, mak, model, y, cruiseContr):
        BMW.__init__(self, mak, model, y)   # in this case it's not actually necessary because ThreeSeries (called below) also calls BMW
        ThreeSeries.__init__(self, cruiseContr, mak, model, y)
        self.parkingAssistEnabled = parkAssist
        
        
c = ThreeSeries(True,'BMW', '328i',2019)
print('Car one:')
print(c.make)
print(c.model)
print(c.year)
print(c.cruiseControlEnabled)

print('')

c2 = FiveSeries(False,'BMW', '518d',2017)
print('Car two:')
print(c2.make)
print(c2.model)
print(c2.year)
print(c2.parkingAssistEnabled)

print('')

c3 = FiveSeriesMod(True,'BMW', '530e',2018,True)
print('Car three:')
print(c3.make)
print(c3.model)
print(c3.year)
print(c3.parkingAssistEnabled)
print(c3.cruiseControlEnabled)