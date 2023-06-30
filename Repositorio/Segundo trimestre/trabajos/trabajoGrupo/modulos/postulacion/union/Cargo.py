import random
class Cargo:
    def __init__ (self,nombre,codigoCNO,Ubicacion,Num_empresa):
        self.idCargo= random.randint(10000, 99999)
        self.nombre = nombre
        self.codigoCNO = codigoCNO
        self.Ubicacion = Ubicacion
        self.Num_empresa = Num_empresa
      
    def setidCargo(self,idCargo):
        self.idCargo = tidCargo
    def getidCargo(self):
        return self.idCargo

    def setNombre(self,nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre

    def setcodigoCNO(self,codigoCNO):
        self.codigoCNO = codigoCNO
    def getLugar(self):
        return self.codigoCNO

    def setUbicacion(self,Ubicacion):
        self.Ubicacion = Ubicacion
    def getUbicacion(self):
        return self.Ubicacion

    def setNum_empresa(self,Num_empresa): 
        self.Num_empresa = Num_empresa
    def getNum_empresa(self):
        return self.Num_empresa
    
    def cargos(self):

        return print("Cargo:",self.nombre,"\nid de la empresa:",self.idCargo,"\ncodigo de la CNO:",self.codigoCNO,"\nUbicacion",self.Ubicacion,"\nTelefono de la empresa:",self.Num_empresa)
cargo1=Cargo("Desarrollador de aplicaciones informáticas y digitales",2173,"Cra. 15 #88 64", 322825383)
cargo2=Cargo("Profesional de talento humano",1121,"Cra. 40 #34 65", 322987383)
cargo3=Cargo("Ingeniero electricistas",2133,"Cra. 30 #34 56", 322875383)

