class Cargo:
    def __init__ (self,couc,tiempo,contrato,lugar,vacantes,postulante,fecha,cierre):
        self.__couc=couc
        self.__tiempo=tiempo
        self.__contrato=contrato
        self.__lugar=lugar
        self.__vacantes=vacantes
        self.__postulante=postulante
        self.__fecha=fecha
        self.__cierre=cierre
        couc=[]
    def setTiempo(self,tiempo):
        self.__tiempo=tiempo
    def getTiempo(self):
        return self.__tiempo
    def setContrato(self,contrato):
        self.__contrato=contrato
    def getContrato(self):
        return self.__contrato
    def setLugar(self,lugar):
        self.__lugar=lugar
    def getLugar(self):
        return self.__lugar
    def setVacante(self,vacantes):
        self.__vacantes=vacantes
    def getVacante(self):
        return self.__vacantes
    def setPostulante(self,postulante): 
        self.__postulante=postulante
    def getPostulante(self):
        return self.__postulante
    def setFecha(self,fecha):
        self.__fecha=fecha
    def getFecha(self):
        return self.__fecha
    def setCierre(self,cierre):
        self.__cierre=cierre
    def getCierre(self):
        return self.__cierre
    


