from datetime import date

d1 = date(2016,3,30)
d2 = date(2020,1,20)
d3 = date(2018,7,30)
d4 = date(2018,3,30)
d5 = date(2018,3,12)

ldates = []  # list initialization
# we append the dates in the created list
ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)
ldates.append(d5)

ldates.sort()  # sorts the different dates

for i in ldates :
    
    print(i)
    

