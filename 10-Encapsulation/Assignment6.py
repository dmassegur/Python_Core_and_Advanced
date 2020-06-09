class Patient:
    def __init__(self):  ## not necessary in this case
        self.init = []   ## not necessary in this case
        
    def setId(self,pid):    
        self.id = pid   ## this is a field and is made private with set and only accessible with get
        
    def getId(self):
        return self.id   ## private field set is only accessible with get
    
    def setName(self,n):
        self.name = n
        
    def getName(self):
        return self.name
    
    def setSSN(self,ssn):
        self.ssn = ssn
        
    def getSSN(self):
        return self.ssn
    
p = Patient()

p.setId(int(input('Enter patient ID: ')))
p.setName(input('Enter patient\'s name: '))
p.setSSN(int(input('Enter patient SSN: ')))

print( 'Patient %s, with ID %d, has SSN number: %d' %(p.getName(), p.getId(), p.getSSN()) )
# print( 'Patient ' + str(p.getName()) + ', with ID '+ str(p.getId()) + ', has SSN number: '+ str(p.getSSN()) )


#print(p.init)