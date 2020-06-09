dict1={1:'kk', 2:'hello', 3:'bye'}  # key: value
print(dict)

print(dict1.items())

k= dict1.keys()
for i in k:
    print(i)
    
v= dict1.values()
for i in v:
    print(i) 

print(dict1[3])  #with index you can access only the values!
print(dict1[1])

del dict1[3]
print(dict1)