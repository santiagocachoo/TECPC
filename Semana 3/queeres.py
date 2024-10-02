edad = input('Cual es tu edad? ')
edad = int(float(edad))
print(edad)
if edad < 13:
    print('Eres un niño')
elif edad < 18:
    print('Eres un adolescente')
elif edad < 65:
    print('Eres un adulto')
elif edad <= 105:
    print('Eres un adulto mayor')
else:
    print('Estas muerto')
