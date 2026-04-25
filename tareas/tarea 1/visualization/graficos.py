"""Funciones de generacion de graficos del sistema robotico."""

import os

import matplotlib.pyplot as plt
import numpy as np


CARPETA_RESULTADOS = "resultados_graficos"


def _preparar_salida(nombre_archivo):
    """Crear la carpeta de resultados y retornar una ruta segura."""
    os.makedirs(CARPETA_RESULTADOS, exist_ok=True)
    return os.path.join(CARPETA_RESULTADOS, nombre_archivo)


def plot_metricas(diccionario_experimentos, ambiente, ruta):
    """Graficar comparacion de metricas entre politicas."""
    metricas = ["ISE", "IAE", "ITSE", "ITAE"]
    filtrados = [
        datos
        for _, datos in diccionario_experimentos.items()
        if datos["ambiente"] == ambiente and datos["ruta"] == ruta
    ]

    politicas = [datos["politica"] for datos in filtrados]

    plt.figure(figsize=(14, 4))

    for i, metrica in enumerate(metricas, start=1):
        valores = [datos[metrica] for datos in filtrados]

        plt.subplot(1, 4, i)
        plt.bar(politicas, valores, color=["#3b82f6", "#10b981"])
        plt.title(metrica)
        plt.ylabel("Valor")
        plt.grid(axis="y", alpha=0.3)

    plt.suptitle(f"Metricas - ambiente {ambiente}, ruta {ruta}")
    plt.tight_layout()

    ruta_salida = _preparar_salida(f"metricas_{ambiente}_{ruta}.png")
    plt.savefig(ruta_salida, dpi=300)
    plt.close()


def plot_lidar(angulos, distancias, distancias_norm):
    """Graficar lecturas LiDAR reales y normalizadas."""
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(angulos, distancias, color="#ef4444")
    plt.title("LiDAR - distancias reales")
    plt.xlabel("Angulo [grados]")
    plt.ylabel("Distancia [m]")
    plt.grid(alpha=0.3)

    plt.subplot(1, 2, 2)
    plt.plot(angulos, distancias_norm, color="#2563eb", marker="o", markersize=3)
    plt.title("LiDAR - distancias normalizadas")
    plt.xlabel("Angulo [grados]")
    plt.ylabel("Distancia normalizada")
    plt.ylim(0, 1)
    plt.grid(alpha=0.3)

    plt.tight_layout()

    ruta_salida = _preparar_salida("mapa_lidar.png")
    plt.savefig(ruta_salida, dpi=300)
    plt.close()


def plot_trayectorias(x_ppo, y_ppo, x_mask, y_mask, waypoints, nombre):
    """Graficar trayectorias PPO y PPO-Mask junto con los waypoints."""
    waypoints = np.array(waypoints)

    plt.figure(figsize=(7, 6))
    plt.plot(x_ppo, y_ppo, label="PPO", color="#f97316", linewidth=2)
    plt.plot(x_mask, y_mask, label="PPO-Mask", color="#0ea5e9", linewidth=2)
    plt.scatter(
        waypoints[:, 0],
        waypoints[:, 1],
        marker="s",
        color="black",
        label="Waypoints",
        zorder=3,
    )

    plt.title(f"Trayectorias - ruta {nombre}")
    plt.xlabel("Posicion X [m]")
    plt.ylabel("Posicion Y [m]")
    plt.axis("equal")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()

    ruta_salida = _preparar_salida(f"trayectorias_{nombre}.png")
    plt.savefig(ruta_salida, dpi=300)
    plt.close()
