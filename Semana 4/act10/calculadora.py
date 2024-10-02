def operación(n1, n2, clave):
    if clave == 's':
        return n1 + n2
    elif clave == 'r':
        return n1 - n2
    elif clave == 'm':
        return n1 * n2
    elif clave == 'd':
        if n2 != 0:
            return n1 / n2
        else:
            return 'No se puede dividir entre cero'
    else:
        return 'La clave es invalida'
    
def main():
    n1 = int(input('introduzca el primer numero entero: '))
    n2 = int(input('introduzca el segundo numero entero: '))
    clave = input('introduzca s para sumar, r para restar, m para multiplicar o d para dividir: ')

    print(f'El resultado de la operación es: {operación(n1, n2, clave)}')

main()