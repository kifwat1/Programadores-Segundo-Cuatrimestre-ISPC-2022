


import os
import Paciente

lista_pacientes= []    

def mostrar_opciones():
    print('CRUD EJEMPLO')
    print('*' * 50)
    print('Selecciona una opción:')
    print('[C]reate')
    print('[R]ead - Leer')
    print('[U]pdate - Actualizar')
    print('[D]elete  - Elimnar')
    print('[S]ALIR')

    

def run():
    mostrar_opciones()
    
    command = input()
    command = command.upper()
    

    while True:
        if command == 'C':
            print('CREACIÓN DE CLIENTE')
            print('*' * 50)
            print('Inserta el DNI:')
            dni = input()
            print('Inserta el nombre:')
            nombre = input()
            print('Inserta los apellidos:')
            apellido = input()
            print('Inserta el email:')
            email = input()
            print('Inserta el teléfono (9 cifras sin guiones ni puntos):')
            telefono = input()
            print('Inserta la fecha de nacimiento (YYYY-MM-DD):')
            nacimiento = input()
            lista_pacientes.append(Paciente.Paciente(dni, nombre, apellido, email, telefono, nacimiento))      
            print(Paciente)
            command = ""
        elif command == 'R':
            print('PRINT DE TODOS LOS CLIENTES')
            print('*' * 50)
            for i in lista_pacientes:
                print (i.dni,i.nombre,i.apellido, i.email, i.telefono, i.nacimiento)
            command = ""
        elif command == 'U':
            print('Inserta el DNI:')
            dniBusqueda = input()

                
        elif command == 'D':
            print('Inserta el DNI:')
            dniBusqueda = input()

                
        elif command == 'S':
                os._exit(1)
        else:
                run()
        

  

  

        

if __name__ == "__main__":
    run()
    
