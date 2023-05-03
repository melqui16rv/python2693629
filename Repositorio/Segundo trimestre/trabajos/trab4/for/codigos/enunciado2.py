num1=int(input("Digite un numero: "))
contador=0
for i in range(1,num1+1):
    if num1%i==0:
        contador+=1
if contador==2:
    print("el numero es primo")
else:
    print("el numero no es primo")