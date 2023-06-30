class Empresa:

    def __init__(self,nombre,Id_Empresa,rut):
            self.nombre = nombre
            self.Id_Empresa = Id_Empresa
            self.rut = rut
        

    def setNombre (self, nombre):
        self.__nombre=nombre
    def get_Nombre(self):
        return self.__nombre

    def setId_persona (self,Id_Empresa):
        self.__Id_Empresa = Id_Empresa
    def getId_persona(self):
        return self.__Id_Empresa

    def setrut(self,rut):
        self.__rut= rut
    def getrut (self):
        return self.__rut

    def Publicar_cargo (self):
        Publicar_cargo = input("ingrese el cargo que quiere publicar")

    def seleccionar_individuo (self):
        seleccionar_individuo = input ("seleccione el individuo")

    def cerrar_cargo (self):
        cerrar_cargo = input ("Se cierra el cargo")
    

        