
def mostrar_menu():
    print("Bienvenido al programa")
    print("1. Ingresar")
    print("2. Registrarse")
    print("3. Cuenta")
    print("4. libros")

listaUsuarios={'Juan': 7777,
                    'Pedro':2222,
                    'Maria':3333,
                    'Jose':4444,
                    'David':5555,
                    'Salome':6666}

class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def registro(self):
        self.nuevoUsuario=input("inbrese usuario")
        self.nuevoId= input("Ingrese id: ")
        self.listaUsuarios[self.nuevoId] = self.nuevoUsuario


class Persona(Usuario):
    def __init__(self, nombre, id, departmento):
        super().__init__(nombre, id)
        self.departmento = departmento


class Estudiante(Usuario):
    def __init__(self, nombre, id, clase):
        super().__init__(nombre,id)
        self.clase = clase






