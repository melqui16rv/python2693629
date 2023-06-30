class Idioma:
    def __init__(self,entidad,tipo,tiempo):
        self.entidad = entidad
        self.tipo = tipo
        self.tiempo = tiempo
    
    def setEntidad(self,entidad):
        self.entidad=entidad
    def getEntidad(self):
        return self.entidad

    def setTipo(self,tipo):
        self.tipo=tipo
    def getTipo(self):
        return self.tipo

    def setTipo(self,tiempo):
        self.tiempo=tiempo
    def getTipo(self):
        return self.tiempo