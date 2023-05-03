num1=int(input("digite el primer numero: "))
num2=int(input("digite el segundo numero: "))
mayor=max(num1, num2)
menor=min(num1, num2)
cociente=0
while mayor>=menor:
    mayor-=menor
    cociente+=1
print("El cociente de", max(num1, num2), "entre", min(num1, num2), "es:", cociente)
print("El residuo de", max(num1, num2), "entre", min(num1, num2), "es:", mayor)