class Experiencia:
    def __init__(self, nombreEmpresa,tipoEmpresa,funciones,tiempoCargo):
        self.nombreEmpresa = nombreEmpresa
        self.tipoEmpresa = tipoEmpresa
        self.funciones = funciones
        self.tiempoCargo = tiempoCargo
    
    def setnombreEmpresa(self,nombreEmpresa):
        self.nombreEmpresa=nombreEmpresa
    def getnombreEmpresa(self):
        return self.nombreEmpresa
    
    def settipoEmpresa(self,tipoEmpresa):
        self.tipoEmpresa=tipoEmpresa
    def gettipoEmpresa(self):
        return self.tipoEmpresa
    
    def setfunciones(self,funciones):
        self.funciones=funciones
    def getfunciones(self):
        return self.funciones
    
    def settiempoCargo(self,tiempoCargo):
        self.tiempoCargo=tiempoCargo
    def gettiempoCargo(self):
        return self.tiempoCargo