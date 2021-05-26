def numeros_al_cuadrado(numero):
    dict = {}
    for i in range (numero):
        dict[i+1]= (pow((i+1), 2))

    return dict

def mezclar_diccionarios(dicc_uno, dicc_dos):
    dicc_uno.update(dicc_dos)
    return dicc_uno
    
def filtrar_por_sumar_diez(diccionario):
    n_dic = {}
    for name in enumerate(diccionario):
        if int(name[1]) + int(diccionario[name[1]]) >= 10:
            n_dic[name[1]] = diccionario[name[1]]
    
    return n_dic
 
def ordenar_valores_por_longitud(diccionario):
    string_list = list(diccionario.values())
    for i in range (1, len(string_list)):
        for j in range (0, len(string_list) - i):
            if (len(string_list[j]) < len(string_list[j+1])):
                aux = string_list[j]
                string_list[j] = string_list[j+1]
                string_list[j+1] = aux
        
    return string_list


print(numeros_al_cuadrado(5))

dicc_1 = {'clave1': 1, 'clave3': 3}
dicc_2 = {'clave2': 2, 'clave4': 'pablo'}

print(mezclar_diccionarios(dicc_1, dicc_2))

print(filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}))


dicc = {'boca':'river', 'pablo':'guarna', 'hola':'algoritmos'}

print(ordenar_valores_por_longitud(dicc))

