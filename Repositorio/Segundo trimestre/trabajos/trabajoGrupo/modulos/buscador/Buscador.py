class Buscador  :
    def __init__(self,buscar):
        self.buscar = buscar 
    def setBuscar(self,buscar):
        self.buscar = buscar
    def getBuscar(self):
        return self.buscar

    def buscar_oferta(self):
        o=str(input("introduzca la oferta que quiere buscar:"))
        return o
    def mostrar_sugerencias():
        pass

    def filtrar_ciudad():
        lis=["soacha","cundinamarca","boyaca"]
        ciu=str(input("digite la ciudad donde quiere trabajar"))
        if ciu == lis:
            print("la ciudad se encuentra disponible continue con su busqueda")
        else:
            print("esa ciudad no se encuntra en la base de datos")

    def filtrar_departamento():
        pass
    def mostrar_cargo():
        print("hay x numero de cargos")
    def mostrar_vacante():
        print("hay x numero de vacantes")