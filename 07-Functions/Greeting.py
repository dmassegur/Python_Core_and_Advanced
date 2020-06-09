def display(name) :
    
    def message() :
        return 'hello '
    
    result = message()+name+'!'
    return result

print(display('david'))
# print(message())  # doesn't work because message() is only inside the other function!