#creamos dos variables con nombres (num1 y num2) a estas variables le asignamos los valores (100 y 25) 
num1,num2=100,25
#se imprimen cuatro opciones para que el usuario elija qué operación matemática desea realizar: sumar, restar, multiplicación o divición
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
selector=(input('Digite la opcion')) #se le solicita al usuario que ingrese una opción seleccionando el número correspondiente a la operación que desea realizar
match selector: #con la función match nos ayuda a evaluar la opción ingresada por el usuario.
                #si el usuario ingrasa una de las opciones(1,2,3 o 4) esta hace una determinada función

    case '1': # Si el valor ingresado es '1', se imprime la suma de 'num1' y 'num2'.
        print(num1+num2)
    case '2': # Si el valor es '2', se imprime la resta de 'num1' y 'num2'.
        print(num1-num2)
    case '3': # Si el valor es '3', se imprime el producto de 'num1' y 'num2'.
        print(num1*num2)
    case '4': # Si el valor es '4', se imprime el cociente de 'num1' y 'num2'.
        print(num1/num2)