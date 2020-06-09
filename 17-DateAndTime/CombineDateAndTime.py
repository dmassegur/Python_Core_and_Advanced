from datetime import *

d = date(2018,7,27)
t = time(12,45,32)

dt = datetime.combine(d,t)
print(dt)