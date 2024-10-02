total = 0
suma = 0

while True:
    precio = float(input('Ingrese el precio del articulo: '))
    cantidad = float(input('Ingrese la cantidad del articulo: '))
    usr = input('Desea comprar otro articulo (s/n): ').lower()
    suma += cantidad
    total = total + (precio * cantidad)
    if usr == 'n':
        break

print(f'La cantidad de productos es: {suma}')
print(f'El precio a pagar es: {total}')



