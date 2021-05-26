from campeonato import campeonato

def calcular_campeon(estadisticas):
    maximo = 0
    campeon = ()
    for clave in estadisticas:
        puntos = int(estadisticas[clave][0]*3) + int(estadisticas[clave][1])
        if puntos > maximo:
            campeon = (clave, puntos)
            maximo = puntos

    return campeon

def calcular_equipo_que_desciende(estadisticas):
    minimo = 100
    desciende = ()
    for clave in estadisticas:
        puntos = int(estadisticas[clave][0]*3) + int(estadisticas[clave][1])
        if puntos < minimo:
            desciende = (clave, puntos)
            minimo = puntos
            
    return desciende

def calcular_mas_empatado(estadisticas):
    maximo = 0
    mas_empatado = ()
    for clave in estadisticas:
        puntos = int(estadisticas[clave][1])
        if puntos > maximo:
            mas_empatado = (clave, puntos)
            maximo = puntos

    return mas_empatado

def mejor_ratio_equipo(estadisticas):
    maximo = 0.0
    campeon = ()
    for clave in estadisticas:
        puntos = float(estadisticas[clave][3]) / float(estadisticas[clave][4])
        if puntos > maximo:
            campeon = (clave, puntos)
            maximo = puntos

    return campeon



def main():
    campeon = calcular_campeon(campeonato)
    desciende = calcular_equipo_que_desciende(campeonato)
    mas_empatado = calcular_mas_empatado(campeonato)
    mejor_ratio = mejor_ratio_equipo(campeonato)
    print('El equipo campeon es', campeon[0], 'con', campeon[1], 'puntos.')
    print('El equipo que desciende es', desciende[0], 'con', desciende[1], 'puntos.')
    print('El equipo que mas partidos empato es', mas_empatado[0], 'con', mas_empatado[1], 'partidos.')
    ratio = "El equipo con mejor proporcion goleadora es "+mejor_ratio[0]+" con "+str(mejor_ratio[1])+"."
    print(ratio)


main()