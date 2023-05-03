num = input("digite un numero de 1 hasta 9 digitos: ")
while len(num)>9:
    num = input("El numero tiene mas de 9 digitos, ingrese un numero nuevo ")
i = len(num)-1
while i>=0:
    print(num[i], end="")
    i-=1