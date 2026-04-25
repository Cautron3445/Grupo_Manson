while True:
    temperatura = int(input("Ingrese la temperatura en grados Celsius (°C): "))

    if temperatura >= 20 and temperatura <= 45:
        print("estado normal")
    elif temperatura > 45 and temperatura <= 75:
        print("Advertencia: encendiendo ventiladores auxiliares")
    elif temperatura > 75:
        print("¡peligro critico! Apagando servidor de emergencia")
        break
    else:
        print("Temperatura fuera del rango de operacion.")