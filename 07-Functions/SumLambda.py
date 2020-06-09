def naive_sum(par1, par2): 
#     result = par1+par2
#     return result
    return par1+par2

x = 3
y = 4
z = naive_sum(x,y)

print('Sum of %0.1f + %0.1f = %0.1f, using function.' %(x,y,z))

lambda_sum = lambda p1,p2 : p1+p2
z2 = lambda_sum(x,y)

print('Sum of %0.1f + %0.1f = %0.1f, using lambda.' %(x,y,z2))
