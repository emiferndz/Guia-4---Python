edad = int(input("Ingrese su edad: "))
edad_jubilacion = 65

if edad >= edad_jubilacion:
    print("Esta en edad para jubilarse")
else:
    años_faltantes = edad_jubilacion - edad
    print(f"Le faltan {años_faltantes} años todavia para jubilarse")
