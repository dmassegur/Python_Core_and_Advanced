import mysql.connector


print('## Delete data from the Database via a def function:')

def deleteDB(id):
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
    
    str = "delete from employeeDB where id='%d'"
    args=id 
    # remove a row from the DB
    try:
        cursor.execute(str %(args))  # execute the string created above
#         cursor.execute( "delete from employeeDB where id='%d'" %(args) )
        
        conn.commit() # add all the mods to the DB at once. you need to do this commit() only once at the end of all the executes!!!!
        print('Employee deleted from DB.')
    except :
        conn.rollback()  # roll back on the DB
        print('Employee couldn\'t be deleted from the DB.')

    finally:   # close the DB regardless
        # Close the cursor
        cursor.close()
    
        # Close connection
        conn.close()
    
# Calling the delete function    
empID = int(input('Enter employee ID to be removed: '))
deleteDB(empID)