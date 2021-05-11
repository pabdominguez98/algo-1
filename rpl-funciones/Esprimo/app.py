def es_primo(numero):
    
    if abs(numero == 2) or abs(numero) == 3:
        return True
    elif numero == 1:
        return False
    elif(numero > 3):
        for i in range (numero):
            if(numero % (i+2) == 0) and (i < (numero - 2)):
                return False

    return True



def suma_de_numeros_primos(numero):
    suma = 0
    for i in range (numero):
        if es_primo(i+1) == True:
            suma += (i+1)

    return suma


print(suma_de_numeros_primos(17))



