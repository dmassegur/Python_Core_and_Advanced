
try :

    f = open('myfile.txt','w')
    a,b = [int(x) for x in input('Enter two numbers with spaces:').split()]  ## split(',') if you want to separate thme by ,
    c = a/b
    print(c)
    print('Writing %0.1f into file...' %(c))
    f.write('%0.1f written here.' %(c)) 
    f.close()  ## the file must always be closed!!! but if a exception happens between open and close, it won't be closed! -> solution: add a finally clause (see below)
    print('... done.')
    
except ZeroDivisionError :   ## write this is if the exception is of division by zero
    print('Division by zero is not allow!')
    print('Please enter a non-zero second number')
# except   ## use except alone for any general exception
    
else :    ## this is only executed if the exception doesn't happen
    print('You have entered a non zero 2nd number.')
        
finally:   ## this is executed regardless
    f.close()  ## the file will also be closed in case of an exception.
    print('File closed.')
    
print('Code after the exception has been printed...')