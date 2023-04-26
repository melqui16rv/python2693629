print("Piensa en un número entre 1 y 100. Yo intentaré adivinarlo mediante preguntas.")
min_num, max_num = 1, 100
while True:
    num = (min_num + max_num) // 2
    respuesta = input(f"¿Es el número {num}? (responde 'sí' o 'no') ")
    if respuesta.lower() == "si":
        print("¡Adiviné!")
        break
    elif respuesta.lower() == "no":
        respuesta = input(f"¿Es el número mayor que {num}? (responde 'si' o 'no') ")
        if respuesta.lower() == "si":
            min_num = num + 1
        elif respuesta.lower() == "no":
            max_num = num - 1