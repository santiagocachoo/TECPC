def usd_a_eur(usd):
    return usd * 0.9

def eur_a_usd(eur):
    return eur * 1-10

def usd_a_mxn(usd):
    return usd * 20

def mxn_a_usd(mxn):
    return mxn * 0.05

def eur_a_mxn(eur):
    return eur * 22

def mxn_a_eur(mxn):
    return mxn * 0.04

def main():
    dinero = float(input('Ingrese la cantidad de dinero: '))
    moneda_og = input('Ingrese el tipo de moneda actual (usd, eur, mxn): ').lower()
    moneda_nueva = input('Ingrese la moneda a la que quiere convertir (usd, eur, mxn): ').lower()

    if moneda_og == 'usd':
        if moneda_nueva == 'mxn':
            print(f'El equivalente en pesos es de: {usd_a_mxn(dinero)}')
        elif moneda_nueva == 'eur':
            print(f'El equivalente en euros es de: {usd_a_eur(dinero)}')
        else:
            print('Operación invalida')

    elif moneda_og == 'eur':
        if moneda_nueva == 'usd':
            print(f'El equivalente en dolares es de: {eur_a_usd(dinero)}')
        elif moneda_nueva == 'mxn':
            print(f'El equivalente en pesos mexicanos es de: {eur_a_mxn(dinero)}')
        else:
            print('Operación invalida')
    
    elif moneda_og == 'mxn':
        if moneda_nueva == 'usd':
            print(f'El equivalente en dolares es de: {mxn_a_usd(dinero)}')
        elif moneda_nueva == 'eur':
            print(f'El equivalente en euros es de: {mxn_a_eur(dinero)}')

    else:
        print('Operación invalida')

main()