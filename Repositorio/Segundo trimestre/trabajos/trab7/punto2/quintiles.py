import random


def llenarLista():
    tamano = random.randint(15, 125)
    while tamano % 5 != 0:
        tamano = random.randint(15, 125)
    
    llenarLis = []
    for _ in range(tamano):
        altura = round(random.uniform(1.50, 2.00), 2)
        llenarLis.append(altura)
    
    return llenarLis

def calcular_quintiles(lista_alturas):
    lista_ordenada = ordenar_burbuja(lista_alturas)
    tamano = len(lista_ordenada)
    
    quintiles = []
    quintil = 1
    quintil_pos = 0.2
    
    while quintil <= 4:
        index = int(tamano * quintil_pos)
        valor = lista_ordenada[index]
        quintil_info = {
            'quintil': quintil,
            'posicion': index + 1,
            'valor': valor
        }
        quintiles.append(quintil_info)
        
        quintil += 1
        quintil_pos += 0.2
    
    return quintiles


def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista


lista=llenarLista()
print(lista)

quintiles = calcular_quintiles(lista)
print(ordenar_burbuja(lista))
print("Quintiles:", quintiles)


