nota = float(input('Ingrese la calificacion: '))
if nota > 100 or nota < 0:
    print('Calificación invalida (Ingrese un numero entre el 0 y 100)')
else:
    if nota >= 90:
        print('Sobresaliente (Calificación: A)')
    elif nota >= 80:
        print('Notable (Calificación: B)')
    elif nota >= 70:
        print('Bien (Calificación: C)')
    elif nota >= 60:
        print('Suficiente (Calificación: D)')
    else:
        print('Insuficiente (Calificación: F)')
