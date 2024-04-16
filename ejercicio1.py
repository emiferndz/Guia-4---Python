edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Usted es mayor de edad.")
else:
    if edad < 0:
        print("La edad ingresada es incorrecta")
    else:
        print("Usted es menor de edad")
