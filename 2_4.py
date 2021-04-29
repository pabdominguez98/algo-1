def es_capicua(palabra):
    palabra_invertida = ''
    for i in range (len(palabra)):
        palabra_invertida += palabra[len(palabra)-1-i:len(palabra)-i]
    
    if palabra_invertida == palabra:
        return True
    else:
        return False

print(es_capicua("newquen"))