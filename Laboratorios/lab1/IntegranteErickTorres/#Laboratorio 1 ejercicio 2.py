#Laboratorio 1 Ejercicio 2
#Erick Torres
#Grupo_Manson

Voltaje = float(input("Ingrese el valor del Voltaje Inicial del banco de baterias en voltios= "))
Voltaje_minimo = float(input("ingrese el valor del Voltaje minimo de operacion en voltios= "))
horas = 0

while Voltaje>Voltaje_minimo 
    Voltaje *=0.97
    horas += 1

print("El banco de baterias entrego energia durante",horas,"horas completas")