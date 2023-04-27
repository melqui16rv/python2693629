num=1    #creamos la variable que va a almacenar el número ingresado por el usuario
cont=0   #creamos la variable que ira contando los números ingresados por el usuario
sum=0    #creamos la variable de la suma de los números ingresados
mayor=0  #creamos la variable para almacenar el número mayor ingresado hasta el momento
menor=1000000  #creamos la variable para almacenar el número menor ingresado hasta el momento
while num!=0: #el ciclo(while) se ejecutará hasta que el usuario ingrese un 0
    num=int(input('ingrese numero'))  #le solicitamos al usuario que ingrese un número
    cont=cont+1  # Incrementamos el contador de números ingresados
    sum=sum+num  #vamos acumulamos la suma de los números ingresados
    if num>mayor: #con la función(if) ponemos la condición de que si(num>mayor) entonces(mayor=num)
        mayor=num  #si el número ingresado es mayor al almacenado en la variable mayor, lo actualizamos
    if num<menor and num!=0:
        menor=num  #si el número ingresado es menor al almacenado en la variable menor y no es 0, lo guardamos

#mostramos los resultados
print(f'El usuario ingreso {cont-1} numeros')  #Restamos 1 al contador porque no queremos contar el número 0
print(f'La suma es {sum}')
print(f'El promedio es {sum/(cont-1)} numeros')  #Calculamos el promedio de los números ingresados
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')
#print('El usuario ingreso', cont, 'numeros')
