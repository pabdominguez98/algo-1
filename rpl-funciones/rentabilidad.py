def interes_compuesto(capital_inicial, tiempo_de_inversion, porcentaje_de_rentabilidad):
    for i in range(tiempo_de_inversion):
        ganancia_anual = float(porcentaje_de_rentabilidad * capital_inicial / 100)
        capital_inicial += float(ganancia_anual)

    return capital_inicial
    
    

print(interes_compuesto(100, 3, 3))