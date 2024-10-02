entero = int(input('Introduzca un número entero positivo: '))

suma_divisores = 0
divisor = 1

while divisor < entero:
    if entero % divisor == 0:
        suma_divisores += divisor
    divisor += 1

if suma_divisores == entero:
    print('Es perfecto')
else:
    print('No es perfecto')