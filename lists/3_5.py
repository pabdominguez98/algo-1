def es_primo(numero):
    numero = abs(numero)
    flag = True
    if numero == 1 or numero == 2:
        flag = True
    elif numero > 2:
        for i in range (numero -1):
            if (numero % (i+2) == 0) and (i < numero -2):
                flag = False

    return flag



def filtrar_primos(numeros, menor_numero):
    lista_primos = []
    for i in range (len(numeros)):
        if es_primo(numeros[i]) and numeros[i] > menor_numero:
            lista_primos.append(numeros[i])
    
    return lista_primos

def ordenar_por_longitud_de_tuplas(tuplas):
    for i in range (1, len(tuplas)):
        for j in range (0, len(tuplas) - i):
            if len(tuplas[j]) < len(tuplas[j+1]):
                temp = tuplas[j]
                tuplas[j] = tuplas[j+1]
                tuplas[j+1] = temp
            
    return tuplas



def concatenar_primeros_elementos(lista):
    lista_concatenada = []
    for i in range (len(lista)):
        #si fueran mas parametros usaria un for.. pero para asignar dos parametros, los escribo a mano
        lista_concatenada.append(lista[i][0])
        lista_concatenada.append(lista[i][1])
    
    return lista_concatenada




print(filtrar_primos([11, 7, 3, 19], 15))

lista_tuplas = [(1,5,6), (1,2), (1), (6,4,5,6), ("asd", 9, 5.6, "l", "s")]

print(ordenar_por_longitud_de_tuplas(lista_tuplas))

lista = [[1,4,5,6], [2,3,4,5], [6,4,4,6,7,8], [5,6,7,3,5,6,4]]

print(concatenar_primeros_elementos(lista))
