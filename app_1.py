nota = 1
contador = 0
suma = 0

while nota != 0:
    nota = int(input("Ingrese una nota:"))
    if nota > 0 and nota < 11:
        contador = contador + 1
        suma += nota

promedio = suma / contador

print("El promedio final es:", promedio)
