from trabajador import*

persona1=trabajador(nombre=str(input("Nombre: ")), cargo=str(input("Cargo: ")), salario=float(input("salario: ")), horas=int(input("Horas extras: ")))
#persona2=trabajador("jose", "gerente", "1400000")
persona1.setNombre("Alexander")


print("Nuevo nombre utilizando SET: ", persona1.getNombre())
print("\n")

print("Datos")
print("Nombre:", persona1.nombre, "\nCargo:", persona1.cargo, "\nSalario:", persona1.salario, "\nhoras extras: ", persona1.horas)
#print(persona2.nombre, persona2.cargo, persona2.salario)
print("\n")

print(persona1.__dict__)
print("Nombre utilizando GET:",persona1.getNombre())
print("Cargo utilizando GET:",persona1.getCargo())
print("\n")


x=persona1.salario 
x= x/160
print("el valor de la hora :",x)

hora3= persona1.horas
hora3= hora3*x
print('el valor de las horas extra trabajadas es:',hora3)

y=persona1.salario
y=y+hora3
print('la suma del sueldo mas las horas extras es:',y)


# horas3=persona1.salario/160

# print(calcHora)pep
