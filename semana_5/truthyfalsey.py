def contador(limite):
    contador = 1
    while contador <= limite:
        print(contador)
        contador += 1
    return None

def main():
    lim = int(input('Introduzca hasta que numero contar: '))
    contador(lim)
    return None

main()
