while True:
    try:
        lado_a = float(input("Ingrese el lado a: "))
        lado_b = float(input("Ingrese el lado b: "))
        lado_c = float(input("Ingrese el lado c: "))
    except ValueError:
        print("Error: Debe ingresar numeros validos")
        continue

    if lado_a + lado_b <= lado_c or lado_a + lado_c <= lado_b or lado_b + lado_c <= lado_a:
        print("No son lados validos de un triángulo")
        continue

    perimetro = lado_a + lado_b + lado_c
    area = (lado_a * lado_b) / 2

    print("Perimetro: ", perimetro)
    print("Área: ", area)
    break
