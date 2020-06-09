class Student:  ## class
    major = 'CSE'  ## static field
    
    def __init__(self,rollnumb,na):
        self.rollnumb = rollnumb
        self.name = na
        
    
s1 = Student(23,'david')  ## object
s2 = Student(45,'marija')  ## object
print(s1.major)  ## static fields adopt the same value for all the objects
print(s1.rollnumb)
print(s1.name)
print(s2.major)
print(s2.rollnumb)
print(s2.name)

print(Student.major) 
