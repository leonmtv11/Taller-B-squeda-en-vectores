def almacenar_precios():

  precios = {
    "Manzana": 0.50,
    "Pera": 0.75,
    "Naranja": 1.00,
    "Leche": 2.00,
    "Pan": 1.50,
  }

  return precios

def calcular_precio_total(precios, producto, cantidad):

  if producto in precios:
    precio_unidad = precios[producto]
    precio_total = precio_unidad * cantidad
    return f"{cantidad} {producto} cuestan {precio_total:.2f}"
  else:
    return f"Lo siento, no tenemos {producto} en venta."

# Programa principal
precios = almacenar_precios()

producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad del producto: "))

precio_total = calcular_precio_total(precios, producto, cantidad)
print(precio_total)
