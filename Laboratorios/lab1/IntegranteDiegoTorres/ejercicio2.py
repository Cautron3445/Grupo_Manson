voltaje_inicial = float(input("Ingrese el valor del voltaje inicial (en volts): "))
voltaje_minimo = float(input("Ingrese el valor del voltaje mínimo (en volts) de operacion: "))
horas = 0
while voltaje_inicial > voltaje_minimo:
    voltaje_inicial = voltaje_inicial * 0.97
    horas += 1
print("El banco de baterias logro entregar energia durante ", horas, "horas.")