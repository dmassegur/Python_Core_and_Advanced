from functools import *   # reduce function has to be imported!

lst=[5,10,15,20]

sum_list = float(reduce(lambda x,y:x+y, lst))   # float is actually not needed!
print('Factorial sum of list',lst,'is:',sum_list)

prod_list = float(reduce(lambda x,y:x*y, lst))
print('Factorial product of list',lst,'is:',prod_list)

div_list = reduce(lambda x,y:x/y, lst)
print('Factorial division of list',lst,'is:',div_list)

#!!! You could also use import functools and then  invoke functools.reduce(lambda ...)