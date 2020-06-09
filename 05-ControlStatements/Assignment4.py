x = int(input('Insert desired number: '))
a = 10
b = 100

print('-> Printing numbers from 1 to %d but skipping multiples of %d and not greater than %d:' %(x,a,b))
i=0
while i<x :
    i += 1

    if i%a==0 :
        continue
    if i>b :
        break
    print(i)
    
