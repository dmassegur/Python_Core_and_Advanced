import mysql.connector
from builtins import list


print('## Update data of a  Database row via a def function:')

def updateDB(id,name,salary):
    ## Connect to the database from localhost (local machine), database name, user name and pwd.  
    conn = mysql.connector.connect(host='localhost', database='mydb', user='root',password='Ferrsch56786934ferr')


    db = 'mydb'
    # check if the connection is successfully
    if conn.is_connected():
        print('Connected to mysql database',db)
    else :
        print('Connection to mysql database unsuccessful!')
    


    # Database operations:

    # To do DB operations we need a cursor in python
    cursor= conn.cursor()    
    
    str1 = "UPDATE employeeDB SET salary='%d' WHERE id='%d'"   # update the salary column on row id
    str2 = "UPDATE employeeDB SET name='%s' WHERE id='%d'"     # update the name column on row id
    # update a row from the DB
    try:
        cursor.execute(str1 %(salary,id))  # execute the string created above
        cursor.execute(str2 %(name,id))    # execute the string created above

        conn.commit() # add all the mods to the DB at once. you need to do this commit() only once at the end of all the executes!!!!
        print('Employee ID %d updated in DB successfully.' %(id) )
    except :
        conn.rollback()  # roll back on the DB
        print('Employee ID %d couldn\'t be updated into the DB.' %id)

    finally:   # close the DB regardless
        # Close the cursor
        cursor.close()
    
        # Close connection
        conn.close()
    
# Calling the delete function    
empIDdetails = list(input('Insert new details for the employee that needs update [id,name,salary]: ').split(','))
# print(empIDdetails); # print(len(empIDdetails)); # print(type(empIDdetails)) ;# print(empIDdetails[0])
updateDB( int(empIDdetails[0]) , str(empIDdetails[1]) , int(empIDdetails[2]) )