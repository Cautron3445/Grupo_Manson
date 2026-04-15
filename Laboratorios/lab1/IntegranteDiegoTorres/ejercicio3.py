while True:
    print("----menu de conversion de unidades----")
    print("1. Convertir de miliamperios (mA) a amperios (A)")
    print("2. Convertir de microfaradios (µF) a faradios (F)")
    print("3. Convertir de kiloOhmios (kΩ) a Ohmios (Ω)")
    print("4. Salir")

    opcion = int(input("Seleccione una opción (1-4): "))

    if opcion == 1:
        miliamperios = float(input("Ingrese el valor en miliamperios (mA): "))
        amperios = miliamperios / 1000
        print(f"{miliamperios} mA es igual a {amperios} A.")
    elif opcion == 2:
        microfaradios = float(input("Ingrese el valor en microfaradios (µF): "))
        faradios = microfaradios / 1000000
        print(f"{microfaradios} µF es igual a {faradios} F.")
    elif opcion == 3:
        kiloohmios = float(input("Ingrese el valor en kiloOhmios (kΩ): "))
        ohmios = kiloohmios * 1000
        print(f"{kiloohmios} kΩ es igual a {ohmios} Ω.")
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")