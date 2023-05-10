"""Solicitar 2 números al usuario e imprimir el cociente y el
residuo del mayor en el menor sin utilizar la división ni el mod. """
def obtener_cociente_residuo(num1, num2):
    mayor = max(num1, num2)
    menor = min(num1, num2)
    cociente = mayor // menor
    residuo = mayor % menor
    return (cociente, residuo)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

cociente, residuo = obtener_cociente_residuo(num1, num2)

print(f"El cociente del mayor en el menor es: {cociente}")
print(f"El residuo  del mayor en el menor es: {residuo}")
