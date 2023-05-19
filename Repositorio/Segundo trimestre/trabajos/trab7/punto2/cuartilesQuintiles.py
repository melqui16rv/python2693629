import random

def llenarLista():
    tam = random.randint(15, 125)
    while tam % 5 != 0:
        tam = random.randint(15, 125)
    
    llenarLis = []
    for _ in range(tam):
        altura = round(random.uniform(1.50, 2.00), 2)
        llenarLis.append(altura)
    
    return llenarLis

def hallarC(lista_alturas):
    listOrdenada = mBor(lista_alturas)
    tam = len(listOrdenada)
    
    cuartil1 = listOrdenada[int(tam * 0.25)]
    cuartil2 = listOrdenada[int(tam * 0.5)]
    cuartil3 = listOrdenada[int(tam * 0.75)]
    cuartil4 = listOrdenada[int(tam * 1) - 1]  # Ajuste en el cálculo del índice
    
    rango1 = f"1-{lista_alturas.index(cuartil1)}"
    rango2 = f"{lista_alturas.index(cuartil1)+1}-{lista_alturas.index(cuartil2)}"
    rango3 = f"{lista_alturas.index(cuartil2)+1}-{lista_alturas.index(cuartil3)}"
    rango4 = f"{lista_alturas.index(cuartil3)+1}-{len(lista_alturas)}"
    
    return cuartil1, cuartil2, cuartil3, cuartil4, rango1, rango2, rango3, rango4

def calcular_quintiles(lista_alturas):
    listOrdenada = mBor(lista_alturas)
    tam = len(listOrdenada)
    
    quintil1 = listOrdenada[int(tam * 0.2)]
    quintil2 = listOrdenada[int(tam * 0.4)]
    quintil3 = listOrdenada[int(tam * 0.6)]
    quintil4 = listOrdenada[int(tam * 0.8)]
    quintil5 = listOrdenada[int(tam * 1) - 1]  # Ajuste en el cálculo del índice
    
    return quintil1, quintil2, quintil3, quintil4, quintil5

def mBor(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

lista = llenarLista()

print('La lista generada es: ')
print(lista)

print('La lista ordenada es: ')
print(mBor(lista))
opcion = input("Si quieres hallar los quintiles, ingresa '5'; si deseas hallar los cuartiles, ingresa '4': ")

if opcion == '5':
    quintil1, quintil2, quintil3, quintil4, quintil5 = calcular_quintiles(lista)
    
    rango1 = f"1-{lista.index(quintil2)}"
    rango2 = f"{lista.index(quintil2)+1}-{lista.index(quintil3)}"
    rango3 = f"{lista.index(quintil3)+1}-{lista.index(quintil4)}"
    rango4 = f"{lista.index(quintil4)+1}-{lista.index(quintil5)}"
    rango5 = f"{lista.index(quintil5)+1}-{len(lista)}"
    
    print("Quintiles:")
    print("Quintil 1:", quintil1, "(Rango:", rango1, ")")
    print("Quintil 2:", quintil2, "(Rango:", rango2, ")")
    print("Quintil 3:", quintil3, "(Rango:", rango3, ")")
    print("Quintil 4:", quintil4, "(Rango:", rango4, ")")
    print("Quintil 5:", quintil5, "(Rango:", rango5, ")")

elif opcion == '4':
    cuartil1, cuartil2, cuartil3, cuartil4, rango1, rango2, rango3, rango4 = hallarC(lista)

    print("Cuartiles:")
    print("Cuartil 1:", cuartil1, "(Rango:", rango1, ")")
    print("Cuartil 2:", cuartil2, "(Rango:", rango2, ")")
    print("Cuartil 3:", cuartil3, "(Rango:", rango3, ")")
    print("Cuartil 4:", cuartil4, "(Rango:", rango4, ")")
    
else:
    print("la opción no es valida. ")

