#3.	Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario indique al inicio del programa.
n=int(input("ingrese un numero: "))
fibo=[]
a,b=0,1
while n>0:
    fibo.append(a)
    a,b=b,a+b
    """La operación "n-=1" se utiliza para disminuir el valor de "n" en uno en cada 
    iteración del ciclo, de esta manera se asegura que el ciclo terminará cuando se 
    hayan generado la cantidad de números de Fibonacci que el usuario especificó al 
    inicio."""
    n-=1
print(fibo)