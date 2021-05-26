def cargar_data(localidad, parametros, estadisticas):
    if localidad in estadisticas:
         estadisticas[localidad][0] += parametros[0]
         estadisticas[localidad][1] += parametros[1]
    else:
        estadisticas[localidad] = parametros

    return estadisticas


def calcular_aptos_empleados(estadisticas):
    aptos_empleados = []
    for name in estadisticas:
         aptos_empleados.append((name, estadisticas[name][0], estadisticas[name][1]))

    return aptos_empleados

def calcular_desocupacion(estadisticas):
    desocupacion = []
    for i in range (len(estadisticas)):
        porc_desocupacion = (1 - float(estadisticas[i][2]) / float(estadisticas[i][1])) * 100
        desocupacion.append((estadisticas[i][0], porc_desocupacion))
    
    for i in range (1, len(desocupacion)):
        for j in range (0, len(desocupacion) - i):
            if(int(desocupacion[j][1]) < int(desocupacion[j+1][1])):
                aux = desocupacion[j]
                desocupacion[j] = desocupacion[j+1]
                desocupacion[j+1] = aux

    return desocupacion

def main():
    estadisticas = {}
    condicion = 's'
    while condicion != 'n':
        localidad = input("Ingrese localidad: ")
        personas_en_edad = int(input("Ingrese la cantidad de personas que pueden trabajar: "))
        cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))
        condicion = input("Desea seguir ingresando?(s/n): ")
        parametros = [personas_en_edad, cantidad_empleados]
        estadisticas = cargar_data(localidad, parametros, estadisticas)

    aptos_empleados = calcular_aptos_empleados(estadisticas)  #sin orden aparente

    desocupacion = calcular_desocupacion(aptos_empleados)       #ordenado de mayor a menor

    for i in range (len(aptos_empleados)):
        print("En la localidad de "+aptos_empleados[i][0]+" hay "+str(aptos_empleados[i][1])+" personas en edad laboral y "+str(aptos_empleados[i][2])+" trabajando.")

    for i in range (len(desocupacion)):
        print("La tasa de desocupacion en "+desocupacion[i][0]+" es "+str(desocupacion[i][1])+"%.")
    

main()