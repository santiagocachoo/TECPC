mis_mascotas = ['Dorito', 'Mac']

nombre = input('Ingresa un nombre de mascota: ').capitalize()
if nombre not in mis_mascotas:
    print(f'No tengo una mascota llamada {nombre}')
else:
    print(f'{nombre} es mi mascota')