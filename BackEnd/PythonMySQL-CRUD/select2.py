import mysql.connector

try:
    connection=mysql.connector.connect(host='localhost',
                                       database='TU_PSI',
                                       user='root',
                                       password='KIFWAT', port= '3306')

    mySql_query = "select * from psicologo where nombre like 'si'"
        
        


    cursor = connection.cursor()
    cursor.execute(mySql_query)
   
    rows=cursor.fetchall()
    for row in rows:
    	print(row)
    	

   
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
