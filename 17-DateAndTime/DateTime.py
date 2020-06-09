import time
import datetime


print('time module:')

epochsecs = time.time()  # current time in seconds
print('Time in seconds: ',epochsecs)

t = time.ctime(epochsecs)  # current time in date and time
# t = time.ctime(time.time())  # does the same
print(t)

print('')
print('datetime module:')

dt = datetime.datetime.today()
print(dt)
print(dt.day,dt.month,dt.year)
print(dt.hour,dt.minute,dt.second)
print('Current date: %d-%d-%d' %(dt.day,dt.month,dt.year))
print('Current date: {}-{}-{}' .format(dt.day,dt.month,dt.year))
print('Current time: %d:%d:%2d' %(dt.hour,dt.minute,dt.second))
print('Current time: {}:{}:{}' .format(dt.hour,dt.minute,dt.second))

