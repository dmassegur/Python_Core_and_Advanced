import logging   ## this import is necessary!!

# this is to generate a log file for debugging
logging.basicConfig(filename = 'mylog.log', level = logging.ERROR)
logging.critical('Critical')
logging.error('Error')
logging.warning('Warning')
logging.info('Info')
logging.debug('Debug')

## whatever starts with logging.   is written in the log file
## however, it only writes the logs above the one specified in the second field. in this case, because we enter .ERROR, it only write critical and error and omit the ones below error


logging.basicConfig(filename = 'mylog.log', level = logging.DEBUG)
logging.critical('Critical')
logging.error('Error')
logging.warning('Warning')
logging.info('Info')
logging.debug('Debug')

## in this case, it will print in the log file all the errors above Debug.