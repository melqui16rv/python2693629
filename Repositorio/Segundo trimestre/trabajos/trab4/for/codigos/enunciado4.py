def numero_perfecto(n):
    sum=0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
numeros_p = []
for i in range(1, 1001):
    if numero_perfecto(i):
        numeros_p.append(i)
print("Hay", len(numeros_p), "numeros perfectos entre 1 y 1000. Son:", numeros_p)

