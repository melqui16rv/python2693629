from Cuenta import*
from superClas import *
from Libros import *

usu1=Usuario(nombre=str(input("digite un usuario: ")), id=int(input("ingrese un id: ")))
print("")
#print(usu1.usuarios_id())
#print(usu1.registro())
print(usu1.inforusuario())

usu1=Cuenta(librosPrestados=int(input("libros Prestados: ")), librosReservados=int(input("libros Reservados: ")), librosDevueltos=int(input("libros Devueltos: ")), librosPerdidos=int(input("libros Perdidos: ")))
print(usu1.calcularMulta())
print(" ")
print("Libreria disponible")
libro=Libros("La maldicion de hill house", "Shirley Jackson", 75757, "Año de publicacion 1959")
print(libro.menulibros())
# person2=Estudiante("melqui",3535,"ADSO")
# print(person2.nombre,person2.id, person2.clase)
