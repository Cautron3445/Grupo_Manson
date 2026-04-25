# Tarea 1 - Sistema de Analisis Robotico

Proyecto para la Tarea 1 de Programacion 2 (EIE 434), basado en un sistema de analisis para un robot limpiaplayas. El archivo `main.py` funciona como punto de entrada y orquesta el flujo general, mientras que la logica del proyecto se separa en paquetes y modulos especializados.

## Modularidad en Python

Un modulo en Python es un archivo `.py` que agrupa funciones, clases o variables relacionadas con una responsabilidad concreta. Por ejemplo, `robot_data.py` concentra la carga de datos y la generacion de senales simuladas.

Un paquete es una carpeta que agrupa modulos relacionados. Para que Python la reconozca como paquete importable, la carpeta incluye un archivo `__init__.py`. En este proyecto se usan paquetes para separar datos, procesamiento y visualizacion.

La ventaja de esta arquitectura es que el codigo queda mas ordenado, facil de probar y facil de mantener. `main.py` no calcula directamente las metricas ni dibuja los graficos: solamente llama funciones definidas en otros modulos.

## Estructura del Proyecto

```text
tarea1_robot_beach/
|-- main.py
|-- README.md
|-- data/
|   |-- __init__.py
|   `-- robot_data.py
|-- processing/
|   |-- __init__.py
|   |-- cinematica.py
|   `-- metricas.py
|-- visualization/
|   |-- __init__.py
|   `-- graficos.py
`-- resultados_graficos/
```

## Responsabilidad de Cada Paquete

`data/`

Contiene funciones relacionadas con datos de entrada y senales simuladas. Aqui se debe implementar la carga de experimentos del paper, la generacion de trayectorias ideales y la simulacion del sensor LiDAR.

`processing/`

Contiene la logica matematica del sistema. En este paquete se deben implementar las metricas de error y el modelo cinematico del robot.

`visualization/`

Contiene funciones para crear y guardar graficos con Matplotlib. Todas las figuras generadas deben guardarse en la carpeta `resultados_graficos/`.

`resultados_graficos/`

Carpeta de salida para los archivos `.png` generados por las funciones de visualizacion.

## Dependencias

El proyecto usa Python 3 y las siguientes librerias:

- `numpy`
- `matplotlib`

Instalacion recomendada:

```bash
pip install numpy matplotlib
```

## Ejecucion

Desde la carpeta principal del proyecto:

```bash
python main.py
```

El archivo `main.py` debe importar funciones desde los paquetes `data`, `processing` y `visualization`. La logica debe permanecer dentro de esos modulos, no directamente en `main.py`.
