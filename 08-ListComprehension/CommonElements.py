## find common elements in a list
a = [1,2,3,4,5]
b = [6,2,4,9,10]

common_els = []
for i in range(0,len(a),1) :
    for j in range(0,len(b),1) :
        if a[i] == b[j] :
            common_els.append(a[i])

print('Common elements between lists',a,'and',b,'are:',common_els,'-> classic way through fors and if')        

## more efficient method than above
common_els2 = []
for i in a :
    if i in b :
        common_els2.append(i)

print('Common elements between lists',a,'and',b,'are:',common_els2,'-> more efficient if and for loops')        


common_els3 = [ a[i] for i in range(0,len(a),1) if a[i] in b ]
print('Common elements between lists',a,'and',b,'are:',common_els3,'-> using list comprehension')        

common_els4 = [ i for i in a if i in b ]
print('Common elements between lists',a,'and',b,'are:',common_els4,'-> using more efficient list comprehension')        
