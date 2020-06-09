s='   You are awesome.   '
print(s)

s1=''' You are the 
creator of your 
destiny. '''
print(s1)

print(s[5])
print(s*3)

print(len(s1))

# slicing!
print(s[0:5]) # counts 5 from element index (which is 0)
print(s[0:])
print(s[7:len(s)])
print(s[-3:-1])  # count 3 from the last element index (which is -1)

print(s[0:12:3]) # steps of 3
print(s[len(s)::-1]) # steps backwards
print(s[::-1]) # len is not needed

# remove spaces at the end and/or the beginning
s2= s.strip()
print(s2)
s2= s.lstrip()
print(s2)
s2= s.rstrip()
print(s2)

print(s.find('awe',0,len(s))) # tries to find awe in string
print(s.find('awe',0,8))   # tries to find awe in string from indices 0 to 8 --> returns -1 if it's not found
print(s.count('a'))  # counts number of a
print(s.replace('awe','ewa'))  # replace feature inside string

print(s.upper())
print(s.lower())
print(s.title())