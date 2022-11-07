import mysql.connector

class Conectar():
    def __init__(self)-> None:
        try:
            self.conexion = mysql.connector.connect(host='localhost',
                                       database='TU_PSI',
                                       user='root',
                                       password='KIFWAT', port= '3306')

          
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)

#PRIMERA OPERACIÓN DEL CRUD: CREATE O INSERT.
    def InsertarValor(self,NOMBRE, APELLIDO, EMAIL, CONTRASEÑA, MATRICULA, SEXO, UBICACION, TIPOS_DE_TERAPIA, PACIENTE_CONSULTOR):
        
        if self.conexion.is_connected():
            try:
                
                cursor = self.conexion.cursor()
                sentenciaSQL= "INSERT INTO PSICOLOGO VALUES(%s,%s, %s, %s, %s,%s, %s, %s, %s)"
                data= ('Carolina', 'Alonso', 'Carolina@gmail.com','Carolina88',689687,'Feminino', 2, 2, 999999)

                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.close()
                print("Los datos se  han guardado correctamente")

            except:
                print("No se pudo concectar a la base de datos")
   
#SEGUNDA OPERACION DEL CRUD: READ O LEER
    def BuscarObjeto(self, Nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "SELECT * from PSICOLOGO where nombre like 'sliman' "
                cursor.execute(sentenciaSQL)
                resultadoREAD = cursor.fetchall() #La variable del resultado
                self.conexion.close() 
                return resultadoREAD
            except:
                print("No se pudo concectar a la base de datos")

#CUARTA OPERACION DEL CRUD: DELETE O ELIMINAR
    def EliminarObjeto(self, Matricula):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from PSICOLOGO  where MATRICULA= 689687"
                cursor.execute(sentenciaSQL)

                self.conexion.commit()                
                self.conexion.close()
            except:
                print("No se pudo concectar a la base de datos")
