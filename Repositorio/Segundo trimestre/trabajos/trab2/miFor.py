fin=int(input("Digite un limite de la serie: "))
cantidad=int(input("Digite la cantidad de cuanto va a ir incrementando o decrementando: "))
if cantidad>0:
    serie=range(0, fin+1, cantidad)
else:
    serie=range(fin, -1, cantidad)
print("Serie generada:")
for num in serie:
    print(num, end=' ')
n = int(input("\nIntroduce un número positivo para contar sus múltiplos: "))
while n<=0:
    n=int(input("El número debe ser positivo, introduce uno nuevo: "))
multiplos=0
for num in range(fin+1):
    if num%n==0:
        multiplos+=1
print(f"Hay {multiplos} multiplos de {n} en la serie.")
