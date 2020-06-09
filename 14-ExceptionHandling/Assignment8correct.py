import logging

logging.basicConfig(filename = 'mylog.log', level = logging.DEBUG)


class InvalidPasswordException(Exception):
    
    pass


def setPassword():
    
    pswd = input('Enter your user password: ')
    
    logging.info('Verifying password length limit...')
    if len(pswd) < 8 :
        raise InvalidPasswordException()



try :
    
    setPassword()    
    
# except :
#     print('Wrong password: password must be at least 8 characters long. Please, try again...')
#     logging.error('Wrong password: password must be at least 8 characters or more!')

except InvalidPasswordException :
    print('Wrong password: password must be at least 8 characters or more! Please, try again...')
    logging.error('Wrong password: password must be at least 8 characters or more!')
    
else :
    print('Password length is correct... Verifying user name an password...')
    logging.info('Password length is correct.')