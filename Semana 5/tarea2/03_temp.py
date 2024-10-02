def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_a_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

def kelvin_a_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32

def main():
    print('1 = Celsius')
    print('2 = Fahrenheit')
    print('3 = Kelvin')
    temp = float(input('Ingrese la temperatura: '))
    escala_og = int(input('Ingrese la escala de la temperatura (1-3): '))
    escala_nueva = int(input('Ingrese la escala a la que desea convertir (1-3): '))

    if escala_og not in [1, 2, 3]:
        print('Ingrese una escala de la lista con su numero correspondiente')
        return

    elif escala_nueva not in [1, 2, 3]:
        print('Ingrese una escala de la lista con su numero correspondiente')
        return

    elif escala_og == 1:
        if escala_nueva == 2:
            print(f'La temperatura en grados Fahrenheit es: {celsius_a_fahrenheit(temp):.1f}')
        else:
            print(f'La temperatura en grados Kelvin es: {celsius_a_kelvin(temp):.1f}')

    elif escala_og == 2:
        if escala_nueva == 1:
            print(f'La temperatura en grados Celsius es: {fahrenheit_a_celsius(temp):.1f}')
        else:
            print(f'La temperatura en grados Kelvin es: {fahrenheit_a_kelvin(temp):.1f}')

    elif escala_og == 3:
        if escala_nueva == 1:
            print(f'La temperatura en grados Celsius es: {kelvin_a_celsius(temp):.1f}')
        else:
            print(f'La temperatura en grados Fahrenheit es: {kelvin_a_fahrenheit(temp):.1f}')

main()

    