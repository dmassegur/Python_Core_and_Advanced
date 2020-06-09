lst=[20,30,40,255]
print(type(lst))
b=bytes(lst)
print(type(b))
# b[2]=22   #bytes can't assign values

b1=bytearray(lst)
print(type(b1))
b1[2]=33
print(b1)