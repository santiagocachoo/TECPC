"""
iteracion = 0
while True:
    print(f'hola {iteracion}')
    iteracion += 1
    if iteracion > 10:
       break



while True:
    print('escribe tu nombre')
    name = input()
    if name == 'Santiago':
        break
print('gracias')

while True:
    print('quien eres')

"""

while True:
    print('quien eres')
    name = input()
    if name != 'Joe':
        continue
    print('hola joe, contraseña porfavor')
    password = input()
    if password == 'swordfish':
        break
print('acceso concedido')