class Educacion:
    def __init__(self,entidadEducacion,tipoEducacion,tiempoEducacion):
        self.entidadEducacion=entidadEducacion
        self.tipoeducacion=tipoEducacion
        self.tiempoeducacion=tiempoEducacion

    def setEntidadEducacion(self,entidadEducacion):
        self.entidadEducacion=entidadEducacion
    def getEntidadEducacion(self):
        return self.entidadEducacion
    
    def settipoEducacion(self,tipoEducacion):
        self.tipoEducacion=tipoEducacion
    def getTipoEducacion(self):
        return self.tipoEducacion

    def setTipo(self,tipo):
        self.tipo=tipo
    def getTipo(self):
        return self.tipo