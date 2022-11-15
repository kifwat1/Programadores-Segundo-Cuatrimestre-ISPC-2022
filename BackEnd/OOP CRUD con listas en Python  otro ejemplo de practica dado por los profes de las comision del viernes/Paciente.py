
class Paciente:
    def __init__(self,dni, nombre, apellido, email, telefono, nacimiento):
        self.__dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.nacimiento = nacimiento
        
    #-----------------------------------------
    def get_dni(self):   ##Getter
        return self.__dni
      
    
    def set_dni(self, new_dni): ##Setter
        self.__dni = new_dni
    #------------------------------------------

    def describe(self): # This one is used to describe the patient
        print(f" El Nombre del paciente es:{self.nombre}. El apellido:{self.apellido}. DNI: {self.__dni}. El email: {self.email}")
        


print(Paciente)

#paciente_1=Paciente(12121212,"Alonso", "Alfred", "alonso@gmail.com", 11613265, 1999/9/30)
#paciente_1.describe()
#print(paciente_1.get_dni())
#paciente_1.set_dni(1989563) ##### Updating the DNI
#print(paciente_1.get_dni())
#print("DNI ACTUALIZADO", paciente_1.describe())

 
