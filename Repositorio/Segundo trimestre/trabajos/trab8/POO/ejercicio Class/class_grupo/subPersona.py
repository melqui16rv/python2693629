from Libros import Usuario


class Persona(Usuario):
    def __init__(self, nombre, id, departmento):
        super().__init__(nombre, id)
        self.departmento = departmento

    def set_departamento(self, departamento):
        self.departamento = departamento
    def get_departamento(self):
        return self.departamento

