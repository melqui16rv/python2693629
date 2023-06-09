from Libros import Usuario


class Estudiante(Usuario):
    def __init__(self, nombre, id, clase):
        super().__init__(nombre,id)
        self.clase = clase
    
    def set_clase(self, clase):
        self.clase = clase
    def getclase(self):
        return self.clase