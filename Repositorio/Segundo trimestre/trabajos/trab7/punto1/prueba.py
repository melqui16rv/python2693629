"""Llenar dos arreglos de n elementos con números generados con la función random. Compararlos y decir:
a.	Cuál de los dos tiene la suma más alta
b.	Cuál de los dos tiene el número mayor
c.	Cuál de los dos tiene el número menor
d.	Cuál es el promedio conjunto (uniendo los dos arreglos)
e.	Sacar el promedio de cada uno y decir si está por encima o por debajo del arreglo conjunto
f.	Cuál de los dos tiene mayor cantidad de pares
g.	Cuál de los dos tiene mayor cantidad de impares"""
import random


def llenarLista1(tam,rango):
    lista1=[random.randrange(rango) for i in range(tam)]
    return lista1

def llenarLista2(tam,rango):
    lista2=[random.randrange(rango) for i in range(tam)]
    return lista2


def sumarListas(lista1, lista2):
    suma1 = 0
    suma2 = 0
    for i in range(len(lista1)):
        suma1 += lista1[i]
    for j in range(len(lista2)):
        suma2 += lista2[j]
    print("la suma de la lista uno es:", suma1)
    print("la suma de la lista dos es:", suma2)
    if suma1 > suma2:
        return "La lista 1 tiene la suma más alta"
    elif suma2 > suma1:
        return "La lista 2 tiene la suma más alta"
    else:
        return "Ambas listas tienen la misma suma"


def numMayorMenor(lista1, lista2):
    maximo1 = lista1[0]
    minimo1 = lista1[0]
    maximo2 = lista2[0]
    minimo2 = lista2[0]
    for i in range(1, len(lista1)):
        if lista1[i] > maximo1:
            maximo1 = lista1[i]
        if lista1[i] < minimo1:
            minimo1 = lista1[i]
    for j in range(len(lista2)):
        if lista2[j] > maximo2:
            maximo2 = lista2[j]
        if lista2[j] < minimo2:
            minimo2 = lista2[j]
    if maximo1 == maximo2:
        print("Ambas listas tienen el mismo número mayor:", maximo1)
    elif maximo1 > maximo2:
        print("La lista 1 tiene el número mayor:", maximo1)
    else:
        print("La lista 2 tiene el número mayor:", maximo2)
    if minimo1 == minimo2:
        print("Ambas listas tienen el mismo número menor:", minimo1)
    elif minimo1 < minimo2:
        print("La lista 1 tiene el número menor:", minimo1)
    else:
        print("La lista 2 tiene el número menor:", minimo2)

       
def unir_listas(lista1, lista2):
    lista1.extend(lista2)
    return lista1


def sumaLista(lista1):
    sum=0
    for x in lista1:
        sum+=x
    return sum


def promedioLista(lista):
    return sumaLista(lista)/len(lista)


l1=llenarLista1(3,10)
print(l1)

l2=llenarLista2(3,10)
print(l2)

print(sumarListas(l1,l2))

print(numMayorMenor(l1,l2))

print("promedio lista uno")
print(round(promedioLista(l1),2))

print("promedio lista dos")
print(round(promedioLista(l2),2))

lista1=unir_listas(l1,l2)
print("La lista unida es: ",lista1)

print("el promedio conjunto es: ")
print(round(promedioLista(lista1),2))
