nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

#Tuve que utilizar (caracter.isalpha()) para poder verificar si los caracteres son letras, y concatené las cadenas de la variable nombre y apellido para tomar todo eso.
while not all(caracter.isalpha() for caracter in nombre + apellido):
  print("Error: El nombre o apellido contiene caracteres no validos")
  nombre = input("Ingrese su nombre: ")
  apellido = input("Ingrese su apellido: ")

print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
