"""13. Solicitar al usuario un número de hasta 9 dígitos e
imprimirlo en orden contrario. Ej. digito 6754 imprimo 4576 """
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num = num // 10
    return reversed_num

def run_program():
    num = 0
    while num != -1:
        num = int(input("Ingrese un número de hasta 9 dígitos (o -1 para salir): "))
        if num != -1:
            reversed_num = reverse_number(num)
            print("El número invertido es:", reversed_num)
    print("Fin del programa")
run_program()
