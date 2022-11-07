
#Insercion multimples,insercion de varios registros a la vez
#Insert various dates using lists and tuples


import mysql.connector

try:
    connection=mysql.connector.connect(host='localhost',
                                       database='TU_PSI',
                                       user='root',
                                       password='KIFWAT', port= '3306')

    mySql_insert_query = """INSERT INTO PSICOLOGO (NOMBRE, APELLIDO, EMAIL, CONTRASEÑA, MATRICULA, SEXO, UBICACION, TIPOS_DE_TERAPIA, PACIENTE_CONSULTOR)
                           VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s)"""

    records_to_insert =[
        ('Sigmund', 'Freud','freud@gmail.com','freud88',75689, 'Masculino', 1, 1,208963578),
        ('Fernanda', 'Alonso', 'Alonso@gmail.com','alonso88',689687,'Feminino', 2, 2, 208963578)]
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

