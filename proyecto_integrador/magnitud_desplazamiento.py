import math as m

def magnitud_desplazamiento(pix, pfx, piy, pfy):                    # toma punto inicial y punto final de x y y
    desplazamiento_x = pfx - pix                                    # calcula desplazamiento de x
    desplazamiento_y = pfy - piy                                    # calcula desplazamiento de y
    magnitud = m.sqrt(desplazamiento_x**2 + desplazamiento_y**2)    # calcula magnitud con teorema de pitagoras
    return magnitud                                                 # devuelve magnitud