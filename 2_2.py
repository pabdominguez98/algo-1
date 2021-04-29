def contar_caracteres(cadena, caracter_1, caracter_2):
    contador = 0
    for i in range (len(cadena)):
        if cadena[i:i+1] == caracter_1 or cadena[i:i+1] == caracter_2:
            contador = contador + 1
    
    return contador


print(contar_caracteres("Carlooos", "a", "o"))