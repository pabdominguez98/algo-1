def suma_de_divisores(numero):
    suma = 0
    for i in range (numero):
        if i > 1 and numero % i == 0:
            suma += i
    
    return suma

print(suma_de_divisores(32))