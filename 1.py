#Busqueda secuencial

lista = [1001322, 1001323, 1001324, 1001325]
def pedirCedula(lista):
        num = int(input('Por favor ingrese su cédula: '))
        return num
def busquedaCedulas(lista, num):
    for i in range(0, len(lista)):
        if num == lista[i]:
            return True
    return False

while True:
    num = pedirCedula(lista)
    encontrado = busquedaCedulas(lista,num)
    if encontrado == True:
        print("Usted puede votar")
        break
    else:
        print("Usted no puede votar")

