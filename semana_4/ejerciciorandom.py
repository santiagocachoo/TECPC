valor = input('Introduzca comando (start, stop, pause, exit): ')
match valor:
    case 'start':
        print('Iniciando el sistema...')
    case 'stop':
        print('Deteniendo el sistema...')
    case 'pause':
        print('Pausando el sistema...')
    case 'exit':
        print('Saliendo del programa...')
    case _:
        print('Comando no reconocido')