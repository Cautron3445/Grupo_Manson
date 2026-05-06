
def calibrar_robot(*angulos_prueba, **configuracion_robot):
    
    desplazamiento_total = sum(angulos_prueba)
    articulaciones_en_movimiento = len(angulos_prueba)

    print("------Configuración del robot-------")
    for key, value in configuracion_robot.items():
        if key == "torque_max" and value > 100:
        
            print("peligro de sobrecarga torque_max excede el límite seguro (torque_max > 100)")

        else:
            print(f"{key}: {value}")

    return desplazamiento_total, articulaciones_en_movimiento

desplazamiento, articulaciones = calibrar_robot(45, 90, -30, 15, velocidad=50, torque_max=120, herramienta="pinza")
print("------calibración del robot-------")
print(f"Desplazamiento total: {desplazamiento} unidades")
print(f"Articulaciones en movimiento: {articulaciones}")


