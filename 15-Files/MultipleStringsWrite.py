# open the file for writing
f = open('myfile.txt', 'w')

print('Enter text (Type # at the end.):')

s = ''
while '#' not in s :
    s = input()
    f.write(s+'\n')

f.close()