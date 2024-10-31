print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Definimos una lista con las asignaturas del curso
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Inicializamos una lista para almacenar las asignaturas que no se han aprobado
asignaturas_repetir = []

# Iteramos sobre cada asignatura para preguntar la nota al usuario
for asignatura in asignaturas:
    # Pedimos al usuario que ingrese la nota
    # Convertimos la entrada a un número flotante para permitir decimales
    nota = float(input(f"Ingrese la nota que sacaste en {asignatura}: "))
    
    # Verificamos si la nota es menor a 6 (considerando 6 como la nota mínima para aprobar)
    if nota < 6:
        # Si no se aprueba, agregamos la asignatura a la lista de repetir
        asignaturas_repetir.append(asignatura)

# Mostramos las asignaturas que el usuario tiene que repetir
if asignaturas_repetir:
    print("Las asignaturas que tienes que repetir son:")
    for asignatura in asignaturas_repetir:
        print(f"- {asignatura}")
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")
