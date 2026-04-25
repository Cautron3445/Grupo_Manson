# =============================================================================
# main.py - Tarea 1 Programacion 2 (PUCV)
# Integracion de modulos de robotica e IA: "Robot Limpiaplayas"
# =============================================================================

import numpy as np

from data.robot_data import (
    cargar_experimentos,
    generar_trayectoria_ideal,
    simular_lidar,
)
from processing.cinematica import (
    calcular_error_seguimiento,
    calcular_movimiento,
    distancia_al_objetivo,
)
from processing.metricas import calcular_todas_las_metricas
from visualization.graficos import plot_lidar, plot_metricas, plot_trayectorias


def main():
    print("--- INICIANDO SISTEMA DE EVALUACION: PLAYABOT 2026 ---")

    # Paso 1: cargar los datos base del paper.
    datos_paper = cargar_experimentos()

    # Paso 2: validar el modelo cinematico del robot.
    print("\n[VALIDACION] Verificando modelo fisico del robot...")
    x_test, y_test, th_test = 0.0, 0.0, 0.0
    v_test, w_test = 0.5, 0.1

    x_nuevo, y_nuevo, th_nuevo = calcular_movimiento(
        x_test, y_test, th_test, v_test, w_test
    )
    distancia_meta = distancia_al_objetivo(
        x_nuevo, y_nuevo, x_meta=1.0, y_meta=1.0
    )

    print(
        " > Pose inicial: (0,0,0) -> "
        f"Nueva pose: ({x_nuevo:.2f}, {y_nuevo:.2f}, {th_nuevo:.2f} rad)"
    )
    print(f" > Distancia restante al objetivo (1,1): {distancia_meta:.2f} m")

    # Paso 3: generar la lectura simulada del sensor LiDAR.
    print("\n[SENSOR] Generando lectura de 36 sectores...")
    angulos, dist_reales, dist_norm = simular_lidar(n_sectores=36)
    plot_lidar(angulos, dist_reales, dist_norm)

    # Paso 4: evaluar el seguimiento de trayectorias.
    print("\n[NAVEGACION] Evaluando seguimiento de rutas...")

    ruta_triangular = [[0, 0], [4, 0], [2, 4], [0, 0]]
    x_id_tri, y_id_tri = generar_trayectoria_ideal(ruta_triangular)

    x_ppo_tri = x_id_tri + np.random.normal(0, 0.12, len(x_id_tri))
    y_ppo_tri = y_id_tri + np.random.normal(0, 0.12, len(y_id_tri))
    x_mask_tri = x_id_tri + np.random.normal(0, 0.04, len(x_id_tri))
    y_mask_tri = y_id_tri + np.random.normal(0, 0.04, len(y_id_tri))

    plot_trayectorias(
        x_ppo_tri,
        y_ppo_tri,
        x_mask_tri,
        y_mask_tri,
        ruta_triangular,
        "triangulo",
    )

    ruta_cuadrada = [[0, 0], [4, 0], [4, 4], [0, 4], [0, 0]]
    x_id_cuad, y_id_cuad = generar_trayectoria_ideal(ruta_cuadrada)

    x_ppo_cuad = x_id_cuad + np.random.normal(0, 0.15, len(x_id_cuad))
    y_ppo_cuad = y_id_cuad + np.random.normal(0, 0.15, len(y_id_cuad))
    x_mask_cuad = x_id_cuad + np.random.normal(0, 0.05, len(x_id_cuad))
    y_mask_cuad = y_id_cuad + np.random.normal(0, 0.05, len(y_id_cuad))

    plot_trayectorias(
        x_ppo_cuad,
        y_ppo_cuad,
        x_mask_cuad,
        y_mask_cuad,
        ruta_cuadrada,
        "cuadrado",
    )

    # Paso 5: calcular metricas de error sobre la ruta cuadrada.
    errores_cuad_ppo = calcular_error_seguimiento(
        x_ppo_cuad, y_ppo_cuad, x_id_cuad, y_id_cuad
    )
    metricas_cuadrado = calcular_todas_las_metricas(errores_cuad_ppo, dt=0.1)

    print("\n[METRICAS] Resultados PPO en ruta cuadrada:")
    for nombre_metrica, valor_metrica in metricas_cuadrado.items():
        print(f" > {nombre_metrica}: {valor_metrica}")

    # Paso 6: graficar la comparativa historica del paper.
    plot_metricas(datos_paper, ambiente="real", ruta="simple")

    print("\n--- PROCESO FINALIZADO ---")
    print("Revise la carpeta 'resultados_graficos' para ver los reportes visuales.")


if __name__ == "__main__":
    main()
