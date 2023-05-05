import random
list=[]
suma=0

tam=int(random.randint(1,5))
print(tam)

mayor=0
menor=100
for i in range(tam):
    num=int(random.randrange(100))
    list.append(num)
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
print(list)
print(f"El numero {mayor} es el mayor de la lista")
print(f"El numero {menor} es el menor de la lista")

for g in list:
    suma=suma+g
print('la suma es', suma)