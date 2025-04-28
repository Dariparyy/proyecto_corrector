import os

# Creo un diccionario donde se almacenarán los alumnos y sus examenes.
alumnos = {}

# Creo la función para limpiar pantalla.
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Creo el bucle principal del menú.
while True:
    limpiar()  # Limpio pantalla antes de mostrar el menú.
    print ("===== SISTEMA DE NOTAS =====")
    print ("1. Añadir alumno y examen")
    print ("2. Introducir respuestas del alumno")
    print ("3. Ver nota del alumno")
    print ("4. Salir")

    opcion = input("\nElige una opción: ").strip()
    limpiar()

    if opcion == "1":
        print ("=== AÑADIR ALUMNO Y EXAMEN ===")
        nombre = input("Nombre del alumno: ").strip().title()
        if nombre in alumnos:
            print ("⚠️ El alumno ya existe.")
            input("\nPresiona Enter para continuar...")
            continue

        try:
            num_preguntas = int(input("Número de preguntas: "))
        except ValueError:
            print ("⚠️ Error: Introduce un número válido.")
            input("\nPresiona Enter para continuar...")
            continue

        respuestas_correctas = [input(f"Respuesta correcta {i+1}: ").strip().lower() for i in range(num_preguntas)]
        alumnos[nombre] = {"correctas": respuestas_correctas, "respuestas": None}

        print("\n✅ Examen guardado correctamente.")
        input("\nPresiona Enter para continuar...")

    elif opcion == "2":
        print("=== INTRODUCIR RESPUESTAS DEL ALUMNO ===")
        nombre = input("Nombre del alumno: ").strip().title()
        if nombre not in alumnos:
            print("⚠️ El alumno no existe.")
            input("\nPresiona Enter para continuar...")
            continue

        num_preguntas = len(alumnos[nombre]["correctas"])
        if alumnos[nombre]["respuestas"] is not None:
            confirmar = input("⚠️ El alumno ya tiene respuestas guardadas. ¿Deseas sobrescribirlas? (s/n): ").strip().lower()
            if confirmar != 's':
                continue

        respuestas = [input(f"Respuesta {i+1}: ").strip().lower() for i in range(num_preguntas)]
        alumnos[nombre]["respuestas"] = respuestas

        print("\n✅ Respuestas guardadas correctamente.")
        input("\nPresiona Enter para continuar...")

    elif opcion == "3":
        print("=== VER NOTA DEL ALUMNO ===")
        nombre = input("Nombre del alumno: ").strip().title()
        if nombre not in alumnos or not alumnos[nombre]["respuestas"]:
            print("⚠️ No hay respuestas registradas para este alumno.")
            input("\nPresiona Enter para continuar...")
            continue

        correctas = alumnos[nombre]["correctas"]
        respuestas = alumnos[nombre]["respuestas"]
        aciertos = sum(1 for i in range(len(correctas)) if respuestas[i] == correctas[i])
        nota = aciertos / len(correctas) * 10

        limpiar()
        print(f"=== NOTA DE {nombre.upper()} ===")
        print(f"📌 Nota final: {nota:.2f}/10\n")
        print("📋 Detalle de respuestas:")

        for i in range(len(correctas)):
            resultado = "✔️" if respuestas[i] == correctas[i] else "❌"
            print(f"Pregunta {i+1}: {resultado}")
            print(f"   - Respuesta dada: {respuestas[i]}")
            print(f"   - Respuesta correcta: {correctas[i]}\n")

        input("Presiona Enter para continuar...")

    elif opcion == "4":
        print("👋 Saliendo del programa...")
        break

    else:
        print("⚠️ Opción no válida. Por favor, elige entre 1, 2, 3 o 4.")
        input("\nPresiona Enter para continuar...")