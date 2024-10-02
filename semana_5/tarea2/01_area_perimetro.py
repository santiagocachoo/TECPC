def a_cuadrado(lado):
    return lado * lado

def p_cuadrado(lado):
    return lado * 4

def a_trapecio(b_mayor, b_menor, altura):
    return ((b_mayor + b_menor) * altura) / 2

def p_trapecio(b_mayor, b_menor, lado1, lado2):
    return b_mayor + b_menor + lado1 + lado2

def a_triangulo(lado, altura):
    return lado * altura / 2

def p_triangulo(lado):
    return lado * 3

def a_rectangulo(base, altura):
    return base * altura

def p_rectangulo(base, altura):
    return (base + altura) * 2

def main():
    print('1 = cuadrado')
    print('2 = trapecio')
    print('3 = triangulo equilatero')
    print('4 = rectangulo')

    figura = int(input('Seleccione una figura (1-4): '))

    if figura not in [1, 2, 3, 4]:
        print('Figura no reconocida. Por favor intente de nuevo')
        return

    operacion = input('Calcular area o perimetro? (a/p): ').lower()

    match figura:
        case 1:
            lado = float(input('Introduzca la medida del lado del cuadrado: '))
            if operacion == 'a':
                print(f'El area del cuadrado es: {a_cuadrado(lado)}')
            elif operacion == 'p':
                print(f'El perimetro del cuadrado es: {p_cuadrado(lado)}')
            else:
                print('Operación no reconocida. Por favor intente de nuevo')

        case 2:
            b_mayor = float(input('Introduzca la medida de la base mayor del trapecio: '))
            b_menor = float(input('Introduzca la medida de la base menor del trapecio: '))       
            if operacion == 'a':
                altura = float(input('Introduzca la medida de la altura del trapecio: '))
                print(f'El area del trapecio es: {a_trapecio(b_mayor, b_menor, altura)}')
            elif operacion == 'p':
                lado1 = float(input('Introduzca la medida del lado 1 del trapecio: '))
                lado2 = float(input('Introduzca la medida del lado 2 del trapecio: '))
                print(f'El perimetro del trapecio es: {p_trapecio(b_mayor, b_menor, lado1, lado2)}')
            else:
                print('Operación no reconocida. Por favor intente de nuevo')

        case 3:
            lado = float(input('Introduzca la medida de un lado del triangulo: '))
            if operacion == 'a':
                altura = float(input('Introduzca la medida de la altura del triangulo: '))
                print(f'El area del triangulo es: {a_triangulo(lado, altura)}')
            elif operacion == 'p':
                print(f'El perimetro del triangulo es: {p_triangulo(lado)}')
            else:
                print('Operación no reconocida. Por favor intente de nuevo')
        
        case 4:
            base = float(input('Introduzca la medida de la base del rectangulo: '))
            altura = float(input('Introduzca la medida de la altura del rectangulo: '))
            if operacion == 'a':
                print(f'El area del rectangulo es: {a_rectangulo(base, altura)}')
            elif operacion == 'p':
                print(f'El perimetro del rectangulo es: {p_rectangulo(base, altura)}')
            else:
                print('Operación no reconocida. Por favor intente de nuevo')
        
main()