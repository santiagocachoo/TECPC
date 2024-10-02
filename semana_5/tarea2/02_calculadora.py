def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        return 'Error: No se puede dividir entre cero'
    return n1 / n2

def div_entera(n1, n2):
    if n2 == 0:
        return 'Error: No se puede dividir entre cero'
    return n1 // n2

def modulo(n1, n2):
    if n2 == 0:
        return 'Error: No se puede dividir entre cero'
    return n1 % n2

def exp(n1, n2):
    return n1 ** n2

def main():
    print('1 = suma')
    print('2 = resta')
    print('3 = multiplicación')
    print('4 = división')
    print('5 = división entera')
    print('6 = modulo')
    print('7 = exponenciación')

    operacion = int(input('Seleccione su operación deseada (1-7): '))

    if operacion not in [1, 2, 3, 4, 5, 6, 7]:
        print('Operación no reconocida. Por favor intente de nuevo')
        return

    n1 = float(input('Ingrese el primer numero: '))
    n2 = float(input('Ingrese el segundo numero (o la potencia, si es el caso): '))

    if operacion == 1:
        print(f'El resultado es: {suma(n1, n2)}')
    
    elif operacion == 2:
        print(f'El resultado es: {resta(n1, n2)}')

    elif operacion == 3:
        print(f'El resultado es: {multiplicacion(n1, n2)}')

    elif operacion == 4:
        print(f'El resultado es: {division(n1, n2)}')

    elif operacion == 5:
        print(f'El resultado es: {div_entera(n1, n2)}')

    elif operacion == 6:
        print(f'El resultado es: {modulo(n1, n2)}')

    elif operacion == 7:
        print(f'El resultado es: {exp(n1, n2)}')

    else:
        print('Operación no reconocida. Por favor intente de nuevo')


main()

