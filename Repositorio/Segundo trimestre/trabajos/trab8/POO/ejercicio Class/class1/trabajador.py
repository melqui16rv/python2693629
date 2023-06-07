"""Escriba una clase Empleado que tenga como propiedades
nombre, cargo, salario
escriba metodos contructores, setters y getters
escriba un método que permita calcular cuanto gana el empleado en una hora
un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3%
Un método que reciba una cantidad de horas extras y calcule el salario incrementando las extras. No puede hacer mas de dos 
horas diarias y trabaja de luenes a viernes. Valide

Anexar variable de clase que cuente cantidad de objetos creados de esa clase"""

class trabajador:
    def __init__(self, nombre, cargo, salario, horas):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.horas = horas
   
        #SET nombre y cargo
    def setNombre(self,nombre):
        self.nombre=nombre
    def setCargo(self,cargo):
        self.cargo=cargo
        
        #GET nombre y cargo
    def getNombre(self):
        return self.nombre        
    def getCargo(self):
        return self.cargo
    
    

    # def setHorasExr(self, horasExtras):
    #     horasExtras=horasExtras
        
    #     #SET horas extras
    # def setHorasEx(self,nombre):
    #     self.nombre=nombre
    #     #GET horas extras
    # def getHorasEx(self):
    #     return self.nombre        

