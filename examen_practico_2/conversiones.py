# funciones de conversión
def convertir_longitud(valor, unidad_origen, unidad_destino):
    conversiones = {
        'metros': 1,
        'kilometros': 1000,
        'millas': 1609.34,
        'pies': 0.3048
    }

    try: 
        factor_origen = conversiones[unidad_origen.lower()]
        factor_destino = conversiones[unidad_destino.lower()]
        return valor * (factor_origen / factor_destino)
    except KeyError:
        raise ValueError('Unidad de medida no valida')
    
def convertir_masa(valor, unidad_origen, unidad_destino):
    conversiones = {
        'kilogramos': 1,
        'gramos': 0.001,
        'libras': 0.453592,
        'onzas': 0.0283495
    }

    try:
        factor_origen = conversiones[unidad_origen.lower()]
        factor_destino = conversiones[unidad_destino.lower()]
        return valor * (factor_origen / factor_destino)
    except KeyError:
        raise  ValueError('Unidad de masa no valida')
    
def convertir_energia(valor, unidad_origen, unidad_destino):
    conversiones = {
        'julios': 1,
        'calorias': 4.184,
        'kilovatios-hora': 3600000
    }
    
    try:
        factor_origen = conversiones[unidad_origen.lower()]
        factor_destino = conversiones[unidad_destino.lower()]
        return valor * (factor_origen / factor_destino)
    except KeyError:
        raise ValueError('Unidad de energia no valida')
    
# funcion para guardar archivo.txt
def guardar_conversiones(lista_conversiones, nombre_archivo='conversiones.txt'):
    with open(nombre_archivo, 'a') as archivo:
        for conversion in lista_conversiones:
            archivo.write(f'Se convirtio {conversion[0]} {conversion[1]} en {conversion[2]} {conversion[3]}.\n')

# funcion de menu
def mostrar_menu():
    print("\nMenú de Conversión:")
    print("1. Convertir longitud (metros, kilómetros, millas, pies)")
    print("2. Convertir masa (kilogramos, gramos, libras, onzas)")
    print("3. Convertir energía (julios, calorías, kilovatios-hora)")
    print("4. Salir")

# funcion main
def main():
    lista_conversiones = []

    while True:
        mostrar_menu()

        try:
            opcion = int(input('Elija una opcion: '))

            match opcion:
                case 1:
                    valor = float(input('Ingrese el valor a convertir: '))
                    unidad_origen = input('Ingrese la unidad origen: ')
                    unidad_destino = input('Ingrese la unidad destino: ') 
                    resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
                    lista_conversiones.append((valor, unidad_origen, resultado, unidad_destino, 'longitud'))
                case 2: 
                    valor = float(input('Ingrese el valor a convertir: '))
                    unidad_origen = input('Ingrese la unidad origen: ')
                    unidad_destino = input('Ingrese la unidad destino: ')
                    resultado = convertir_masa(valor, unidad_origen, unidad_destino)
                    lista_conversiones.append((valor, unidad_origen, resultado, unidad_destino, 'masa'))
                case 3: 
                    valor = float(input('Ingrese el valor a convertir: '))
                    unidad_origen = input('Ingrese la unidad origen: ')
                    unidad_destino = input('Ingrese la unidad destino: ')
                    resultado = convertir_energia(valor, unidad_origen, unidad_destino)
                    lista_conversiones.append((valor, unidad_origen, resultado, unidad_destino, 'energia'))
                case 4:
                    print('Saliendo del programa, adios...')
                    guardar_conversiones(lista_conversiones)
                    break
                case _:
                    print('Opción no valida. Intente de nuevo.')
                    continue

            if opcion != 4:
                print(f'{valor} {unidad_origen} es igual a {resultado:.4f} {unidad_destino}.')
        
        except ValueError as ve:
            print(f'Error: {ve}. Ingrese datos validos.')

main()

                
    

    