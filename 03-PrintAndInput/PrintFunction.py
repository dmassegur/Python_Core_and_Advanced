print()
print('hello '*3)
print('hello\n everyone')

a,b=10,20
print(a,b)  # default separator is a space
print(a,b,sep='')
print(a,b,sep=',')
print(a,b,sep=' +*- ')

name='John'
marks=94.56789542

print(name,marks)
print('Name is',name,'Marks are',marks)

print('Name is %s, Marks are %f' %(name,marks))
print('Name is %s, Marks are %.2f' %(name,marks))

print('Name is {}, Marks are {}'.format(name,marks))
print('Name is {0}, Marks are {1}'.format(name,marks))


x='1'
y='2'
print(x+y,end=' ')  ## adding end= the next print is a continuation
print(y)

x='1'
y='2'
print(x+y,end='3')  ## adding end= the next print is a continuation
print(y)

x='1'
y='2'
print(x+y)  ## without the , end the next print goes to the bottom
print(y)


x=3; print(x)
y=2;