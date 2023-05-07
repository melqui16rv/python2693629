"""Llenar dos arreglos de n elementos con números generados con la función random. Compararlos y decir:
a.	Cuál de los dos tiene la suma más alta
b.	Cuál de los dos tiene el número mayor
c.	Cuál de los dos tiene el número menor
d.	Cuál es el promedio conjunto (uniendo los dos arreglos)
e.	Sacar el promedio de cada uno y decir si está por encima o por debajo del arreglo conjunto
f.	Cuál de los dos tiene mayor cantidad de pares
g.	Cuál de los dos tiene mayor cantidad de impares"""
import random


list=[]
suma1=0
suma2=0
par1=0
par2=0
impar1=0
impar2=0

tam=int(random.randint(10, 15))
print(tam)
mayor1=0
menor1=100
for i in range(tam):
    num=int(random.randrange(100))
    list.append(num)
    if num>mayor1:
        mayor1=num
    if num<menor1:
        menor1=num
print("La lista uno es: ", list)
print(f"El número {mayor1} es el mayor de la lista.")
print(f"El número {menor1} es el menor de la lista.")

for g in list:
    suma1 = suma1 + g
    if g % 2 == 0:
        par1 += 1
    else:
        impar1+=1
print("La suma es:", suma1)
print(f"Hay {par1} pares")
print(f"hay {impar1} numeros impares" )


list1=[]

tam=int(random.randint(10, 15))
print(tam)
mayor2=0
menor2=100
for i in range(tam):
    num=int(random.randrange(100))
    list1.append(num)
    if num>mayor2:
        mayor2=num
    if num<menor2:
        menor2=num
print("La lista dos es: ", list1)
print(f"El número {mayor2} es el mayor de la lista.")
print(f"El número {menor2} es el menor de la lista.")

for g in list1:
    suma2 = suma2 + g
    if g % 2 == 0:
        par2 += 1
    else:
        impar2+=1
print("La suma es:", suma2)
print(f"Hay {par2} numeros pares")
print(f"Hay {impar2} numeros impares")



print('RESULTADOS')

if mayor1<mayor2:
    print(f"el numero mayor es {mayor2} que le pertenece a la lista Dos")
else:
    print(f"el numero mayor es {mayor1} que le pertenece a la lista Uno")


if menor1>menor2:
    print(f"el numero menor es {menor2} que le pertenece a la lista Dos")
else:
    print(f"el numero menor es {menor1} que le pertenece a la lista Uno")


if par1<par2:
    print(f"la lista dos tine mas pares que la lista uno, nuemero de pares: {par2}")
else:
    print(f"la lista uno tine mas pares que la lista dos, nuemero de pares: {par1}")


if impar1<impar2:
    print(f"la lista dos tine mas impares que la lista uno, nuemero de impares: {impar2}")
else:
    print(f"la lista uno tine mas impares que la lista dos, nuemero de impares: {impar1}")