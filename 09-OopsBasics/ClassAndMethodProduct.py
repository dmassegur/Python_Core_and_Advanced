class Product:   ## class to define objects
    def __init__(self):   ## self is always refering to the properties of the class
        self.name = 'phone'   ## this is a public field
        self.description = 'it\'s awesome'   ## this is a public field
        self.price = 700   ## this is a public field
             
    def display(self):  ## instance or method!   ## self is always needed in a class
        print(self.name)
        print(self.price)
        print(self.description)

        
p1 = Product()  # p1 is an object that will adopt the values from the default class

print(p1)  # won't write correctly
print(p1.name)
print(p1.description)
print(p1.price)


p2 = Product()
p2.name = 'tablet'
p2.description = 'it\'s bad'
p2.price = 900

print(p2.name)
print(p2.description)
print(p2.price)

p3 = Product()
p3.display()
