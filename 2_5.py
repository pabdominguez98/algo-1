def insertar_separadores(cadena, separador, espaciado):
    cadena_separada = ''
    contador = 0
    for i in range (len(cadena)):
        if contador == espaciado:
            cadena_separada += separador
            contador = 0
        cadena_separada += cadena[i: i+1]
        contador += 1
    
    return cadena_separada

print(insertar_separadores("holacomoestas", "|", 4))
        
  