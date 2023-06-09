from Cuenta import *

class Cuenta:
    def __init__(self, librosPrestados, librosReservados, librosDevueltos, librosPerdidos):
        self.librosPrestados = librosPrestados
        self.librosReservados = librosReservados
        self.librosDevueltos = librosDevueltos
        self.librosPerdidos = librosPerdidos
        self.sumar =[]
        self.precios=str("libros Prestados a :0 \n libros Reservados a :5000 \n libros Devueltos a :0 \n libros Perdidos a :5000")

    def calcularMulta(self):
        self.sumar = [self.librosPrestados*0+self.librosReservados*5000+self.librosDevueltos*0+self.librosPerdidos*10000]
        return print(self.precios), print("\n"), print("""Su multa se calculo de la siguiente manera:\n
Se suma libros prestados con libros Reservados.
Luego se resta el resultado con los libros que fueron devuelto
Al final se suma a la multa depende de cuantos libros perdio
""","su multa es de $",self.sumar,"pesos")
