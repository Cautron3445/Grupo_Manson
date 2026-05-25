import numpy as np


def comparar_rendimiento(datos: list) -> dict:
    """Calcula consumo, basura recolectada y eficiencia para cada robot.

    Cada fila de ``datos`` tiene el formato:
    [paso, nombre, x, y, bateria, basura_recolectada]
    """
    matriz_datos = np.array(datos, dtype=object)
    nombres_robots = np.unique(matriz_datos[:, 1])
    resultados = {}

    for nombre in nombres_robots:
        # La máscara selecciona solamente las filas correspondientes al robot actual.
        mascara_robot = matriz_datos[:, 1] == nombre
        datos_robot = matriz_datos[mascara_robot]

        bateria = datos_robot[:, 4].astype(float)
        basura = datos_robot[:, 5].astype(float)

        consumo_bateria = 100.0 - bateria[-1]
        basura_total = basura[-1]

        if consumo_bateria == 0:
            eficiencia = 0.0
        else:
            eficiencia = basura_total / consumo_bateria

        resultados[nombre] = {
            "consumo_bateria": float(consumo_bateria),
            "basura_total": float(basura_total),
            "eficiencia": float(eficiencia),
        }

    return resultados

