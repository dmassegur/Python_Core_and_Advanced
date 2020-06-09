lst=[10,20.0,'david',-200,'kk']
print(lst)
print(lst[3])
print(lst[3:4]) #slicing on lists
print(lst*4)
print(len(lst))

lst.append(-31.24)
print(lst)
#lst.remove('David')
print(lst)
lst.remove('david')  # function on lists. hence why the dot
print(lst)
del(lst[2]); print(lst)  #in-built function in python. hence why not with dot

# lst.clear()
# print(lst)

lst.remove('kk')
print(max(lst))
print(min(lst))

lst.insert(2, 99)
print(lst)

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)