catNames = []
while True:
    print('Ingresa el nombre del gato ' + str(len(catNames) + 1) + 
          ' (ingresa "ALTO" para detenerte):')
    name = input()
    if name == 'ALTO':
        break
    catNames = catNames + [name]

if len(catNames) == 0:
    pass
else:
    print('Los nombres de los gatos son:')
    for name in catNames:
        print('  ' + name)
        
