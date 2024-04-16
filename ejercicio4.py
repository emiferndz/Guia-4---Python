numero_anterior = None

while True:
  try:
    numero = int(input("Ingrese un numero entero (que nno se repita): "))
  except ValueError:
    print("Error: Debe ingresar un numero")
    continue

  if numero == numero_anterior:
    print("Error: El numero ya está en la lista, intente de vuelta")
    continue

  numero_anterior = numero
  print("Numero ingresado: ", numero)

  if numero_anterior == 4:
    break  

print("Lista completa, muchas gracias")
