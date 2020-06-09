import mysql.connector


## Connect to the database from localhost (local machine), database name, user name and pwd.  
conn = mysql.connector.connect(host='localhost', database='mydb', user='root',password='Ferrsch56786934ferr')


db = 'mydb'
# check if the connection is successfully
if conn.is_connected():
    print('Connected to mysql database',db)
else :
    print('Connection to mysql database unsuccessful!')
    


# Database operations:
print('## Add data into the Database:')

# To do DB operations we need a cursor in python
cursor= conn.cursor()    

# add a row into the DB
try:
    cursor.execute("insert into employeeDB values(3,'maksim',30000)")  # execute the addition to the DB as if it was in the MySQL workbench
    conn.commit() # add all the mods to the DB at once. you need to do this commit() only at the end of all the executes!!!!
    print('Employee details added to DB.')

except :
    conn.rollback()  # roll back on the DB
    print('Employee couldn\'t be inserted into the DB.')

finally:   # close the DB regardless
    # Close the cursor
    cursor.close()
    
    # Close connection
    conn.close()