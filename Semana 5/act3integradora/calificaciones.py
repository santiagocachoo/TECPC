usuario = 'usuario972'
password = 'pepito'

acceso = False
while not acceso:
    usr_intento = input('Bienvenido al sistema, ingrese su usuario: ')
    if usr_intento == usuario:
        pswrd_intento = input('Ingrese su contraseña: ')
        if pswrd_intento == password:
            acceso = True
            break
        else:
            print('Contraseña incorrecta, intente de nuevo')
    else:
        print('Usuario inexistente. Intente de nuevo.')

if acceso:
    def calif_valida(text, calif_max):
        while True:
            calif = float(input(text))
            if 0 <= calif <= calif_max:
                return calif
            else:
                print(f'Error. La calificación debe de ser entre 0 y {calif_max}. Intentelo de nuevo')


    qz_1 = calif_valida('Introduzca calificación de quizes de la unidad de formación 1 (10%): ', 10)
    tareas_1 = calif_valida('Introduzca calificación de tareas de la unidad de formación 1 (25%): ', 25)
    examen_1 = calif_valida('Introduzca calificación de examen de la unidad de formación 1 (25%): ', 25)
    reto_1 = calif_valida('Introduzca calificación de reto de la unidad de formación 1 (40%): ', 40)
    qz_2 = calif_valida('Introduzca calificación de quizes de la unidad de formación 2 (10%): ', 10)
    tareas_2 = calif_valida('Introduzca calificación de tareas de la unidad de formación 2 (25%): ', 25)
    examen_2 = calif_valida('Introduzca calificación de examen de la unidad de formación 2 (25%): ', 25)
    reto_2 = calif_valida('Introduzca calificación de reto de la unidad de formación 2 (40%): ', 40)
    qz_3 = calif_valida('Introduzca calificación de quizes de la unidad de formación 3 (10%): ', 10)
    tareas_3 = calif_valida('Introduzca calificación de tareas de la unidad de formación 3 (25%): ', 25)
    examen_3 = calif_valida('Introduzca calificación de examen de la unidad de formación 3 (25%): ', 25)
    reto_3 = calif_valida('Introduzca calificación de reto de la unidad de formación 3 (40%): ', 40)

    calificacion_1 = qz_1 + tareas_1 + examen_1 + reto_1
    calificacion_2 = qz_2 + tareas_2 + examen_2 + reto_2
    calificacion_3 = qz_3 + tareas_3 + examen_3 + reto_3
    promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3

    print(f'La calificación de la unidad de formación 1 es: {calificacion_1:.2f}')
    print(f'La calificación de la unidad de formación 2 es: {calificacion_2:.2f}')
    print(f'La calificación de la unidad de formación 3 es: {calificacion_3:.2f}')
    print(f'El promedio del semestre es: {promedio:.2f}')
    
