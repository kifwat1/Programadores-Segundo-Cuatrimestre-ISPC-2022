import mysql.connector 

import mysql.connector

try:
    connection=mysql.connector.connect(host='localhost',
                                       database='TU_PSI',
                                       user='root',
                                       password='KIFWAT', port= '3306')

    mySql_insert_query = " DELETE FROM paciente_consultor  WHERE DNI_PACIENTE = '8888888';"

    
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "registro(s) borrado") 

except mysql.connector.Error as error:
    print("Failed to delete record from paciente_consultor {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
