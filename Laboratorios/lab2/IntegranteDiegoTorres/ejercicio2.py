coords_x = [2, 8, 8, 2]
coords_y = [1, 1, 5, 5]

def evaluar_zona_poligono(x,y):
    (ancho,alto) = (max(coords_x) - min(coords_x), max(coords_y) - min(coords_y))

    area = ancho * alto

    (x_centro,y_centro) = ((max(coords_x) + min(coords_x)) / 2, (max(coords_y) + min(coords_y)) / 2)

    centro_geom = (x_centro, y_centro)

    return (ancho, alto, area, x_centro, y_centro, centro_geom)

(ancho, alto, area, x_centro, y_centro, centro_geom) = evaluar_zona_poligono(coords_x, coords_y)

print("------Resultados del análisis del polígono-----")
print(f"Bounding Box: {ancho} x {alto} unidades")
print(f"Área: {area} unidades cuadradas")
print(f"Centro Geométrico del poligono: {centro_geom}")
