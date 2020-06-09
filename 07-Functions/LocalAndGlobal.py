x = 123   # this is a global variable

def display() :
    x = 670  # because x is global it won't get modified here
    print(x)  # it will print x because x is global!!!
    y = 678  # y is local!
    print(globals()['x'])  # prints the global variable
    
print(x)
display()
print(x)

print('\n')
z = display
z()