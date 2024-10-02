def equivalente(horas, minutos, segundos):
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos

def AreaRectangulo(base, altura):
    return base * altura

def PerimetroRectangulo(base, altura):
    return 2*(base + altura)

def main():
    print(AreaRectangulo(1, 1))
    print(PerimetroRectangulo(1, 1))

