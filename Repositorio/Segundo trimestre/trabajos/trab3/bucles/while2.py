x=5 #creamos una variable y le asignamos valores que no den residuo(0)
y=3 #creamos una variable y le asignamos valores que no den residuo(0)
#utilizamos while cuando no savemos cuanto se debe de repetir un ciclo
while not (x%y==0 or y%x==0): #si al dividir (X y Y) o (Y y X) y nos dan como residuo(0), negamos con la función(not), para seguir piendo numeros hasta que den factor
    print('Rutina para saber si dos numeros son factores')
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))
    #pedimos un numero y lo almacenamos en las variables(X y Y) como enteros    
print('Son factor') #el siclo se termina cuando se ingresa un factor, por ejemplo(10 para X y 20 para Y)