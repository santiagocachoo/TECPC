def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2*(base + altura)

def main():
    base = float(input('Introduza la medida de la base del rectangulo: '))
    altura = float(input('Introduzca la medida de la altura del rectangulo: '))

    eleccion = input('Quieres calcular perimetro o area? (a para area, p para perimetro): ')

    if eleccion == 'a':
        print(f'El area del rectangulo es: {area_rectangulo(base, altura)} cm cuadrados.')
    elif eleccion == 'p':
        print(f'El perimetro del rectangulo es: {perimetro_rectangulo(base, altura)} cm.')
    else:
        print('La clave es invalida. Por favor, elija a o p dependiendo de lo que quiera calcular.')

main()
