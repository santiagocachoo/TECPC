x = float(input('Introduzca la medida del lado 1: '))
y = float(input('Introduzca la medida del lado 2: '))
z = float(input('Introduzca la medida del lado 3: '))

if x <= 0 or y <= 0 or z <= 0:
    print('El triangulo no es valido (Los lados deben ser mayores a 0)')
elif x + y <= z or x + z <= y or y + z <= x:
    print('El triangulo no es valido (Los lados no cumplen las condiciones para formar un triangulo)')
else: 
    if x == y == z:
        print('El triangulo ingresado es un triangulo rectangulo')
    elif x == y or y == z or x == z:
        print('El triangulo ingresado es un triangulo isosceles')
    else:
        print('El triangulo ingresado es un triangulo escaleno')

lados = sorted([x, y, z])
a, b, c = lados
if a**2 + b**2 == c**2:
    print('El triangulo es un triangulo rectangulo')