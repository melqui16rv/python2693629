from Persona import *
from Buscador import *



def mostrar_menu():
        print("MENÚ\n")
        print("1. iniciar sesion")
        print("2. Ver ficha")
        print("3. Postularse")
        print("4. Buscar oferta")
        print("5. Filtrar ciudad")
        print("6. Filtrar departamento")
        print("7. Mostrar cargo")
        print("8. Mostrar vacantes")
        print("9. salir")

continuar = True
while continuar:
    print("")
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ")
    print("")

    if opcion == "1":
        usu1=Persona(nombre=str(input("digite su nombre: ")), usuario=str(input("ingrese usuario: ")), contrasena=str(input("ingrese la contraseña: ")))
         
    elif opcion == "2":
        print(Persona.getver())
                  
    elif opcion == "3":
        print(Persona.getcredenciales())
        
    elif opcion=="4":
        print(Buscador.buscar_oferta())
         
    elif opcion == "5":
        print(Buscador.filtrar_ciudad())
    elif opcion == "6":
        print("")
    elif opcion == "7":
        print(Buscador.mostrar_cargo)
    elif opcion == "8":
        print(Buscador.mostrar_vacante) 
    elif opcion == "9":  
        print ("Asta luego")   
    else:
         print("Opción inválida. Por favor, ingrese un número válido.")