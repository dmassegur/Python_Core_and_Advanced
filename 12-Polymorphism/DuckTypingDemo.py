class Duck:
    def talk(self):
        print('quak quak')
        
class Human:
    def talk(self):
        print('hello')
        
def callTalk(obj):   ## it requires an object 
    obj.talk()  ## this is a dynamic (or polymorphic) function that calls the method inside different classes
    
d = Duck()     ## reminder! d is an object that uses a class!
callTalk(d);  ## ; does nothing

h = Human()
callTalk(h)

