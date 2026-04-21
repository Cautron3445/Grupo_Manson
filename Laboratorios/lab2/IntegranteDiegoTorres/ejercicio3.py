configuracion_robot = {
"velocidad": 50 ,
"torque_max": 120 ,
"herramienta": "pinza"
}

def calibrar_robot(*args, **kwargs):
    
    desplazamiento_total = sum(args)
    articulaciones_en_movimiento = len(args)

    for key, value in kwargs.items():
        if key == "torque_max" and value > 100:
        
            print("peligro de sobrecarga")

        else:
            print(f"{key}: {value}")

    return desplazamiento_total, articulaciones_en_movimiento

desplazamiento, articulaciones = calibrar_robot(10, 20, 15)
print("------Resultados de la calibración del robot-------")
print(f"Desplazamiento total: {desplazamiento} unidades")
print(f"Articulaciones en movimiento: {articulaciones}")

calibrar_robot(velocidad=50, torque_max=120, herramienta="pinza")
