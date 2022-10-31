
#Insercion multimples,insercion de varios registros a la vez

import mysql.connector

try:
    connection=mysql.connector.connect(host='localhost',
                                       database='TU_PSI',
                                       user='root',
                                       password='KIFWAT', port= '3306')

    mySql_insert_query = """INSERT INTO PSICOLOGO (NOMBRE, APELLIDO, SEXO, CUIL, FECHA_DE_NACIOMIENTO, COLEGIO_REGULADOR, EMAIL, CONTRASEÑA, TELEFONO)
                           VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s)"""

    records_to_insert =[('Sigmund', 'Freud', 'Hombre', 5124541, '1958-01-01', 'Colegio de Freud','freud@gmail.com','freud999',747474)]
                         ####Ejemplos para probar el funcionamiento del registro.
 

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into PSICOLOGO table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

