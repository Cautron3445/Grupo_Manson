"""Modelo cinematico y errores espaciales del robot."""

import numpy as np


def calcular_movimiento(x, y, theta, v, omega, dt=0.1):
    """Calcular la nueva pose del robot diferencial."""
    v = np.clip(v, -0.8, 0.8)
    omega = np.clip(omega, -0.6, 0.6)

    x_nuevo = x + v * np.cos(theta) * dt
    y_nuevo = y + v * np.sin(theta) * dt
    theta_nuevo = theta + omega * dt

    return x_nuevo, y_nuevo, theta_nuevo


def distancia_al_objetivo(x, y, x_meta, y_meta):
    """Calcular la distancia euclidiana entre la pose actual y la meta."""
    return float(np.sqrt((x_meta - x) ** 2 + (y_meta - y) ** 2))


def calcular_error_seguimiento(x_real, y_real, x_ideal, y_ideal):
    """Calcular el error de seguimiento entre trayectoria real e ideal."""
    n_puntos = min(len(x_real), len(y_real), len(x_ideal), len(y_ideal))

    x_real = np.array(x_real[:n_puntos])
    y_real = np.array(y_real[:n_puntos])
    x_ideal = np.array(x_ideal[:n_puntos])
    y_ideal = np.array(y_ideal[:n_puntos])

    return np.sqrt((x_real - x_ideal) ** 2 + (y_real - y_ideal) ** 2)
