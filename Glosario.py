import os

# Archivos de texto para cada letra del alfabeto
def crear_archivos():
    for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        with open(f"{letra}.txt", "a") as archivo:
            pass 

# Leer las palabras y las descripciones del archivo para devolverlas como una lista de tuplas
def leer_palabras(nombre_archivo):
    palabras = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                if linea.strip():  # Asegurarse de no leer líneas vacías
                    palabra, descripcion = linea.strip().split(": ", 1)
                    palabras.append((palabra, descripcion))
    return palabras

# Escribir las palabras y descripciones en el archivo correspondiente
def escribir_palabras(nombre_archivo, palabras):
    with open(nombre_archivo, "w") as archivo:
        for palabra, descripcion in palabras:
            archivo.write(f"{palabra}: {descripcion}\n")

# Guardar cada palabra con su respectiva descripción
def guardar_palabra_descripcion():
    palabra = input("Ingresa una palabra: ")
    descripcion = input(f"Ingresa la descripción de {palabra}: ")
    letra_inicial = palabra[0].upper()
    nombre_archivo = f"{letra_inicial}.txt"

    # Leer palabras existentes, agregar la nueva palabra y ordenar
    palabras = leer_palabras(nombre_archivo)
    palabras.append((palabra, descripcion))
    palabras.sort(key=lambda tupla: tupla[0])

    # Escribir todas las palabras ordenadas en el archivo
    escribir_palabras(nombre_archivo, palabras)

# Funcionalidad para agregar una palabra al glosario
def agregar_palabra(palabra, descripcion):
    letra_inicial = palabra[0].upper()
    nombre_archivo = f"{letra_inicial}.txt"

    # Leer palabras existentes, agregar la nueva palabra y ordenar
    palabras = leer_palabras(nombre_archivo)
    palabras.append((palabra, descripcion))
    palabras.sort(key=lambda tupla: tupla[0])

    # Escribir todas las palabras ordenadas en el archivo
    escribir_palabras(nombre_archivo, palabras)

# Funcionalidad para ver las palabras del archivo
def ver_palabras(letra):
    nombre_archivo = f"{letra}.txt"
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            return archivo.read()
    else:
        return "El archivo del glosario no existe."

# Menú principal
def menu():
    crear_archivos()  # Asegurarse de que los archivos existen al iniciar el programa
    while True:
        print("\nMenú del Glosario")
        print("1. Agregar una palabra")
        print("2. Ver palabras de un archivo")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            guardar_palabra_descripcion()
        elif opcion == "2":
            letra = input("Ingresa la letra para ver palabras: ").upper()
            print(f"\nContenido de {letra}.txt:")
            print(ver_palabras(letra))
        elif opcion == "3":
            break
        else:
            print("Opción no válida, por favor elige opcion de nuevo.")

# Ejemplo de uso
menu()
