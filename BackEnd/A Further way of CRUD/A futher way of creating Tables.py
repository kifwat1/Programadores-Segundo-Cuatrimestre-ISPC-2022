import mysql.connector
my_connection=mysql.connector.connect(host='localhost',
                                       database='TU_PSI',
                                       user='root',
                                       password='KIFWAT', port= '3306')
miCursor=my_connection.cursor()
"""miCursor.execute('''
                CREATE TABLE TIPOS_DE_TERAPIA(
                    ID INT PRIMARY KEY AUTO_INCREMENT,
                    NOMBRE_RAMA VARCHAR(45))''')"""

TIPOS_DE_TERAPIA= [
    (1,'Terapia Familiar'), 
    (2,'Terapia de pareja'),
    (3,'Individual'),
    (4,'Consulturia de empresas'),
    (5,'Deportiva')]

miCursor.executemany("INSERT INTO TIPOS_DE_TERAPIA VALUES(%s,%s)",TIPOS_DE_TERAPIA)
my_connection.commit()
print("Table Tipos de Terapia and dates are registred correctly")
my_connection.close()

#Inserting only one one value doesn´t work properly 
