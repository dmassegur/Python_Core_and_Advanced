print('## Small program to determine whether a number is prime: ##')
x = int(input('-> Enter the desired number: '))

primeflag = True
for i in range(2,x,1) :
    if x%i==0 :
        primeflag = False
        break

if primeflag :
    print('Inserted number %d is prime because it can only be divided by itself!' %(x))
else :
    print('Inserted number %d is not prime because it can be divided by %d!' %(x,i))  
    

dividers = []
for i in range(2,x,1) :
    if x%i==0 :
        primeflag = False
        dividers.append(i)

if primeflag :
    print('Inserted number %d is prime because it can only be divided by itself!' %(x))
else :
    print('Inserted number',x, 'is not prime because it can be divided by', dividers)  

    
print('\n## Deciding all the prime numbers up to chosen number %d' %(x))
j = 1    
primeflag = True
while j<=x :
    for i in range(2,j,1) :
        if j%i==0 :
            primeflag = False
            break
    
    if primeflag :
        print('Number %d is prime.  It can only be divided by itself!' %(j))
    else :
        print('Number %d is not prime.  It can be divided by %d!' %(j,i))  
    
    j += 1    
    primeflag = True
    