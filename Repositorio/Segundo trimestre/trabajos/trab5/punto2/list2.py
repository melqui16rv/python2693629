import random # Importar el módulo random para generar números aleatorios

lista=[] #creamos una variable y le asignamos una lista vacia
tam=int(random.randint(10,20)) #le asignamos el tamaño de modo que sea aleatorio de un rango de 10 a 20, todo esto con la función random y randint
print(tam)

for i in range(tam):
    num=int(random.randrange(100)) #con la funcion randreage generamos un numero aleatorio dentro de un rango especificado
    lista.append(num) #con el metodo append agregamos un elemnto al final de lalista
print(lista) #imprimimos la lista