def calc(par1, par2) :
    summ = par1+par2
    minus = par1-par2
    prod = par1*par2
    div = par1/par2
    avg = (par1+par2)/2
    
    return summ, minus, prod, div, avg

x = 10
y = 20
calcxy = calc(x,y)

print(x,y,'->',calcxy)

print('Operations for numbers %0.1f and %0.1f are:' %(x,y))
print('Sum %0.1f + %0.1f = %0.1f.' %(x,y,calcxy[0])) 
print('Subtraction %0.1f - %0.1f = %0.1f.' %(x,y,calcxy[1]))
print('Product %0.1f x %0.1f = %0.1f.' %(x,y,calcxy[2]))  
print('Division %0.1f / %0.1f = %0.1f.' %(x,y,calcxy[3]))  
print('Average %0.1f and %0.1f = %0.1f.' %(x,y,calcxy[4])) 

for i in calcxy :
    print(i)
# for i in range(0,len(calcxy),1) :
#     print(calcxy[i])