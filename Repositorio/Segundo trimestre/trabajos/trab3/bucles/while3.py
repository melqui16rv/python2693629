num=1
cont=0
sum=0
while num!=0:
    sum+=num
    num=int(input('ingrese numero'))
    cont=cont+1 #cont+=1

print(f'El usuario ingreso {cont-1} numeros') #print('El usuario ingreso', cont, 'numeros')
print('la suma de los numeros es: ',sum-1)
print('el promedio de la suma es: ',sum/cont)
