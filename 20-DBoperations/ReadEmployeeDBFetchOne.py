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

# To do DB operations we need a cursor in python
cursor= conn.cursor()    

# execute the db and put it in the cursor
cursor.execute('select * from employeeDB')  # it's the same command to read as in the MySQL Workbench

# fetch each row from the DB in the cursor one by one, using a while loop
row = cursor.fetchone()
# Display row and fetch next one until the end:
while row is not None:   # this will stop when the row becomes NOne, ie. nothing else is fetched
    print(row)
    row=cursor.fetchone()  # fetch the next record

# Close the cursor
cursor.close()

    
# Close connection
conn.close()