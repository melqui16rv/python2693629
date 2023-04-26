# Solicitar al usuario que ingrese dos números con la función input y guardamos los números en las variables(X y Y)
x=input('ingrese numero')
y=input('ingrese numero')

# Comprobar si los números son iguales(==), descendentes(>) o ascendente(o por descarte ponemos la función else)
if x==y:                  #con la función if preguntamos si X y Y son iguales (resultado booleano)
    print('son iguales')  #si es verdadero, imprime(son iguales)
elif x>y:                 #si falso, con la función elif preguntamos si X es mayor que Y (resultado booleano)
    print('descendente')  #si es verdadero, imprime(descendente)
else:                     #si es falso, con la función else se escoge por descarte que es ascendente
    print('ascendente')   #imprime(ascendente)
