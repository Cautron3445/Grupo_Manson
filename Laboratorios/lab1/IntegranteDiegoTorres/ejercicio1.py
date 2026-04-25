voltaje = float(input("ingrese el valor del voltaje: "))  
corriente = float(input("ingrese el valor de la corriente: "))  
resistencia = voltaje / corriente
print("El valor de la resistencia es:", resistencia, "Ohms")
potencia = voltaje * corriente
print("El valor de la potencia es:", potencia, "Watts")
if potencia > 1000:
    print("¡Peligro! Alta disipación de potencia detectada.")
else:
    print("Operacion en rangos seguros.")