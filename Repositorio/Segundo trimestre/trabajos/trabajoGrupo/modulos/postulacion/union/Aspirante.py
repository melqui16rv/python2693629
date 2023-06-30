from Persona import * 
class Aspirante:
    def __init__(self, correo, numTelefono, documento, sisben, direccion):
        self.correo=correo
        self.numTelefono=numTelefono
        self.documento=documento
        self.sisben=sisben
        self.direccion=direccion

        self.educacion=[]
        self.idiomas=[]
        self.expeLaborar=[]
    
    def setCorreo(self,correo):
        self.correo=correo
    def getCorreo(self):
        return self.correo
        
    def setNumTelefono(self,numTelefono):
        self.numTelefono=numTelefono
    def getNumTelefono(self):
        return self.numTelefono
    
    def setDocumento(self,documento):
        self.documento=documento
    def getDocumento(self):
        return self.documento
    
    def setSisben(self,sisben):
        self.sisben=sisben
    def getSisben(self):
        return self.sisben

    def setDireccion(self,direccion):
        self.direccion=direccion
    def getDireccion(self):
        return self.direccion
    
    
    def setEducacion(self,educacion):
        self.educacion=educacion
    def getEducacion(self):
        return self.educacion

    def setIdiomas(self,idiomas):
        self.idiomas=idiomas
    def getIdiomas(self):
        return self.idiomas

    def setExpeLaboral(self,expeLaboral):
        self.expeLaboral=expeLaboral
    def getExpeLaboral(self):
        return self.expeLaboral
    
    def hoja_vida(self):
        print("Correo: ",self.correo,"\nTelefono:",self.numTelefono, "\nDocumento: ",self.documento, "\nSisben:",self.sisben, "\nDirección:",self.direccion)