"""Metricas de evaluacion del controlador."""

import numpy as np


def calcular_IAE(errores, dt):
    """Calcular Integral Absolute Error."""
    errores = np.array(errores)
    return float(np.sum(np.abs(errores)) * dt)


def calcular_ISE(errores, dt):
    """Calcular Integral Square Error."""
    errores = np.array(errores)
    return float(np.sum(errores**2) * dt)


def calcular_ITAE(errores, dt):
    """Calcular Integral Time Absolute Error."""
    errores = np.array(errores)
    tiempo = np.arange(len(errores)) * dt
    return float(np.sum(tiempo * np.abs(errores)) * dt)


def calcular_ITSE(errores, dt):
    """Calcular Integral Time Square Error."""
    errores = np.array(errores)
    tiempo = np.arange(len(errores)) * dt
    return float(np.sum(tiempo * errores**2) * dt)


def calcular_todas_las_metricas(errores, dt):
    """Calcular ISE, IAE, ITSE e ITAE en un diccionario."""
    return {
        "ISE": round(calcular_ISE(errores, dt), 2),
        "IAE": round(calcular_IAE(errores, dt), 2),
        "ITSE": round(calcular_ITSE(errores, dt), 2),
        "ITAE": round(calcular_ITAE(errores, dt), 2),
    }


def calcular_mejora(valor_ppo, valor_mask):
    """Calcular la mejora porcentual de PPO-Mask respecto de PPO."""
    return float(((valor_ppo - valor_mask) / valor_ppo) * 100)
