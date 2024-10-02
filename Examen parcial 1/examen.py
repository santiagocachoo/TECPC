# Usa este espacio para probar tu programa
# No olvides copiarlo a Canvas
import math as m

"""
EJERCICIO 1 (prestamos)

def cuota_fija(capital, tasa, tiempo):
  tasa_mensual = tasa/100/12
  n = tiempo * 12
  
  cuota = (capital * tasa_mensual) / (1-(1 + tasa_mensual) ** -n)
  cuotas = [cuota] * n
  return cuotas
  
def cuota_decreciente(capital, tasa, tiempo):
  tasa_mensual = tasa/100/12
  n = tiempo * 12
  capital_mensual = capital / n
  cuotas = []
  
  for mes in range(1, n+1):
    saldo_restante = capital - (capital_mensual * (mes-1))
    interes_mensual = saldo_restante * tasa_mensual
    
    cuota_mes = capital_mensual + interes_mensual
    cuotas.append(cuota_mes)
  return cuotas
  
def mostrar_resumen_prestamo(cuotas, capital):
  total_pagado = sum(cuotas)
  interes_totales = total_pagado - capital
  
  print('Resumen de prestamo:')
  print(f'Total pagado: ${total_pagado:.2f}')
  print(f'Total de intereses pagados: ${interes_totales:.2f}')
  print('Plan de pago completo:')
  
  for mes, cuota in enumerate(cuotas, 1):
    print(f'Mes {mes}: ${cuota:.2f}')

def solicitar_datos():
  while True:
    try:
      capital = float(input('Introduzca el capital del prestamo: '))
      tasa = float(input('Introduzca la tasa de interes anual del prestamo (%): '))
      tiempo = int(input('Introduzca el tiempo del prestamo en años: '))

      if capital <= 0 or tasa <= 0 or tiempo <= 0:
        raise ValueError("Los valores deben ser positivos")
      return capital, tasa, tiempo
    except ValueError as ve:
      print(f'Entrada invalida: {ve}.') 

def main():
  print('Calculadora de prestamos')

  capital, tasa, tiempo = solicitar_datos()

  while True:
    print('1 = Cuota fija')
    print('2 = Cuota decreciente')

    usr = input('Seleccione su tipo de plan de pagos (1 o 2): ')

    match usr:
      case '1':
        cuotas = cuota_fija(capital, tasa, tiempo)
        mostrar_resumen_prestamo(cuotas, capital)
        break
      case '2':
        cuotas = cuota_decreciente(capital, tasa)
        mostrar_resumen_prestamo(cuotas, capital)
        break
      case _:
        print('Opcion invalida. Intente de nuevo')

main()

"""
"""
EJERCICIO 2 (interes simple y compuesto)

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
        tiempo = float(input('Ingrese el tiempo de la inversión en años: '))

        if capital <= 0 or tasa <= 0 or tiempo <= 0:
            raise ValueError('El capital, la tasa y el tiempo deben ser valores positivos')
        if not (0 < tasa < 1):
            raise ValueError('La tasa de interes debe estar entre 0 y 1 (ej: 0.05 para 5%)')
        
        return capital, tasa, tiempo
    except ValueError as ve:
        print(f'Error: {ve}')
        return None, None, None

def main():
    capital, tasa, tiempo = datos()
    if capital is None:
        return
    
    tipo_interes = input('Seleccione el tipo de interes (simple/compuesto): ').lower()

    match tipo_interes:
        case 'simple':
            resultado = interes_simple(capital, tasa, tiempo)
            mostrar_resumen_inversion(resultado)

        case 'compuesto':
            frecuencia = input('Seleccione la frecuencia de capitalizacion (anual, semestral, trimestral, mensual): ').lower()
            resultado = interes_compuesto(capital, tasa, tiempo, frecuencia)
            mostrar_resumen_inversion(resultado)

        case _:
            print('Opción no valida')

main()

"""
"""
EJERCICIO 3 (volumen y area superficial)

def calcular_volumen_esfera(radio):
    return (4/3) * m.pi * radio**3

def calcular_volumen_cono(radio, altura):
    return (1/3) * m.pi * radio**2 * altura

def calcular_volumen_cilindro(radio, altura):
    return m.pi * radio**2 * altura

def calcular_area_superficial_esfera(radio):
    return 4 * m.pi * radio**2

def calcular_area_superficial_cono(radio, altura):
    generatriz = m.sqrt(radio**2 + altura**2)
    return m.pi * radio * (radio + generatriz)

def calcular_area_superficial_cilindro(radio, altura):
    return 2 * m.pi * radio * (radio + altura)


def datos(necesita_altura):
    try:
        radio = float(input('Ingresa el radio: ')) 
        if radio <= 0:
            raise ValueError('El radio debe ser positivo')
        altura = None
        if necesita_altura:
            altura = float(input('Ingrese la altura: '))
            if altura <= 0:
                raise ValueError('La altura debe ser positiva')
        return radio, altura
    except ValueError as ve:
        print(f'Error: {ve}')
        return None, None

def menu():
    print('Seleccione la opción deseada:')
    print('1: Volumen de una esfera')
    print('2: Volumen de un cono')
    print('3: Volumen de un cilindro')
    print('4: Área superficial de una esfera')
    print('5: Área superficial de un cono')
    print('6: Área superficial de un cilindro')

    opcion = input("Escribe el número de la opción: ")

    return opcion

def main():
    opcion = menu()

    match opcion:
        case '1':
            radio, _ = datos(False)
            if radio is not None:
                resultado = calcular_volumen_esfera(radio)
                print(f'El volumen de la esfera es: {resultado:.2f}')
        case '2':  
            radio, altura = datos(True)
            if radio is not None and altura is not None:
                resultado = calcular_volumen_cono(radio, altura)
                print(f"El volumen del cono es: {resultado:.2f}")
        case '3':  
            radio, altura = datos(True)
            if radio is not None and altura is not None:
                resultado = calcular_volumen_cilindro(radio, altura)
                print(f"El volumen del cilindro es: {resultado:.2f}")
        case '4':  
            radio, _ = datos(False)
            if radio is not None:
                resultado = calcular_area_superficial_esfera(radio)
                print(f"El área superficial de la esfera es: {resultado:.2f}")
        case '5':  
            radio, altura = datos(True)
            if radio is not None and altura is not None:
                resultado = calcular_area_superficial_cono(radio, altura)
                print(f"El área superficial del cono es: {resultado:.2f}")
        case '6':  
            radio, altura = datos(True)
            if radio is not None and altura is not None:
                resultado = calcular_area_superficial_cilindro(radio, altura)
                print(f"El área superficial del cilindro es: {resultado:.2f}")
        case _:
            print("Opción no válida.")

main()

"""