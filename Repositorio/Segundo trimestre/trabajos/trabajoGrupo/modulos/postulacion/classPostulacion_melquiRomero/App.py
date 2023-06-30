from Persona import *
from Aspirante import *

def mostrar_menu():
        print("MENÚ\n")
        print("1. iniciar seccion")
        print("2. cargar datos de hoja de vida")
        print("3. ver cargos")
        print("4. postularse")
        print("5. ver perfil de usuario")
        print("6. ver hoja de vida")
        print("7. salir del programa")

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
                  
     elif opcion == "5":
         print(usu1.perfilUsuario())
        
     elif opcion=="6":
        print(usu1.hoja_vida())
         
     elif opcion == "7":
         print("¡Hasta luego!")
         continuar = False
     else:
         print("Opción inválida. Por favor, ingrese un número válido.")