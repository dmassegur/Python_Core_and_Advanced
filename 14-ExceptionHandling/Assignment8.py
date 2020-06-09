import logging

logging.basicConfig(filename = 'mylog.log', level = logging.DEBUG)

try :
    pswd = input('Enter your user password: ')
    
    logging.info('Verifying password length limit...')
    assert len(pswd) > 8, 'Wrong password: password must be at least 8 characters long. Please, try again...'
    
    
# except :
#     print('Wrong password: password must be at least 8 characters long. Please, try again later...')
#     logging.error('Wrong password: password must be at least 8 characters or more!')

except AssertionError as obj :
    print(obj)
    logging.error('Wrong password: password must be at least 8 characters or more!')
    
else :
    print('Password length is correct... Password has been saved...')
    logging.info('Password length is correct. Password saved.')