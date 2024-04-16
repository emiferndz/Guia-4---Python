frase = input("Ingrese una frase: ")
cantidad_palabras = 1

for caracter in frase:
    if caracter == " ":
        cantidad_palabras += 1

print("La frase contiene", cantidad_palabras, "palabras.")
