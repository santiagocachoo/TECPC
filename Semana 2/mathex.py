import math as m

numero = float(input('Ingrese un numero con decimal: '))

truncado = m.trunc(numero)
print(f'\nTruncado de {numero}: ', truncado)

redondeado = round(numero)
print(f'\nRedondeado de {numero}: ', redondeado)

techo = m.ceil(numero)
print(f'\nCeil de {numero}: ', techo)

suelo = m.floor(numero)
print(f'\nFloor de {numero}: ', suelo)

absoluto = m.fabs(-numero)
print(f'\nValor absoluto de {numero}: ', absoluto)