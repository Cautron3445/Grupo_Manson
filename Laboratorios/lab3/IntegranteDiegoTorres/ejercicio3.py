import random
import time
import numpy as np

matriz1 = [[random.random() for _ in range(100)] for _ in range(100)]
matriz2 = [[random.random() for _ in range(100)] for _ in range(100)]

matriz1_np = np.array(matriz1)
matriz2_np = np.array(matriz2)

# Multiplicación de matrices clásica en Python puro con 3 ciclos for anidados
resultado_clasico = [[0.0 for _ in range(100)] for _ in range(100)]
start_clasico = time.time()
for i in range(100):
    for j in range(100):
        for k in range(100):
            resultado_clasico[i][j] += matriz1[i][k] * matriz2[k][j]
         
end_clasico = time.time()

tiempo_clasico = end_clasico - start_clasico

# Multiplicación de matrices con NumPy
start_numpy = time.time()
resultado_numpy = matriz1_np @ matriz2_np
end_numpy = time.time()

tiempo_numpy = end_numpy - start_numpy
print(f"Tiempo clásico Python puro: {tiempo_clasico:.2f} segundos")
print(f"Tiempo NumPy: {tiempo_numpy:.2f} segundos")
if tiempo_numpy > 0:
    print(f"NumPy es {tiempo_clasico / tiempo_numpy:.2f} veces más rápido que el método clásico.")
else:
    print("NumPy es extremadamente rápido (tiempo medido como 0), no se puede calcular la relación de velocidad.")



