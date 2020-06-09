class Programmer:   ## getter and setter instances in a class
    ##def __init__(self):
    def setName(self, na):
        self.name = na
        
    def getName(self):    
        return self.name
    
    def setSalary(self,sal):
        self.salary = sal
        
    def getSalary(self):
        return self.salary
    
    def setTechnologies(self,techs):
        self.technologies = techs
        
    def getTechnologies(self):
        return self.technologies
    
p1 = Programmer()
p1.setName('david')
p1.setSalary(10000)
p1.setTechnologies(['java','matlab','python','fortran'])
                    
print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())