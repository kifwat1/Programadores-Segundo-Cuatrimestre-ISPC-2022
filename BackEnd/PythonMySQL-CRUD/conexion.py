
import mysql.connector
from mysql.connector import Error
try:
    connection=mysql.connector.connect(host='localhost',
                                       database='TU_PSI',
                                       user='root',
                                       password='KIFWAT', port= '3306')
    
    if connection.is_connected():
        db_Info=connection.get_server_info()
        print("Connected to MySQL Server version", db_Info)
        cursor=connection.cursor()
        cursor.execute("select database();")
        record=cursor.fetchone()
        print("Se ha conectado a la base de datos: ", record)




except Error as e:
    print ("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
