## How to create a customised exception

class OverTheLimitException(Exception) :
    #def __init__(self):
    pass   ## you can use pass in a class if you don't have to pass any parameter/field, so to avoid def __init__(self)


def withdrawal(amount):
    print('You have requested: \u00a3%0.2f.' %(amount))
    
    if amount>500 :
        raise OverTheLimitException()
    
    
    
try :
    withdrawal(float(input('Enter the amount of cash you would like to withdraw: ')))
    
except OverTheLimitException :
    print(u'The withdrawal limit in this cash machine is of \u00a3500. Please, insert a smaller amount.')
    
else :
    print('Please, collect your money.')
    
finally :
    
    print('Thank you for using this cash machine. Have a good day.')
    
