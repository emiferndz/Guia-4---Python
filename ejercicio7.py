while True:
    try:
        a = float(input("Ingrese el coeficiente a: "))
        b = float(input("Ingrese el coeficiente b: "))
        c = float(input("Ingrese el coeficiente c: "))
    except ValueError:
        print("Debe ingresar números validos")
        continue

    discriminante = b**2 - 4 * a * c

    if discriminante < 0:
        print("La ecuaciom no tiene soluciones reales")
        break

    x1 = (-b + (discriminante ** 0.5)) / (2 * a)
    x2 = (-b - (discriminante ** 0.5)) / (2 * a)

    print("raiz 1: ", x1)
    print("raiz 2: ", x2)
    break
