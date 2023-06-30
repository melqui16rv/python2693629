class Persona:
    def __init__(self,persona,credenciales,infoLaboral,infoPersonal,hojaVida,ver_ficha):
        self.persona = persona
        self.credenciales = credenciales
        self.infoLaboral =infoLaboral
        self.infoPersonal = infoPersonal
        self.hojaVida = hojaVida
        self.__ver_ficha=ver_ficha
    
    def setVer(self,ver_ficha):
        self.__ver_ficha = ver_ficha
    def getver(self):
        return self.__ver_ficha

    def setnombre(self,nombre):
        self.nombre = nombre
    def getnombre(self):
        return self.nombre

    def setcredenciales(self,credenciales):
        self.credenciales = credenciales
    def getcredenciales(self):
        return self.credenciales 

    def setinfoLaboral(self, infoLaboral):
        self.infoLaboral=infoLaboral
    def getinfoLaboral(self,):
        return self.infoLaboral

    def setinfoPersonal(self, infoPersonal):
        self.infoPersonal=infoPersonal
    def getinfoPersonal(self,):
        return self.infoLaboral

    def sethojaVida(self,hojaVida):
        self.hojaVida=hojaVida
    def gethojaVida(self,):
        return self.hojaVida

    def ver_ficha(self):
        print("345121385 ",end="|"), print("asistencia en desarrollo de software")
        print("salario", end="|"), print("1.000.000--1.500.000")
        print("experiencia minima",end="|"), print("6 meses")
        print("tipo de contrato",end="|"), print ("indefinido")
        print("publicado",end="|"), print("00/00/1111")
        print("vacantes")
        print("cargo")
        return self.__ver_ficha
        
    def postularse(self):
        pos=str(input("introdusca sus credenciales para poderse postular"))
        self.credenciales=pos
        return self.credenciales
    def ver_Ponderacion():
        pass
