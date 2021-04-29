def precendencia_de_caracteres(cadena, caracter_1, caracter_2):
    comb_count = 0

    for i in range (len(cadena)):
        if cadena[i:i+1] == caracter_1 and cadena[i+1:i+2] == caracter_2:
            comb_count += 1
    
    return comb_count


print(precendencia_de_caracteres("hola holanda sapent", "h", "o"))
