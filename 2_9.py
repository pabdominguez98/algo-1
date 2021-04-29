def sumar_caracteres_numericos(cadena):
    suma = 0
    for i in range (len(cadena)):
        if cadena[i:i+1].isnumeric():
            suma += int(cadena[i:i+1])
    
    return suma


print(sumar_caracteres_numericos("hola1fd4fds5"))