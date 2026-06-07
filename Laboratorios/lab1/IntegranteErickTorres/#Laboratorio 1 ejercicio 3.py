#Laboratorio 1 Ejercicio 3
#Erick Torres
#Grupo_Manson

print("Menu de conversion de unidades")
print("1: Convertir miliamperios (mA) a amperios (A)")
print("2: Convertir microfaradios (uF) a faradios (F)")
print("3: Convertir kiloohmios (kOhm) a ohmios (Ohm)")
print("4: Salir")

eleccion = int(input("Eliga una opcion del 1 al 4 ="))

if eleccion == 1
    mA = float(input("Ingrese el valor en mA = "))
    print(mA,"[mA] equivalen a ",mA/1000,"[A]")

elif eleccion == 2 
    uF = float(input("Ingrese el valor en uF = "))
    print(uF,"[uF] equivalen a ",uF/1000000,"[F]")

elif eleccion == 3
    kOhm = float(input("Ingrese el valor en kOhm = "))
    print(kOhm,"[kOHM] equivalen a ",kOhm*1000,"[Ohm]")

elif eleccion == 4
    print("Hasta luego")
    break

else:
    print("Eliga una opcion valida")