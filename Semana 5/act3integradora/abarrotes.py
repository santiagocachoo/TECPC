print('Bienvenido a Abarrotes Lupita!!!')
productos = {
    '100100': ('Torta de Jamón', 45.5),
    '100101': ('Torta de pierna especial', 37.9),
    '100102': ('Taco de canitas', 22.8),
    '100103': ('Taco de asada', 55.45),
    '100104': ('Agua (100ml)', 10),
    '100105': ('Jarra de jamaica (1L)', 124.09),
    '100106': ('Vaso de coca-cola', 15.78),
    '100107': ('Orden de tacos de asada', 123.56),
    '100108': ('Orden de tacos de carnitas', 125.88),
    '100109': ('Orden doble de tacos carnitas con bebidas', 456.78),
    '100110': ('Orden doble tacos de asada con bebidas', 567.67)
}

print('Menu de productos:')
for codigo, (nombre, precio) in productos.items():
    print(f'Codigo: {codigo}, Producto: {nombre}, Precio: {precio}')

precio_final = 0
primera_vez = True

while True:
    if primera_vez:
        usuario = input('Desea agregar algo? S/N: ')
        primera_vez = False
    else:
        usuario = input('Desea agregar algo más? S/N: ')
    
    if usuario == 'S':
        codigo = input('Ingrese el codigo del producto: ')
        if codigo in productos:
            cantidad = int(input('Ingrese la cantidad: '))
            nombre_producto, precio = productos[codigo]
            precio_total = precio * cantidad
            precio_final += precio_total
            print(f'El precio de {nombre_producto} ({cantidad}) sería de {precio_total:.2f}')
        else:
            print('Codigo incorrecto, intente nuevamente')
    elif usuario == 'N':
        print(f'El total de su orden es de {precio_final:.2f} MXN.')
        break
    else:
        print('Por favor, ingrese S o N.')
