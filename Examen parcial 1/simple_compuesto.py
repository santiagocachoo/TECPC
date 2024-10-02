def interes_simple(capital, tasa, tiempo):
    return capital * (1 + tasa * tiempo)

def interes_compuesto(capital, tasa, tiempo, frecuencia):
    frecuencias = {'anual': 1, 'semestral': 2, 'trimestral': 4, 'mensual': 12}
    n = frecuencias.get(frecuencia, 1)
    return capital * (1 + tasa / n) ** (n * tiempo)

def mostrar_resumen_inversion(resultado):
    print(f'Despues del tiempo indicado, el valor de su inversión es: {resultado}')

def datos():
    try:
        capital = float(input('Ingrese el capital inicial: '))
        tasa = float(input('Ingrese la tasa de interes en decimales (ej: 0.05 para 5%): '))
        tiempo = int(input('Ingrese el tiempo de la inversión en años: '))

        if capital <= 0 or tasa <= 0 or tiempo <= 0:
            raise ValueError('El capital, la tasa y el tiempo deben ser valores positivos')
        if not (0 < tasa < 1):
            raise ValueError('La tasa de interes debe estar entre 0 y 1 (ej: 0.05 para 5%)')
        
        return capital, tasa, tiempo
    except ValueError as ve:
        print(f'Error: {ve}')
        return None, None, None
    
    

        