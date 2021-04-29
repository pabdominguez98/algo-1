def numeros_positivos(numero):
    array_positivos = []
    for i in range(numero):
        array_positivos.append[i+1]

    return array_positivos


def numeros_positivos_pares(numero):
    array_pares = []
    for i in range(numero):
        if (i+1) % 2 == 0:
            array_pares.append(i+1)

    return array_pares


def numeros_positivos_pares_cuadrado(numero):
    array_pares_cuadrados = []
    for i in range(numero):
        if (i+1) % 2 == 0:
            array_pares_cuadrados.append(pow((i+1), 2))

    return array_pares_cuadrados


def impares_al_cuadrado(lista):
   array_impares_cuadrados = [1, 2, 3]
   for i in range(len(lista)):
       if lista[i] % 2 != 0:
           array_impares_cuadrados.append(pow(lista[i], 2))
       else:
           array_impares_cuadrados.append(lista[i])


    return array_impares_cuadrados

    
    
def filtrar_tuplas_por_suma(lista_de_tuplas):
    suma_tuplas = []
    for i in range (len(lista_de_tuplas)):
        if (lista_de_tuplas[i][0]) + (lista_de_tuplas[i][1]) >= 0:
            suma_tuplas.append(lista_de_tuplas[i])

    return suma_tuplas
    
def filtrar_tupla_elemento_par(lista_de_tuplas):
    elementos_par = []
    for i in range (len(lista_de_tuplas)):
        if lista_de_tuplas[i][0] % 2 == 0 or lista_de_tuplas[i][1] % 2 == 0:
            elementos_par.append(lista_de_tuplas[i])
    
    return elementos_par

print (numeros_positivos(4))
