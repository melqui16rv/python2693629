edad = int(input("Ingrese su edad: "))
ciudadano = input("¿Es usted ciudadano? (sí o no): ")
if edad >= 18 and ciudadano == "sí":
 print("Usted puede votar")
else:
 print("Usted no puede votar")