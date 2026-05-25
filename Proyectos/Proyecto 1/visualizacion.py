import matplotlib.pyplot as plt
import numpy as np


def graficar_recoleccion_vs_bateria(resultados: dict):
    """Genera un gráfico de barras agrupadas del rendimiento de cada robot."""
    nombres_robots = list(resultados.keys())
    basura_total = [resultados[nombre]["basura_total"] for nombre in nombres_robots]
    consumo_bateria = [
        resultados[nombre]["consumo_bateria"] for nombre in nombres_robots
    ]

    x = np.arange(len(nombres_robots))
    ancho = 0.35

    plt.figure(figsize=(9, 5))
    plt.bar(
        x - ancho / 2,
        basura_total,
        width=ancho,
        color="green",
        label="Basura Recolectada (kg)",
    )
    plt.bar(
        x + ancho / 2,
        consumo_bateria,
        width=ancho,
        color="red",
        label="Batería Consumida (%)",
    )

    plt.title("Rendimiento: Recolección vs Consumo Energético")
    plt.ylabel("Cantidad")
    plt.xticks(x, nombres_robots)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()
