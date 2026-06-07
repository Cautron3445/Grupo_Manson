#Laboratorio 1 Ejercicio 1
#Erick Torres
#Grupo_Manson

Voltaje = float(input("Ingrese valor del Voltaje en voltios = "))
Corriente = float(input("Ingrese valor de la Corriente en amperios = "))

Resistencia = Voltaje/Corriente
Potencia_Disipada = Voltaje*Corriente

print("La Resistencia es = ",Resistencia,"[Ohm]")
print("La Potencia Disipada es = ",Potencia_Disipada,"[W]")

if (Potencia_Disipada > 1000):
    print ("¡Peligro! Alta disipacion de potencia detectada")
else:
    print ("operacion en rangos seguros")
