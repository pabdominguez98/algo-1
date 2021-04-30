def ultimos_tres_elementos(lista):
    lista_3 = []
    if len(lista) > 3:
        lista_3.append(lista[len(lista)-3])
        lista_3.append(lista[len(lista)-2])
        lista_3.append(lista[len(lista)-1])
    
    else:
        lista_3 = lista
    
    return lista_3

    
def ultimos_tres_elementos_concatenados(lista):
    lista_concat = []
    lista_concat.append(lista[0][len(lista[0])-3])
    lista_concat.append(lista[0][len(lista[0])-2])
    lista_concat.append(lista[0][len(lista[0])-1])
    lista_concat.append(lista[1][len(lista[1])-3])
    lista_concat.append(lista[1][len(lista[1])-2])
    lista_concat.append(lista[1][len(lista[1])-1])
    lista_concat.append(lista[2][len(lista[2])-3])
    lista_concat.append(lista[2][len(lista[2])-2])
    lista_concat.append(lista[2][len(lista[2])-1])

    return lista_concat
    
def indices_pares(lista):

    lista_pares = []
    for i in range (len(lista)):
        if i % 2 == 0:
            lista_pares.append(lista[i])
    
    return lista_pares
    
def indices_impares(lista):
    lista_impares = []

    for i in range (len(lista)):
        if i % 2 != 0:
            lista_impares.append(lista[i])

    return lista_impares

def invertir(lista):
    lista_ivertida = []
    for i in range (len(lista)):
        lista_ivertida.append(lista[(len(lista)-1)-i])

    return lista_ivertida

print(ultimos_tres_elementos([5,3,6,2,5,32,6,4,7]))

print(ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]]))

print(indices_pares(["a","b","c","d","e", "f"]))

print(indices_impares(["a","b","c","d","e", "f"]))


print(invertir([1,2,3,4,5]))