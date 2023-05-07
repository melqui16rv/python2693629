"""1.	Llenar un arreglo de n elementos con números generados con la función random. N es ingresado por el usuario. Diseñe un menú con las siguientes operaciones. 
a.	Imprimir arreglo original (El primero que se generó)
b.	Suma
c.	Promedio
d.	Mayor
e.	Menor
f.	Ordenar ascendente (No perder el arreglo original; el del punto a)
g.	Ordenar descendente (No perder el arreglo original; el del punto a)
h.	Moda
i.	Mediana
j.	Buscar. Decir si encuentra el número, en qué posición(es) está, cuantas veces está"""
import random

list=[]
suma=0

tam=int(random.randint(10, 15))
print(tam)
mayor=0
menor=100
for i in range(tam):
    num=int(random.randrange(100))
    list.append(num)
    if num>mayor:
        mayor=num
    if num<menor:
        menor=num
print("La lista original es: ", list)
print(f"El número {mayor} es el mayor de la lista.")
print(f"El número {menor} es el menor de la lista.")

for g in list:
    suma=suma+g
promedio=suma/tam
print("la suma es: ", suma)
print(f"El promedio de la lista es: {promedio}")

for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print(f"La lista ordenada es: {list}")

for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j]<list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print(f"La lista de forma descendnte: {list}")

if tam%2==0:
    mediana=(list[tam//2]+list[tam//2-1])/2
else:
    mediana=list[tam//2]
print(f"La mediana de la lista es {mediana}.")

frecuencias={}
for g in list:
    if g in frecuencias:
        frecuencias[g]+=1
    else:
        frecuencias[g]=1
moda = None
max_frecuencia = 0
for g in frecuencias:
    if frecuencias[g] > max_frecuencia:
        moda = g
        max_frecuencia = frecuencias[g]
print(f"La moda de la lista es {moda}.")

num=int(input("Ingrese un número para buscar en la lista: "))
veces=0
posiciones=[]
for i in range(tam):
    if list[i]==num:
        veces+=1
        posiciones.append(i)
if veces>0:
    print(f"El número {num} aparece {veces} veces en la lista, en las posiciones {posiciones}.")
else:
    print(f"El número {num} no está en la lista.")
