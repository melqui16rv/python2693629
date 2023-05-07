#[] {} ()
x=100 # asignamos a la variable (x) el numero 100

""" con la funcion type nos ayuda a saver el tipo de dato que 
esta almacenado una variable en este caso (x) de tipo enteero """
print('tipo de x',type(x))

lista=[1,1.4,'sena',['a','b',],'soacha'] #generamos una lista y le agregamos datos
print(f'elemento {lista[4]}') #impriminos el dato 4, recordando que el ultimo numero es numero de elementos menos uno(porque la lista se cuenta desde 0)
print(len(lista)) #con la funcion lend sabemos cuantos datos hay en la lista

""" con la funcion type nos ayuda a saver el tipo de dato que 
esta almacenado una variable en este caso (lista) es de tipo list """
print('tipo de lista',type(lista))
print('ultimo indice',lista[-1]) #imprimimos el ultimo dato almacenado, el menos 1 es porque la lista inicia en 0(ultimo numero es numero de elementos menos uno)

print(len(lista))
lista.append(20) #con el metodo append agregamos un elemento al final de la lista
lista.append('python') 
print(lista)
lista.insert(len(lista),'java') #con el metodo inert podemos agregar un elemento en una posicion especifica
print(lista) #finalizamos imprimiendo la lista