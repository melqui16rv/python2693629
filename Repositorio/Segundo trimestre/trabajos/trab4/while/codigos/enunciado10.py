m=int(input("digite el primer numero: "))
n=int(input("digite el segundo número: "))
while m!=n:
    if m>n:
        m=m-n
    else:
        n=n-m
print("El m.c.d de los dos numeros es:", m)