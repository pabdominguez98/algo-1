def filtrar_pares(lista):
    new_list = []
    for i in range(len(lista)):
      if lista[i] % 2 == 0:
          new_list.append(lista[i])
    
    return new_list


def filtrar_primos(lista):
    new_list = []
    for i in range (len(lista)):
        if lista[i] == 1 or lista[i] == 2:
            new_list.append(lista[i])
        elif lista[i] > 2:
            for j in range (2, lista[i] + 1):

                if lista[i] % j  == 0 and j < lista[i]:
                    
                    break
                elif lista[i] % j == 0 and lista[i] == j:
                    
                    new_list.append(lista[i])
    
    return new_list



def sumar_elementos(lista):
    suma = 0
    for i in range (len(lista)):
        suma += int(lista[i])
    
    return suma


def esta_ordenada(lista):
    for i in range (len(lista)):
        if i < len(lista) -1 :
            if lista[i] > lista[i+1]:
                return False
        
    return True
    

def producto_escalar(vector_1, vector_2):
    prod_escalar = 0
    for i in range (len(vector_1)):
       prod_escalar += vector_1[i] * vector_2[i]
    
    return prod_escalar
    

def letras_en_palabra(letras, frase):
    flag = True
    for i in range (len(letras)):

        flag = False

        for j in range (len(frase)):
            if frase[j:j+1] == letras[i]:
                flag = True
        
        if not flag:
            return False
        
        
    
    return True



    




print(sumar_elementos([1,3,5,5]))

print(filtrar_pares([1,2,3,4,5,6]))

print("Primos:", filtrar_primos([1,2,3,4,5,6,6,43,85,90, 97]))


print(letras_en_palabra(['a', 'b', 'c'], "aabaac"))


print("Esta ordenada:", esta_ordenada([1,2,3,4,5,6,7]))

print("Producto escalar:", producto_escalar([1,2,3], [1,2,3]))

