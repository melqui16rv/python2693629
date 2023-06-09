class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    
    def set_id(self, id):
        self.id = id
    def getid(self):
        return self.id
    
    def inforusuario(self):
        return print(f"su usuario es {self.nombre}, y su id es {self.id}")

    def usuarios_id(self):
        print("los usurios con sus id son: ")
        self.listaUsuarios={'Juan': 7777,
                            'Pedro':2222,
                            'Maria':3333,
                            'Jose':4444,
                            'David':5555,
                            'Salome':6666}
        return print(self.listaUsuarios,"\t")
    # def lsls(self):
    #     self.titulo={titulo:autor}
    #     self.autor=
    #     isbn
    #     publicación
    #     estado

    #     def setISBN( self, isbn, titulo):
    #         values=list(titulo.keys())
    #         print(values)
    def registro(self):
        self.nuevoUsuario=input("ingrese usuario")
        self.nuevoId= input("Ingrese id: ")
        self.listaUsuarios[self.nuevoId] = self.nuevoUsuario
        print(f"se agrego el usuario {self.nuevoUsuario} con su id {self.nuevoId} ")


class Persona(Usuario):
    def __init__(self, nombre, id, departmento):
        super().__init__(nombre, id)
        self.departmento = departmento


class Estudiante(Usuario):
    def __init__(self, nombre, id, clase):
        super().__init__(nombre,id)
        self.clase = clase