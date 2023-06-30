from Aspirante import *
from Persona import *
from Empresa import *
from Cargo import *
import random



def mostrar_menu():
        print("MENÚ\n")
        print("1. iniciar seccion")
        print("2. cargar datos de hoja de vida")
        print("3. ver perfil de usuario")
        print("4. ver hoja de vida")
        print("5. ver cargos")
        print("6. salir del programa")
        
def menuPostulacion():
    print("postulacion")
    print("1. postularse a cargo 1")
    print("2. postularse a cargo 2")
    print("3. postularse a cargo 3")
    print("4. retroceder")

continuar = True
while continuar:
     print("")
     mostrar_menu()
     opcion = input("Ingrese el número de la opción deseada: ")
     print("")

     if opcion == "1":
         usu1=Persona(nombre=str(input("digite su nombre: ")), usuario=str(input("ingrese usuario: ")), contrasena=str(input("ingrese la contraseña: ")))
    
     elif opcion == "2":
         usu1=Aspirante(correo=str(input("correo: ")), numTelefono=int(input("ingrese numero telefonico: ")), documento=int(input("ingrese su documento: ")), sisben=str(input("ingrese su sisben: ")), direccion=str(input("ingrese su dirección: ")))
         
     elif opcion=="3":
         print(usu1.perfilUsuario())
        
     elif opcion=="4":
        print(usu1.hoja_vida())

        
     elif opcion== "5":
         print(cargo1.cargos())
         print("")
         print(cargo2.cargos())
         print("")
         print(cargo3.cargos())
         
         print("-----")
         continuar2=True
         while continuar2:
            print("")
            menuPostulacion()
            opcion=input("ingrese una opcion para la postulacion: ")
            print("")
            if opcion=="1":
                print(cargo1.cargos(), "Postulado al cargo de", cargo1.getNombre())
                
            elif opcion=="2":
                print(cargo2.cargos(), "Postulado al cargo de", cargo2.getNombre())
            
            elif opcion=="3":
                print(cargo3.cargos(), "Postulado al cargo de", cargo3.getNombre())
            elif opcion=="4":
               print("atras")
               continuar2=False                    
            else:
                print("opcion invalida")
         

     elif opcion == "6":
         print("¡Hasta luego!")
         continuar = False
     else:
         print("Opción inválida. Por favor, ingrese un número válido.")