## classic way
lst = []
for x in range(1,11,1) :
    lst.append(x**3)
     
print(lst)

## using a comprehension:
# lst2 = []
lst2 = [x**3 for x in range(1,11,1)]
print(lst2)