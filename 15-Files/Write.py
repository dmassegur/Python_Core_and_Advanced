# open the file for writing
f = open('myfile.txt', 'w')

s = input('Enter text: ')

f.write(s)

f.close()