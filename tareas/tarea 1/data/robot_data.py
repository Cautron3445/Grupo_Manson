"""Funciones de datos y simulacion sensorial del robot limpiaplayas."""

import numpy as np


def cargar_experimentos():
    """Retornar los datos de las Tablas 6, 7 y 8 del paper."""
    experimentos = {
        # Tabla 6: indices de desempeno para ruta simple.
        "exp1": {
            "politica": "PPO",
            "ambiente": "real",
            "ruta": "simple",
            "ISE": 434.99,
            "IAE": 135.93,
            "ITSE": 6932.79,
            "ITAE": 2601.61,
            "tiempo_s": None,
            "pasos": None,
            "reward_medio": None,
        },
        "exp2": {
            "politica": "PPO-Mask",
            "ambiente": "real",
            "ruta": "simple",
            "ISE": 362.85,
            "IAE": 128.92,
            "ITSE": 5869.30,
            "ITAE": 2669.86,
            "tiempo_s": None,
            "pasos": None,
            "reward_medio": None,
        },
        "exp3": {
            "politica": "PPO",
            "ambiente": "simulado",
            "ruta": "simple",
            "ISE": 73.35,
            "IAE": 24.51,
            "ITSE": 203.90,
            "ITAE": 89.73,
            "tiempo_s": None,
            "pasos": None,
            "reward_medio": None,
        },
        "exp4": {
            "politica": "PPO-Mask",
            "ambiente": "simulado",
            "ruta": "simple",
            "ISE": 73.79,
            "IAE": 22.91,
            "ITSE": 200.16,
            "ITAE": 73.77,
            "tiempo_s": None,
            "pasos": None,
            "reward_medio": None,
        },
        # Tabla 7: desempeno en ruta cuadrada.
        "exp5": {
            "politica": "PPO",
            "ambiente": "simulado",
            "ruta": "cuadrado",
            "ISE": None,
            "IAE": None,
            "ITSE": None,
            "ITAE": None,
            "tiempo_s": 27.89,
            "pasos": 270,
            "reward_medio": 7.12,
        },
        "exp6": {
            "politica": "PPO",
            "ambiente": "real",
            "ruta": "cuadrado",
            "ISE": None,
            "IAE": None,
            "ITSE": None,
            "ITAE": None,
            "tiempo_s": 112.48,
            "pasos": 594,
            "reward_medio": 3.75,
        },
        "exp7": {
            "politica": "PPO-Mask",
            "ambiente": "simulado",
            "ruta": "cuadrado",
            "ISE": None,
            "IAE": None,
            "ITSE": None,
            "ITAE": None,
            "tiempo_s": 24.42,
            "pasos": 235,
            "reward_medio": 7.94,
        },
        "exp8": {
            "politica": "PPO-Mask",
            "ambiente": "real",
            "ruta": "cuadrado",
            "ISE": None,
            "IAE": None,
            "ITSE": None,
            "ITAE": None,
            "tiempo_s": 103.46,
            "pasos": 569,
            "reward_medio": 4.13,
        },
        # Tabla 8: desempeno en ruta triangular.
        "exp9": {
            "politica": "PPO",
            "ambiente": "simulado",
            "ruta": "triangulo",
            "ISE": None,
            "IAE": None,
            "ITSE": None,
            "ITAE": None,
            "tiempo_s": 26.20,
            "pasos": 254,
            "reward_medio": 7.38,
        },
        "exp10": {
            "politica": "PPO",
            "ambiente": "real",
            "ruta": "triangulo",
            "ISE": None,
            "IAE": None,
            "ITSE": None,
            "ITAE": None,
            "tiempo_s": 104.37,
            "pasos": 581,
            "reward_medio": 3.92,
        },
        "exp11": {
            "politica": "PPO-Mask",
            "ambiente": "simulado",
            "ruta": "triangulo",
            "ISE": None,
            "IAE": None,
            "ITSE": None,
            "ITAE": None,
            "tiempo_s": 22.75,
            "pasos": 219,
            "reward_medio": 8.25,
        },
        "exp12": {
            "politica": "PPO-Mask",
            "ambiente": "real",
            "ruta": "triangulo",
            "ISE": None,
            "IAE": None,
            "ITSE": None,
            "ITAE": None,
            "tiempo_s": 116.71,
            "pasos": 638,
            "reward_medio": 4.45,
        },
    }

    return experimentos


def generar_trayectoria_ideal(waypoints, puntos_por_segmento=100):
    """Generar una trayectoria ideal a partir de una lista de waypoints."""
    x_ideal = []
    y_ideal = []

    for i in range(len(waypoints) - 1):
        x_inicio, y_inicio = waypoints[i]
        x_fin, y_fin = waypoints[i + 1]

        x_segmento = np.linspace(x_inicio, x_fin, puntos_por_segmento)
        y_segmento = np.linspace(y_inicio, y_fin, puntos_por_segmento)

        x_ideal.extend(x_segmento)
        y_ideal.extend(y_segmento)

    return np.array(x_ideal), np.array(y_ideal)


def simular_lidar(n_sectores=36, d_min=0.5, d_max=30.0):
    """Simular una lectura de LiDAR 2D con un obstaculo cercano."""
    angulos_deg = np.linspace(0, 360, n_sectores)
    distancias = np.random.uniform(d_min, d_max, n_sectores)

    distancias[5:9] = np.random.uniform(0.5, 2.0, len(distancias[5:9]))
    distancias_norm = (distancias - d_min) / (d_max - d_min)

    return angulos_deg, distancias, distancias_norm
