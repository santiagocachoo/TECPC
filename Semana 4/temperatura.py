temp = float(input('Introduzca la temperatura en grados celcius (solo el numero): '))

if temp < 0:
    print('Temperatura congelante')
elif temp <= 10:
    print('Temperatura fria')
elif temp <= 25:
    print('Temperatura templada')
elif temp <= 35:
    print('Temperatura caliente')
else: 
    print('Temperatura extrema')