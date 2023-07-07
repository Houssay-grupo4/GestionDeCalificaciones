import notas_diccionario

class Profesor:
    def __init__(self):
        self.materias = []

    def verificar_materias(self):
        return self.materias

    def ver_notas(self, materia):
        if materia in self.materias:
            for alumno, info in notas_diccionario.materias[materia].items():
                notas = info.get("notas", [])
                promedio = sum(notas) / len(notas) if notas else 0
                print(f"Alumno: {alumno}")
                print(f"Notas: {notas}")
                print(f"Promedio: {promedio}")
                print()
        else:
            print("No tienes acceso a esta materia.")

    def modificar_nota(self, materia, alumno, nueva_nota):
        if materia in self.materias:
            for materia_info in notas_diccionario.materias[materia]:
                nombre_alumno = list(materia_info.keys())[0]
                if alumno.lower() in nombre_alumno.lower():
                    materia_info[nombre_alumno]["notas"] = [nueva_nota]
                    print("Nota modificada con éxito.")
                    break
            else:
                print("El alumno no se encuentra en la lista.")
        else:
            print("No tienes acceso a esta materia.")

    def agregar_nota(self, materia, alumno, nueva_nota):
        if materia in self.materias:
            materia_info = notas_diccionario.materias[materia]
            for alumno_info in materia_info:
                if alumno_info.lower() == alumno.lower():
                    materia_info[alumno_info]["notas"].append(nueva_nota)
                    print("Nota agregada con éxito.")
                    return
            print("El alumno no se encuentra en la lista.")
        else:
            print("No tienes acceso a esta materia.")

    def agregar_alumno(self, materia, alumno):
        if materia in self.materias:
            if alumno in notas_diccionario.materias[materia]:
                print("El alumno ya existe en la lista.")
            else:
                notas_diccionario.materias[materia][alumno] = {"notas": []}
                print("Alumno agregado con éxito.")
        else:
            print("No tienes acceso a esta materia.")



    def ingresar_nombre(self):
        nombre = input("Ingrese su nombre como profesor: ")
        self.materias = notas_diccionario.profesores.get(nombre.lower(), [])

        if not self.materias:
            print("No se encontraron materias asignadas a este profesor.")
            return False

        return True

    def menu_opciones_profesor(self):
        if not self.ingresar_nombre():
            return

        while True:

            print("\nMaterias disponibles:")
            for i, materia in enumerate(self.materias, start=1):
                print(f"{i}. {materia}")

            opcion_materias = int(input("Selecciona una materia: "))

            if opcion_materias < 1 or opcion_materias > len(self.materias):
                print("Opción inválida.")
                return

            materia_seleccionada = self.materias[opcion_materias - 1]

            print(f"\nOpciones de {materia_seleccionada}:")
            print("1. Ver notas de los alumnos")
            print("2. Modificar nota de un alumno")
            print("3. Agregar nota a un alumno")
            print("4. Agregar nuevo alumno")
            print("5. Cambiar de materia")
            print("6. Salir")

            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                self.ver_notas(materia_seleccionada)
            elif opcion == 2:
                alumno = input("Ingrese el nombre del alumno: ")
                nueva_nota = float(input("Ingrese la nueva nota: "))
                self.modificar_nota(materia_seleccionada, alumno, nueva_nota)
            elif opcion == 3:
                alumno = input("Ingrese el nombre del alumno: ")
                nueva_nota = float(input("Ingrese la nueva nota: "))
                self.agregar_nota(materia_seleccionada, alumno, nueva_nota)
            elif opcion == 4:
                alumno = input("Ingrese el nombre del alumno: ")
                self.agregar_alumno(materia_seleccionada, alumno)
            elif opcion == 5:
                continue
            elif opcion == 6:
                print("Saliendo del programa...")
                return
            else:
                print("Opción inválida.")










