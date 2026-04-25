red_esp8266 = {
"Nodo_Tanque": {"ip": "192.168.1.10", "estado": "activo", "salida_dac": 3000},
"Nodo_Motor": {"ip": "192.168.1.11", "estado": "falla", "salida_dac": 0},
"Nodo_Valvula": {"ip": "192.168.1.12", "estado": "inactivo", "salida_dac": 150},
"Nodo_Caldera": {"ip": "192.168.1.13", "estado": "activo", "salida_dac": 4000}
}

def auditar_red(nodos):
    cantidad_nodos = len(nodos)
    lista_fallas= []
    lista_inactivos = []
    activos = 0
    suma_salida_dac = 0

    for nodo, info in nodos.items():
        if info["estado"] == "falla":
            lista_fallas.append(info["ip"])
        elif info["estado"] == "inactivo":
            lista_inactivos.append(info["ip"])
        elif info["estado"] == "activo":
            suma_salida_dac += info["salida_dac"]
            activos += 1

    if activos > 0:
        prom_salida_dac = suma_salida_dac / activos
    else:
        prom_salida_dac = 0


    

    
    return cantidad_nodos, lista_fallas, lista_inactivos, prom_salida_dac


total, fallas, inactivos, promedio = auditar_red(red_esp8266)

print("------Auditoría de la Red--------")
print(f"Cantidad de nodos en la red: {total}")
print(f"Nodos en falla: {fallas}")
print(f"Nodos inactivos: {inactivos}")
print(f"Promedio de salida DAC: {promedio}")