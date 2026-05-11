import random 
import time
import numpy as np  

lista_clasica = [random.random() for _ in range(5000000)]
lista_numpy = np.array(lista_clasica)

inicio_clasica = time.time()
cuadrados_clasica = [x**2 for x in lista_clasica]
fin_clasica = time.time()
tiempo_clasica = fin_clasica - inicio_clasica   

inicio_numpy = time.time()
cuadrados_numpy = lista_numpy ** 2  
fin_numpy = time.time()
tiempo_numpy = fin_numpy - inicio_numpy

print(f"Tiempo clásico Python puro: {tiempo_clasica:.2f} segundos")
print(f"Tiempo NumPy: {tiempo_numpy:.2f} segundos")
if tiempo_numpy > 0:
    print(f"NumPy es {tiempo_clasica / tiempo_numpy:.2f} veces más rápido que el método clásico.")
else:
    print("NumPy es extremadamente rápido (tiempo medido como 0), no se puede calcular la relación de velocidad.")

