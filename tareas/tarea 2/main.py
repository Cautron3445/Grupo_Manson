"""
Simulador de Selección Campeona del Mundo con POO y Pandas.
Este programa crea una selección de 11 jugadores titulares, demuestra el uso de
herencia, polimorfismo y análisis de datos con Pandas.

Autor: Grupo de Programación 2
EIE 434 – Programación 2 | Escuela de Ingeniería Eléctrica
"""

import pandas as pd
from jugadores import Portero, Defensa, Mediocampista, Delantero
import os


# Selección elegida: España - Candidata a Campeona del Mundo 2026
PAIS_ELEGIDO = "España"

# Creación de los 11 jugadores titulares con la formación requerida
JUGADORES_TITULARES = [
    # 1 Portero
    Portero("Unai Simón", 26, 1.86, 1, atajadas_historicas=180),
    
    # 4 Defensas
    Defensa("Álvaro Odriozola", 28, 1.84, 2, balones_recuperados=450),
    Defensa("Robin Le Normand", 27, 1.87, 3, balones_recuperados=420),
    Defensa("Aymeric Laporte", 29, 1.89, 4, balones_recuperados=550),
    Defensa("José Luis Gayà", 28, 1.81, 5, balones_recuperados=380),
    
    # 4 Mediocampistas
    Mediocampista("Sergio Busquets", 34, 1.83, 6, asistencias=120),
    Mediocampista("Pedri", 21, 1.74, 7, asistencias=85),
    Mediocampista("Gavi", 20, 1.73, 8, asistencias=60),
    Mediocampista("Carlos Soler", 26, 1.82, 9, asistencias=55),
    
    # 2 Delanteros
    Delantero("Álvaro Morata", 31, 1.86, 10, goles_anotados=280),
    Delantero("Ferran Torres", 24, 1.84, 11, goles_anotados=95),
]



def demostrar_acciones():
    """Demuestra el uso de métodos heredados, específicos y polimorfismo."""
    print("=" * 70)
    print("--- SIMULADOR DE CAMPEÓN DEL MUNDO ---")
    print("=" * 70)
    print(f"Selección: {PAIS_ELEGIDO}\n")
    
    print("ACCIONES EN LA CANCHA:")
    print("-" * 70)
    
    # Demostración de métodos heredados y específicos
    for i, jugador in enumerate(JUGADORES_TITULARES, 1):
        print(f"\n{i}. {jugador.nombre}:")
        print(f"   {jugador.correr()}")
        
        # Llamar al método específico según el tipo de jugador
        if isinstance(jugador, Portero):
            print(f"   {jugador.atajar()}")
        elif isinstance(jugador, Defensa):
            print(f"   {jugador.marcar()}")
        elif isinstance(jugador, Mediocampista):
            print(f"   {jugador.dar_pase()}")
        elif isinstance(jugador, Delantero):
            print(f"   {jugador.patear_al_arco()}")
    
    # Polimorfismo: demostración mediante mostrar_rol()
    print("\n\n" + "=" * 70)
    print("ROLES DEL EQUIPO (Polimorfismo):")
    print("-" * 70)
    for jugador in JUGADORES_TITULARES:
        print(jugador.mostrar_rol())


def construir_tabla_datos():
    """Construye un DataFrame de Pandas con la información de los jugadores."""
    datos_jugadores = []
    
    for jugador in JUGADORES_TITULARES:
        # Obtener la posición usando mostrar_rol()
        rol_completo = jugador.mostrar_rol()
        posicion = rol_completo.split(" - ")[1]
        
        # Crear diccionario con los datos del jugador
        datos = {
            "País": PAIS_ELEGIDO,
            "Dorsal": jugador.dorsal,
            "Nombre": jugador.nombre,
            "Edad": jugador.edad,
            "Altura_m": jugador.altura,
            "Posición": posicion,
        }
        
        # Agregar datos específicos según la posición
        if isinstance(jugador, Portero):
            datos["Atajadas"] = jugador.atajadas_historicas
        elif isinstance(jugador, Defensa):
            datos["Balones_recuperados"] = jugador.balones_recuperados
        elif isinstance(jugador, Mediocampista):
            datos["Asistencias"] = jugador.asistencias
        elif isinstance(jugador, Delantero):
            datos["Goles"] = jugador.goles_anotados
        
        datos_jugadores.append(datos)
    
    # Crear DataFrame
    tabla_equipo = pd.DataFrame(datos_jugadores)
    return tabla_equipo


def mostrar_estadisticas(tabla_equipo):
    """Muestra estadísticas básicas y tabla del equipo."""
    print("\n" + "=" * 70)
    print("TABLA DEL EQUIPO TITULAR")
    print("=" * 70)
    print(tabla_equipo.to_string(index=False))
    
    print("\n" + "=" * 70)
    print("ESTADÍSTICAS BÁSICAS DEL EQUIPO")
    print("=" * 70)
    
    # Edad promedio del equipo
    edad_promedio = tabla_equipo["Edad"].mean()
    print(f"\nEdad promedio del equipo: {edad_promedio:.2f} años")
    
    # Altura máxima
    altura_maxima = tabla_equipo["Altura_m"].max()
    jugador_mas_alto = tabla_equipo[tabla_equipo["Altura_m"] == altura_maxima]["Nombre"].values[0]
    print(f"Altura máxima: {altura_maxima} m ({jugador_mas_alto})")
    
    # Cantidad de jugadores por posición
    print("\nJugadores por posición:")
    posiciones_count = tabla_equipo["Posición"].value_counts().sort_index()
    for posicion, cantidad in posiciones_count.items():
        print(f"  {posicion}: {cantidad}")
    
    # Promedio de edad por posición
    print("\nPromedio de edad por posición:")
    edad_por_posicion = tabla_equipo.groupby("Posición")["Edad"].mean().sort_index()
    for posicion, edad in edad_por_posicion.items():
        print(f"  {posicion}: {edad:.2f} años")


def exportar_archivo_csv(tabla_equipo):
    """Exporta la tabla de datos a un archivo CSV."""
    # Crear carpeta output si no existe
    if not os.path.exists("output"):
        os.makedirs("output")
    
    # Nombre del archivo basado en el país elegido
    nombre_archivo = f"output/titulares_{PAIS_ELEGIDO.lower()}.csv"
    tabla_equipo.to_csv(nombre_archivo, index=False, encoding="utf-8")
    print(f"\n✓ Archivo CSV exportado exitosamente: {nombre_archivo}")


def principal():
    """Función principal que ejecuta el simulador de campeón del mundo."""
    # Demostrar métodos, herencia y polimorfismo
    demostrar_acciones()
    
    # Crear tabla de datos con la información de los jugadores
    tabla_equipo = construir_tabla_datos()
    
    # Mostrar tabla y estadísticas
    mostrar_estadisticas(tabla_equipo)
    
    # Exportar a archivo CSV
    exportar_archivo_csv(tabla_equipo)
    

if __name__ == "__main__":
    principal()
