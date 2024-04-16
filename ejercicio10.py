frase = input("Ingrese una frase: ")

vocales = "aeiou"
consonantes = ""

for caracter in frase:
    if caracter in vocales:
        vocales += caracter
    elif caracter.isalpha():
        consonantes += caracter

cantidad_vocales = len(vocales)
cantidad_consonantes = len(consonantes)

porcentaje_vocales = (cantidad_vocales / (cantidad_vocales + cantidad_consonantes)) * 100
porcentaje_consonantes = (cantidad_consonantes / (cantidad_vocales + cantidad_consonantes)) * 100

print("vocales :", cantidad_vocales, "(", f"{porcentaje_vocales:.2f}%", ")")
print("consonantes: ", cantidad_consonantes, "(", f"{porcentaje_consonantes:.2f}%", ")")
