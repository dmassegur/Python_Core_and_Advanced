## Elementwise product of two lists
a = [1,2,3,4,5]
b = [6,7,8,9,10]

## classical way
z = []
for i in range(0,len(a),1) :
    z.append(a[i]*b[i])
    
print(z,'-> using classic way')

## Comprehension
z2 = [a[i]*b[i] for i in range(0,len(a),1)]
print(z2,'-> using list comprehension')