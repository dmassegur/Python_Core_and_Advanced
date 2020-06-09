s={10,20,'dfdg',20}
print(s)
print(type(s))
print(' sets do not allow duplicates!!!!')

s.update([88,99])
print(s)
# print(s*4)
# print(s[:5])

s.remove(20)

fs= frozenset(s)
print(fs)
# fs.update([3])
# fs.remove(30)