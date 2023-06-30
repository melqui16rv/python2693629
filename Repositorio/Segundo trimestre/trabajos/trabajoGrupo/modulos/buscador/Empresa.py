class Empresa:
    def __init__ (self,nombre,ID,RUT):
        self.__nombre=nombre
        self.__ID=ID
        self.__RUT=RUT
        self.__Ficha=[]
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getNombre(self):
        return self.__nombre
    def setID(self,ID):
        self.__ID=ID
    def getNombre(self):
        return self.__ID
    def setNombre(self,RUT):
        self.__RUT=RUT
    def getNombre(self):
        return self.__RUT


    def CrearFicha(self):
        nombreFicha=input("ingrese el nombre de la ficha que quiere guardar")
        numeroFicha=input("ingrese el codigo de la ficha")
        objficha=Empresa(nombreFicha,numeroFicha)
        self.__Ficha.append(objficha)
        


    