contraseña = input("Ingrese una contraseña: ")
if len(contraseña) < 8:
    print("La contraseña es insegura")
else:
    mayusculas = False
    minusculas = False
    numeros = False
    simbolos = False
    for caracter in contraseña:
        if caracter.isupper():
            mayusculas = True
        elif caracter.islower():
            minusculas = True
        elif caracter.isnumeric():
            numeros = True
        else:
            simbolos = True
    if mayusculas and minusculas and numeros and simbolos:
        print("La contraseña es segura")
    else:
        print("La contraseña es insegura")
