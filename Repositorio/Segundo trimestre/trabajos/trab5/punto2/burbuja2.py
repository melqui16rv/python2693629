import random # Importar el módulo random para generar números aleatorios

tam=random.randint(5,10) # Generar un tamaño aleatorio entre 5 y 10 para la lista
lista=[random.randrange(100) for i in range(tam)] # Crear una lista con números aleatorios entre 0 y 99 usando comprensión de listas
print(lista) # Imprimir la lista original

# Ordenar la lista de mayor a menor usando un solo recorrido
for i in range(len(lista)-1): # Si el elemento en la posición i es menor que el siguiente, intercambiarlos
    if lista[i]<lista[i+1]:
        lista[i],lista[i+1]=lista[i+1],lista[i]

print(lista) # Imprimir la lista ordenada de mayor a menor

#in - not in    

# for i in range(len(lista)):
#     print(lista[i])

for x in lista: # Recorrer la lista directamente y mostrar cada elemento
    print(x)

if 10 not in lista: # Verificar si el número 10 está o no en la lista y mostrar un mensaje
    print('no esta')
else:
    print('si esta')