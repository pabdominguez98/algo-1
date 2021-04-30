def numeros_positivos(numero):
    lista = []
    for i in range (numero):
        lista.append(i+1)
    return lista

def numeros_positivos_pares(numero):
    lista = []
    for i in range (numero):
        if (i+1) % 2 == 0:
            lista.append(i+1)
    
    return lista
    
def numeros_positivos_pares_cuadrado(numero):
    lista = []
    for i in range (numero):
        if(i+1) % 2 == 0:
            lista.append(pow((i+1), 2))
    
    return lista

def impares_al_cuadrado(lista):
    lista_nueva = []
    for i in range (len(lista)):
        if lista[i] % 2 != 0:
            lista_nueva.append(pow(lista[i], 2))
        else:
            lista_nueva.append(lista[i])
    
    return lista_nueva

def filtrar_tuplas_por_suma(lista_de_tuplas):
    lista = []
    for i in range (len(lista_de_tuplas)):
        if lista_de_tuplas[i][0] + lista_de_tuplas[i][1] >= 0:
            lista.append(lista_de_tuplas[i])
    
    return lista

    
def filtrar_tupla_elemento_par(lista_de_tuplas):
    lista = []
    for i in range (len(lista_de_tuplas)):
        if lista_de_tuplas[i][0] % 2 == 0 or lista_de_tuplas[i][1] % 2 == 0:
            
            lista.append(lista_de_tuplas[i])

    return lista
        


print (numeros_positivos(5))

print(numeros_positivos_pares(7))

print(numeros_positivos_pares_cuadrado(7))

print(impares_al_cuadrado([1,2,3,4,5,6,7]))

print(filtrar_tuplas_por_suma([(7, -5), (4, -5), (1, 2), (1, -2)]))

print(filtrar_tupla_elemento_par([(7, -5), (4, -5), (1, 2), (1, -2)]))