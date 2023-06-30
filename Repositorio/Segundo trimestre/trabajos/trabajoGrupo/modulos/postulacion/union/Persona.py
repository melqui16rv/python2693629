class Persona:
    def __init__(self, nombre, usuario, contrasena):
        self.nombre=nombre
        self.usuario=usuario
        self.contrasena=contrasena
        self.id_Persona=[]

    def setNombre(self,nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre

    def setUsuario(self,usuario):
        self.usuario=usuario
    def getUsuario(self):
        return self.usuario

    def setContrasena(self,contrasena):
        self.contrasena=contrasena
    def getContrasena(self):
        return self.contrasena
    
    def perfilUsuario(self):
        return print("Nombre:",self.nombre,"\nUsuario:",self.usuario,"\nContraseña:",self.contrasena)
        

