def equivalente(horas, minutos, segundos):
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos

def main():
    h1 = float(input('Introduzca las horas del primer proceso: '))
    m1 = float(input('Introduzca los minutos del primer proceso: '))
    s1 = float(input('Introduzca los segundos del primer proceso: '))
    tiempo_1 = equivalente(h1, m1, s1)
    print(f'El tiempo en segundos del primer proceso es: {tiempo_1} segundos.')

    h2 = float(input('Introduzca las horas del segundo proceso: '))
    m2 = float(input('Introduzca los minutos del segundo proceso: '))
    s2 = float(input('Introduzca los segundos del segundo proceso: '))
    tiempo_2 = equivalente(h2, m2, s2)
    print(f'El tiempo en segundos del segundo proceso es: {tiempo_2} segundos.')

main()
