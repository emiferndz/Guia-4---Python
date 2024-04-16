while True:
    correo_electronico = input("Ingrese su dirección de correo electronico: ")

    if len(correo_electronico) > 255:
        print("La dirección de correo electrónico no debe superar los 255 caracteres")
        continue

    if "@" not in correo_electronico:
        print("La dirección de correo electrónico debe contener un carácter '@'")
        continue

    for caracter in correo_electronico:
        if not caracter.isalnum() and not caracter in "_@.-":
            print("La dirección de correo electrónico solo puede contener letras, numeros, guiones bajos, puntos ('.') y arrobas ('@')")
            continue

    print("Correo electrónico valido: ", correo_electronico)
    break
