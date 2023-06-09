from app import Cuenta


persona1=Cuenta(librosPrestados=int(input("libros Prestados: ")), librosReservados=int(input("libros Reservados: ")), librosDevueltos=int(input("libros Devueltos: ")), librosPerdidos=int(input("libros Perdidos: ")))
# print(persona1.calcularMulta())

# person2=Estudiante("melqui",3535,"ADSO")
# print(person2.nombre,person2.id, person2.clase)