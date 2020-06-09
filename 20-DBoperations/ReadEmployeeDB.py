import mysql.connector


## Connect to the database from localhost (local machine), database name, user name and pwd.  
conn = mysql.connector.connect(host='localhost', database='mydb', user='root',password='Ferrsch56786934ferr')


db = 'mydb'
# check if the connection is successful
if conn.is_connected():
    print('Connected to mysql database',db)
else :
    print('Connection to mysql database unsuccessful!')
    

# Close connection
conn.close()