def almacenar_notas():

  asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
  notas = {}

  for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota en {asignatura}: "))
    notas[asignatura] = nota

  return notas

def mostrar_notas(notas):

  for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")

# Programa principal
notas = almacenar_notas()
mostrar_notas(notas)
