import sys

lst = sys.argv
print('Arguments are: ', lst)
prod = 1
for i in range(1,len(lst)) :
    prod *= int(lst[i])

print('Product of arguments is:', prod)