#Laboratorio 1 Ejercicio 4
#Erick Torres
#Grupo_Manson

while True:
    lectura = float(input("Ingrese una lectura de temperatura en [°C] ="))

    if 20<=lectura<=45:
        print("Estado normal")
    
    elif 45<=lectura<=75:
        print("Advertencia: Encendiendo ventiladaores auxiliares")

    elif lectura>75:
        print("¡Peligro Critico! Apagando servidor de emergencia")
        break

