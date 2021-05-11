import doctest

def es_primo(numero):


    flag = True
    if abs(numero) == 1:
        flag = False
    elif abs(numero) > 2:
        for i in range (numero):
            if numero % (i+2) == 0 and i < numero - 2:
                flag = False
    
    return flag



print(es_primo(3))


