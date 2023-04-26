i=1    #creamos una variable llamada (i) y le asignamos(1)
sum=0  #creamos una variable llamada(sum) y le asignamos(0)
while i<=10:  #utilizamos un bucle(while) para imprimir los números del 1 al 10
    print(i)
    sum+=i #sum=sum+i #agregamos el valor(i) a la variable(sum)
    i+=1 #i=i+1 #incrementamos el valor de(i) en uno en uno
print('la suma es:',sum) #cuando el bucle termine, se imprime(la suma es:) seguido de esto mostramos el valor de(sum)

i=0             #creamos las variable(i) y le asignamos (0)
sp,si=0,0       #creamos las variables(sp y si) y le adignamos (0,0)
while i<=10:    #utilizamos un bucle(while) para imprimir los números del 1 al 10
    print(i)
    if i%2==0:  #si al dividir(i) entre 2 es 0,entonces es par.
        sp+=i   #se agrega el valor de(i) a la variable(sp) para sumar los pares
    else:       #si el resto de dividir(i) entre 2 es diferente de 0,entonces es impar.
        si+=i   #se agrega el valor de(i) a la variable(si) (suma de impares).
    i+=1
# Al salir del bucle(while), se imprime el mensaje(la suma de los pares es:) seguido del valor de(sp) y tambien el mensaje(la suma de los impares es:) seguido del valor de(si)
print('la suma de los pares es:',sp)
print('la suma de los impares es:',si)
