calificacion = int(input("Ingrese su calificación: "))
if calificacion >= 90:
  nota = "A"
elif calificacion >= 80:
  nota = "B"
elif calificacion >= 70:
  nota = "C"
elif calificacion >= 60:
  nota = "D"
else:
  nota = "F"
print("Su nota equivalente es:", nota)