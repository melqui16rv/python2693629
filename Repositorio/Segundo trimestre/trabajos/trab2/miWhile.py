num1=int(input("Digite un numero: "))
num2=int(input("Digite otro numero: "))
while num1==num2:
    print("Los numeros son iguales, por favor introducelos de nuevo otros numeros.")
    num1=int(input("Digite un número: "))
    num2=int(input("Digite otro numero: "))
if num1>num2:
    mayor=num1
    menor=num2
else:
    mayor=num2
    menor=num1
resultado=mayor-menor
if resultado==0:
    print("Los números son iguales, no se puede realizar la operación.")
else:
    print(f"El resultado de restar el número menor ({menor}) al mayor ({mayor}) es {resultado} ")
    while resultado>=menor:
        resultado-=menor
    if resultado==0:
        print("No sobra nada.")
    else:
        print(f"Sobra {resultado}.")

        while resultado>=menor:
            resultado-=menor
        if resultado==0:
            print("No sobra nada.")
        else:
            print(f"Sobra {resultado}.")
