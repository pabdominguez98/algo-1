def filtrador_de_vocales(cadena):
    v_filter = ''

    for i in range (len(cadena)):
        if cadena[i:i+1] == 'a' or cadena[i:i+1] == 'e' or cadena[i:i+1] == 'i' or cadena[i:i+1] == 'o' or cadena[i:i+1] == 'u':
            pass
        else:
            v_filter += cadena[i:i+1]
    
    return v_filter

print(filtrador_de_vocales("Holanda"))
    