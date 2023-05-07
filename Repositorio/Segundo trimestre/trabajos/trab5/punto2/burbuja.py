import random # Importar el módulo random para generar números aleatorios

lista=[] # Crear una lista vacía

tam=int(random.randint(5,10)) # Generar un tamaño aleatorio entre 5 y 10 para la lista

for i in range(tam): # Llenar la lista con números aleatorios entre 0 y 99
    num=int(random.randrange(100))
    lista.append(num)
    
print(lista) # Imprimir la lista original

for i in range(tam): # Ordenar la lista de menor a mayor usando el algoritmo de burbuja
    for j in range(i+1,tam): # Si el elemento en la posición i es mayor que el de la posición j, intercambiarlos
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux

print(lista) # Imprimir la lista ordenada de menor a mayor

for i in range(tam): # Ordenar la lista de mayor a menor usando el algoritmo de burbuja
    for j in range(i+1,tam): # Si el elemento en la posición i es menor que el de la posición j, intercambiarlos
        if lista[i]<lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux            
print(lista) # Imprimir la lista ordenada de mayor a menor

#x,y=10,20 # Asignar los valores 10 y 20 a las variables x e y respectivamente