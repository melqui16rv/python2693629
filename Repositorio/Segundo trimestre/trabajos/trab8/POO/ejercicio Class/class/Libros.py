from Libros import *

class Libros:
    def __init__(self, tiulo, autor, numEstandar, publicacion):
    # super(Cuenta).__init__(librosPrestados,librosReservados, librosReservados, librosPrestados):
        self.tiulo = tiulo
        self.autor = autor
        self.numEstandar = numEstandar
        self.publicacion = publicacion