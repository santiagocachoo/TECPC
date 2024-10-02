numero = int(input("Introduzca un numero entero: "))

if numero == 0:
    print("El numero es par positivo")
elif numero > 0:
    if numero % 2 == 0:
        print("El numero es par positivo")
    else:
        print("El número es impar positivo")
else:
    if numero % 2 == 0:
        print("El numero es par negativo")
    else:
        print("El numero es impar negativo")