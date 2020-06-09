class Student :
    def __init__(self):
        self.__id = 123   ## the __ makes the field private
        self.__name = 'david'
        
    ## to access the private fields, we create an instance method:
    def display(self):    
        print(self.__id)
        print(self.__name)


s = Student()
# print(s.id)  ## won't print because private
# print(s.name) ## won't print because private

s.display()

print(s._Student__id)  ## a workaround to print private fields in an object
print(s._Student__name)  ## a workaround to print private fields in an object