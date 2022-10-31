import mysql.connector

try:
    connection=mysql.connector.connect(host='localhost',
                                       database='TU_PSI',
                                       user='root',
                                       password='KIFWAT', port= '3306')
    
    mySql_Create_Table_Query1 ="""CREATE TABLE TIPOS_DE_TERAPIA(ID INT PRIMARY KEY AUTO_INCREMENT,NOMBRE_RAMA VARCHAR(45))"""
    
    mySql_Create_Table_Query2 ="""CREATE TABLE UBICACION(ID INT PRIMARY KEY AUTO_INCREMENT,PROVINCIA VARCHAR(45))""" 
    
    mySql_Create_Table_Query3 ="""CREATE TABLE PACIENTE_CONSULTOR(DNI_PACIENTE INT UNIQUE NOT NULL,
                                                                 NOMBRE VARCHAR (100) NOT NULL,
                                                                 APELLIDO VARCHAR(100),
                                                                 EMAIL VARCHAR(45),
                                                                 TELEFONO BIGINT,
                                                                 FECHA_NAC DATE,
                                                                 SEXO VARCHAR (50),
                                                                 UBICACION_ID INT,CONSTRAINT PK_ID_PACIENTE PRIMARY KEY (DNI_PACIENTE),
                                                                 CONSTRAINT FK_UBICACION FOREIGN KEY (UBICACION_ID) REFERENCES UBICACION (ID))"""
    
                                                                  
    mySql_Create_Table_Query4 ="""CREATE TABLE PSICOLOGO(NOMBRE VARCHAR(100) NOT NULL,
                                                                 APELLIDO VARCHAR (100) NOT NULL,
                                                                 SEXO VARCHAR(15) NOT NULL,
                                                                 CUIL INT UNIQUE NOT NULL,
                                                                 FECHA_DE_NACIOMIENTO DATE,
                                                                 COLEGIO_REGULADOR VARCHAR(100) NOT NULL,
                                                                 EMAIL VARCHAR(45),
                                                                 CONTRASEÑA VARCHAR(8),
                                                                 TELEFONO BIGINT,
                                                                 UBICACION INT,
                                                                 TIPOS_DE_TERAPIA INT,
                                                                 PACIENTE_CONSULTOR INT,
                                                                 CONSTRAINT PK_CUIL PRIMARY KEY (CUIL),
                                                                 CONSTRAINT FK_UBIC_ID FOREIGN KEY (UBICACION) REFERENCES UBICACION (ID),
                                                                 CONSTRAINT FK_TIPOS_DE_TERAPIA FOREIGN KEY (TIPOS_DE_TERAPIA) REFERENCES TIPOS_DE_TERAPIA(ID),
                                                                 CONSTRAINT FK_PACIENTE_CONSULTOR FOREIGN KEY (PACIENTE_CONSULTOR) REFERENCES PACIENTE_CONSULTOR (DNI_PACIENTE))"""




    
    cursor = connection.cursor()
    result1 = cursor.execute(mySql_Create_Table_Query1)
    print("La tabla-TIPOS_DE_TERAPIA-se ha creado con exito")
    result2 = cursor.execute(mySql_Create_Table_Query2)
    print("La tabla-UBICACION-se ha creado con exito")
    result3 = cursor.execute(mySql_Create_Table_Query3)
    print("La tabla TABLE PACIENTE_CONSULTOR--se ha creado con exito")
    result4 = cursor.execute(mySql_Create_Table_Query4)
    print("La tabla TABLE PSICOLOGO-se ha creado con exito")

except mysql.connector.Error as error:
    print("Failed to create tables in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
