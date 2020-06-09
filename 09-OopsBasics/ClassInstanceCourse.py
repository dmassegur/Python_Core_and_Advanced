class Course :   ## class to define objects
    def __init__(self,name,ratings):
        self.name = name   ## this is a public field
        self.ratings = ratings  ## this is a public field
    
    def average(self):    ## !!! this is an instance or method!!!   ## self is always needed in a class
        numberOfRatings = len(self.ratings)  ## we need self because we are passing some vars
        avg = sum(self.ratings) / numberOfRatings
        print('Average Ratings for',self.name,'is:',avg)
        
        
c1 = Course('java course',[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

print('')

c2 = Course('matlab course',[2,3,4,5])
print(c2.name)
print(c2.ratings)
c2.average()


