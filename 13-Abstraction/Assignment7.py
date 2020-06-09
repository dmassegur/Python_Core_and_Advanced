## Abstraciton and Inteface Assignment for HP and DELL laptops
## Exercise already includes method override!

class TouchScreenLaptop():
    
    def __init__(self, mak, mod, y):
        self.make = mak
        self.model = mod
        self.year = y
        
    def scroll(self):
        print('Scroll option not yet known.')
        
    def click(self):
        print('Click option not yet known.')
        
    def test(self):
        print('test')
 
        
class HP(TouchScreenLaptop):
    
    def __init__(self, mak, mod, y, scroll):        
        TouchScreenLaptop.__init__(self, mak, mod, y)
        self.scrol =  scroll
        
    def scroll(self):
        if self.scrol :
            print('Scroll available on this HP laptop.')
        else :
            print('Scroll not available on this HP laptop.')
            
            
class DELL(TouchScreenLaptop):
    
    def __init__(self, mak, mod, y, scroll ):        
        TouchScreenLaptop.__init__(self, mak, mod, y)
        self.scrol =  scroll
        
    def scroll(self):
        if self.scrol :
            print('Scroll available on this DELL laptop.')
        else :
            print('Scroll not available on this DELL laptop.')
            

class HPNotebook(HP):
    def __init__(self, mak, mod, y, scroll, click):
        HP.__init__(self, mak, mod, y, scroll)
        self.clic = click
        
    def click(self):
        if self.clic :
            print('Click available on this HP Notebook.')
        else :
            print('Click unavailable on this HP Notebook.')
            
class DELLNotebook(DELL):
    def __init__(self, mak, mod, y, scroll, click):
        DELL.__init__(self, mak, mod, y, scroll)
        self.clic = click
        
    def click(self):
        if self.clic :
            print('Click available on this DELL Notebook.')
        else :
            print('Click unavailable on this DEL Notebook.')


            
print('')

c1 = HP('HP','touchscreen', 2020, True)
c1.scroll()
# c1.test()

c2 = DELL('DELL','non touchscreen', 2018, False)
c2.scroll()

print('')

c1 = HPNotebook('HP','touchscreen', 2020, True, False)
c1.scroll()
c1.click()     

c2 = DELLNotebook('DELL','non touchscreen', 2018, False, True)
c2.scroll()
c2.click()