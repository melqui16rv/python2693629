#3.	Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario indique al inicio del programa.
n=int(input("ingrese un numero: "))
fibo=[]
a,b=0,1
while n>0:
    fibo.append(a)
    a,b=b,a+b
    n-=1
print(fibo)