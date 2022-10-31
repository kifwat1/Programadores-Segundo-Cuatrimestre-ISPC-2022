
###THIS FILE IS USED FOR PRACTICE (FOR THE TEAM)
###ESTE ARCHIVO SOLAMENTE PARA PRACTICAR (PARA EL EQUIPO) 

import mysql.connector

try:
    connection=mysql.connector.connect(host='localhost',
                                       database='TU_PSI',
                                       user='root',
                                       password='KIFWAT', port= '3306')

    #insertando datos en la tabla/ insertar fila simple

   
    mySql_insert_query = """INSERT INTO PACIENTE_CONSULTOR(DNI_PACIENTE,NOMBRE,APELLIDO,EMAIL,TELEFONO,FECHA_NAC,SEXO ) VALUES
(8888888, 'Taoufik','Saidi', 'esun-mail-deprueba@gnail.com', 045678987,'1999-01-01','Masculino');"""

         
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)

    connection.commit()
    print(cursor.rowcount, "Records inserted successfully into PACIENTE_CONSULTOR  table")    
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into PACIENTE_CONSULTOR  table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

