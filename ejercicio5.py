nombre_anterior = None

while True:
    try:
        nombre = input("Ingrese un nombre ordenado alfabeticamente: ")
        int(nombre)  #Lo convierto a entero para verificar si es un numero
        print("Error: No se permiten numeros, ingrese un nombre valido...")
        continue
    except ValueError:
        pass  #Si no se puede convertir a entero, es un nombre valido

    if nombre.isalpha() and not nombre.isspace():
        if nombre_anterior and nombre < nombre_anterior:
            print("Error: El nombre debe estar ordenado alfabeticamente")
            continue
        nombre_anterior = nombre
        print("Nombre ingresado: ", nombre)

        if nombre_anterior == "Z":
            break 

print("Lista completa")
