a = int(input('Introduzca el numero menor: '))
b = int(input('Introduzca el numero mayor: '))

while a <= b:
    if a % 2 == 0:
        print(a)
    a += 1