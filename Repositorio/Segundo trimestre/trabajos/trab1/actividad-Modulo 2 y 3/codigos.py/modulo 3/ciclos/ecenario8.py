contador = 0
num = 2
while contador < 10:
    es_primo = True
    for divisor in range(2, num):
        if num % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(num)
        contador += 1
    num += 1