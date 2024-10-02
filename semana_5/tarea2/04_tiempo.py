def segundos_a_minutos(segundos):
    return segundos / 60

def minutos_a_horas(minutos):
    return minutos / 60

def horas_a_dias(horas):
    return horas / 24

def dias_a_horas(dias):
    return dias * 24

def horas_a_minutos(horas):
    return horas * 60

def minutos_a_segundos(minutos):
    return minutos * 60

def main():
    print('s = segundos')
    print('m = minutos')
    print('h = horas')
    print('d = dias')
    print('Operaciones disponibles: s-m, m-h, h-d, d-h, h-m, m-s')

    tiempo_og = input('Ingrese la unidad de tiempo (s/m/h/d): ').lower()
    tiempo_nuevo = input('Ingrese la unidad de tiempo a la que desea convertir (s/m/h/d): ')
    tiempo = float(input('Ingrese la cantidad de tiempo: '))

    if tiempo_og == 's':
        if tiempo_nuevo == 'm':
            print(f'El equivalente en minutos es: {segundos_a_minutos(tiempo):.2f}')
        else: 
            print('Operación no valida')
        
    elif tiempo_og == 'm':
        if tiempo_nuevo == 'h':
            print(f'El equivalente en horas es: {minutos_a_horas(tiempo):.2f}')
        elif tiempo_nuevo == 's':
            print(f'El equivalente en segundos es: {minutos_a_segundos(tiempo):.2f}')
        else:
            print('Operación invalida')

    elif tiempo_og == 'h':
        if tiempo_nuevo == 'd':
            print(f'El equivalente en dias es: {horas_a_dias(tiempo):.2f}')
        elif tiempo_nuevo == 'm':
            print(f'El equivalente en minutos es: {horas_a_minutos(tiempo):.2f}')

    elif tiempo_og == 'd':
        if tiempo_nuevo == 'h':
            print(f'El equivalente en horas es: {dias_a_horas(tiempo):.2f}')
        else:
            print('Operación invalida')
    
    else:
        print('Operación invalida')


main()