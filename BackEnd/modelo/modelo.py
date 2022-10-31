import mysql.connector

class Conectar():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(host='localhost',
                                       database='TU_PSI',
                                       user='root',
                                       password='KIFWAT', port= '3306')

          
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)

#PRIMERA OPERACIÓN DEL CRUD: CREATE O INSERT.
    def InsertarValor(self, NOMBRE, APELLIDO, SEXO, CUIL, FECHA_DE_NACIOMIENTO, COLEGIO_REGULADOR, EMAIL, CONTRASEÑA, TELEFONO):
       
       if self.conexion.is_connected():
           
        try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "INSERT INTO PSICOLOGO VALUES(%s,%s, %s, %s, %s,%s, %s, %s, %s)"
                data= ('Fernando', 'Alonso', 'Hombre', 78999, '1988-01-01', 'Colegio de Freud','alonso@gmail.com','alonso88',142536475869)

                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.close()
                print("El tipo de terapia se ha guardado correctamente")

        except:
            print("No se pudo concectar a la base de datos")
   
#SEGUNDA OPERACION DEL CRUD: READ O LEER
    def BuscarObjeto(self, Nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "SELECT * from psicologo where nombre like 'sliman' "
                cursor.execute(sentenciaSQL)
                resultadoREAD = cursor.fetchall() #La variable del resultado
                self.conexion.close()
                return resultadoREAD

            except:
                print("No se pudo concectar a la base de datos")

#CUARTA OPERACION DEL CRUD: DELETE O ELIMINAR
    def EliminarObjeto(self, Nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from psicologo  where CUIL=4124541 "
                cursor.execute(sentenciaSQL)

                self.conexion.commit()                
                self.conexion.close()
            except:
                print("No se pudo concectar a la base de datos")
