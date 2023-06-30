class Cargo:
    def __init__ (self,Id_cargo,Nombre,Codigo_cno,Ubicacion,Num_empresa):
        self.__Id_cargo = Id_cargo
        self.__Nombre = Nombre
        self.__Codigo_cno = Codigo_cno
        self.__Ubicacion = Ubicacion
        self.__Num_empresa = Num_empresa
      
    def setId_cargo(self,Id_cargo):
        self.__Id_cargo = tId_cargo
    def getId_cargo(self):
        return self.__Id_cargo

    def setNombre(self,Nombre):
        self.__Nombre = Nombre
    def getNombre(self):
        return self.__Nombre

    def setCodigo_cno(self,Codigo_cno):
        self.__Codigo_cno = Codigo_cno
    def getLugar(self):
        return self.__Codigo_cno

    def setUbicacion(self,Ubicacion):
        self.__Ubicacion = Ubicacion
    def getUbicacion(self):
        return self.__Ubicacion

    def setNum_empresa(self,Num_empresa): 
        self.__Num_empresa = Num_empresa
    def getNum_empresa(self):
        return self.__Num_empresa

    

