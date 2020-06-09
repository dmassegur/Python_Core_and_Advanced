class Flight:
    def __init__(self, engine):
        self.engine = engine
        
    def startEngine(self):
        self.engine.start()   ## it'll call method from another class!
    
    def startEngineMod(self):
        self.engine.start()   ## it'll call method from another class!
#         print(self.engine.x)
        return self.engine.x

class AirbusEngine:
    def start(self):
        print('Starting Airbus engine...')
        
class BoeingEngine:
    def start(self):
        print('Starting Boeing engine...')
            
class EngineMod:
    def start(self):
        self.x = 10  ## always the self. in front!!!
        print('hello test')
#         return self.x
        

# create the objects:

ae = AirbusEngine()
f = Flight(ae)  ## to this class Flight, we are passing object ae Class AirbusEngine rather than a value
f.startEngine()

be = BoeingEngine()
f2 = Flight(be)  ## to this class Flight, we are passing object ae Class BoeingEngine rather than a value
f2.startEngine()


bm = EngineMod()
g = Flight(bm)  
y = g.startEngineMod()
print(y)