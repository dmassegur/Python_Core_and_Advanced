## Set and Get are to encapsulate the data in a class and makes the data (semi)private because only way to get is via method get.
class Student :
    def setId(self,nid):  ## method or instance
        self.id = nid
        
    def getId(self):    ## method or instance
        return self.id

    def setName(self,n):    ## method or instance
        self.name = n
        
    def getName(self):    ## method or instance
        return self.name


s = Student()
s.setId(345)
s.setName('dan')

print(s.getId())  ## it goes with () because you are calling a method not a var inside a class
print(s.getName()) 