def ordenar_lista_menor_a_mayor(lista):
    for i in range (1, len(lista)):
        for j in range (0, len(lista) - i):
            if lista[j] > lista[j+1]:
                temp = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = temp
            
    return lista


def ordenar_lista_mayor_a_menor(lista):
    for i in range (1, len(lista)):
        for j in range (0, len(lista)-i):
            if(lista[j] < lista[j+1]):
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp

    return lista

    

def ordenar_lista_alfabeticamente(lista):
  
    for i in range (1, len(lista)):
        for j in range (0, len(lista) - 1):
            if ord(lista[j][0:1]) > ord(lista[j+1][0:1]):
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
            elif ord(lista[j][0:1]) == ord(lista[j+1][0:1]):
                if ord(lista[j][1:2]) > ord(lista[j+1][1:2]):
                    temp = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = temp
    
    return lista

def ordenar_palabras_por_longitud(lista):
  
    for i in range (len(lista)):
        minimo = i
        for j in range (i, len(lista)):
            
            if len(lista[j]) > len(lista[minimo]):
                minimo = j
        
        if minimo != i:
            temp = lista[i]
            lista[i] = lista[minimo]
            lista[minimo] = temp
        
    return lista
 
    
def ordenar_lista_por_tupla(lista):
    for i in range (1, len(lista)):
        for j in range (0, len(lista) - i):
            if lista[j][1] < lista[j+1][1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    
    return lista

def ordenar_lista_por_suma_tupla(lista):
    for i in range (1, len(lista)):
        for j in range (0, len(lista) - i):
            if (lista[j][0] + lista[j][1]) < (lista[j+1][0] + lista[j+1][1]):
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    
    return lista
    


print(ordenar_lista_menor_a_mayor([5,2,6,34,4,1]))
print(ordenar_lista_mayor_a_menor([5,2,6,23,4,1]))

print(ordenar_lista_alfabeticamente( ['de', 'lista', 'ordenar', 'probando', 'palabras'] ))

print(ordenar_palabras_por_longitud(["hola", "estas", "como", "si", "string largo", "a"]))

print(ordenar_lista_por_tupla([(1,2), (2,3), (6,7), (5,4), (7,1)]))

print(ordenar_lista_por_suma_tupla([(1, 5), (7, 3), (5, 4), (4, 3)]))