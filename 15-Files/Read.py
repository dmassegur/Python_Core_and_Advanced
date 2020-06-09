import os, sys

# Check if the file exists
if os.path.isfile('myfile.txt') :
    
    # If exists
    # Read a file
    f = open('myfile.txt','r')
    
else : 
    print('File does not exist.')
    sys.exit()  ## to exit the run
    

s = f.read()  ## reads all the lines!
print(s)

s = f.readline()  ## reads one line!
print(s)


f.close()