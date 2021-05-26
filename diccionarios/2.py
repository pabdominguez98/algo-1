
def sumar_votos(partido, votos, diccionario):
    if partido in diccionario:
        diccionario[partido] = diccionario[partido] + votos
    else: 
        diccionario[partido] = votos

    return diccionario

def ordenar_partidos(partidos):
     partidos = list(partidos.items())
     for i in range(1, len(partidos)):
         for j in range(0, len(partidos) - i):
             if(partidos[j][1] < partidos[j+1][1]):
                 aux = partidos[j]
                 partidos[j] = partidos[j+1]
                 partidos[j+1] = aux

     return partidos    
        


def main():
    status = 's'
    partidos = {}
    while status != 'n':
        partido = input("Ingrese el partido a sumarle votos: ")
        votos = int(input("Ingrese la cantidad de votos a sumarle: "))
        status = input("Desea seguir ingresando?(s/n): ")
        partido = sumar_votos(partido, votos, partidos)
    partidos = ordenar_partidos(partidos)
     
    for i in range(len(partidos)):
        print('El partido', partidos[i][0], 'obtuvo', partidos[i][1], 'votos.')



   
main()