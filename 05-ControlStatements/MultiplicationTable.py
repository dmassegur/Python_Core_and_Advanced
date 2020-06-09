x = int(input('Enter desired number for times table display: '))

print('\n-> Times table for number %d:' %x)
for i in range(1,11,1) :
    prod = x*i
    print('%dx%d = %d' %(x,i,prod))
    