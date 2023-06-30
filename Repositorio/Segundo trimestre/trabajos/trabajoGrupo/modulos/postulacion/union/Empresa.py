import random
class Empresa:

    def __init__(self,nombre,rut):
            self.nombre = nombre
            self.id_empresa= random.randint(10000, 99999)
            self.rut = rut

    def setNombre (self, nombre):
        self.__nombre=nombre
    def get_Nombre(self):
        return self.__nombre

    def setId_persona (self,Id_Empresa):
        self.__Id_Empresa = Id_Empresa
    def getId_persona(self):
        return self.__Id_Empresa

    def setRut(self,rut):
        self.__rut= rut
    def getRut (self):
        return self.__rut
    
    def infoEmpresa(self):
        return print("Nombre:",self.nombre, "\nrut:",self.rut," \nid_empresa:", self.id_empresa)
    def Publicar_cargo (self):
        Publicar_cargo = input("ingrese el cargo que quiere publicar")

    def seleccionar_individuo (self):
        seleccionar_individuo = input ("seleccione el individuo")

    def cerrar_cargo (self):
        cerrar_cargo = input ("Se cierra el cargo")

empresa1=Empresa("NETDATA", 81675600)
print(empresa1.infoEmpresa())