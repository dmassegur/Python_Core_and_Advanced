tpl=(50, 400,-10, 'xyz',50)
print(tpl)
print(tpl*3)
print(tpl[3])
print('Tuples cannot be modified!!!')

print(tpl.count(-10))
print(tpl.count(50))
print(tpl.index('xyz'))
print(tpl.index(50))

lst=[67, 34,'xss']
print(type(lst))
tpl2=tuple(lst)
print(type(tpl2))
lst2=list(tpl2)
print(type(lst2))


tpl2 = (34,)
print(type(tpl2))
