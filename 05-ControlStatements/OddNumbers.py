x = int(input('Enter min number: '))
y = int(input('Enter max number: '))

i = x
count = 0
while i<=y :
    if i%2!=0 :
        print('Odd number found: %d' %(i))
        count += 1
    i += 1   
    
print('Total odd numbers found between inserted numbers: %d' %(count))
