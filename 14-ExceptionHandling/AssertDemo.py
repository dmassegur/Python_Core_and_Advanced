import logging

logging.basicConfig(filename = 'mylog.log', level = logging.DEBUG)

try :
    num = int(input('Enter an even number: '))
    logging.info('Asserting even number...')
    assert num%2==0, 'Assertion error: You have entered an odd number!'

except AssertionError as obj:
    print(obj)
    logging.error('Assertion error: odd number entered.')
    
    
print('You entered:', num) ## since we have added the exception, this print will be executed