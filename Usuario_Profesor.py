from notas_diccionario import materias

class Profesor:
    def __init__(self):
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def verificar_materias(self):
        return self.materias

    def ver_notas(self, materia):
        if materia in self.materias:
            for alumno in materias[materia]:
                nombre = list(alumno.keys())[0]
                notas = alumno["notas"]
                promedio = sum(notas) / len(notas)
                print(f"Alumno: {nombre}")
                print(f"Notas: {notas}")
                print(f"Promedio: {promedio}")
                print()
        else:
            print("No tienes acceso a esta materia.")

    def modificar_nota(self, materia, alumno, nueva_nota):
        if materia in self.materias:
            for i, alumno_info in enumerate(materias[materia]):
                if alumno_info[list(alumno_info.keys())[0]] == alumno:
                    alumno_info["notas"] = nueva_nota
                    print("Nota modificada con éxito.")
                    break
            else:
                print("El alumno no se encuentra en la lista.")
        else:
            print("No tienes acceso a esta materia.")

    def agregar_nota(self, materia, alumno, nueva_nota):
        if materia in self.materias:
            for alumno_info in materias[materia]:
                if alumno_info[list(alumno_info.keys())[0]] == alumno:
                    alumno_info["notas"].append(nueva_nota)
                    print("Nota agregada con éxito.")
                    break
            else:
                print("El alumno no se encuentra en la lista.")
        else:
            print("No tienes acceso a esta materia.")

    def agregar_alumno(self, materia, alumno, notas):
        if materia in self.materias:
            nuevo_alumno = {alumno: "Alumno " + str(len(materias[materia])+1), "notas": notas}
            materias[materia].append(nuevo_alumno)
            print("Alumno agregado con éxito.")
        else:
            print("No tienes acceso a esta materia.")

    def ingresar_nombre(self):
        nombre = input("Ingrese su nombre como profesor: ")
        self.materias = profesores.get(nombre.lower(), [])

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
                notas = []
                while True:
                    nota = input("Ingrese una nota (ingrese 'fin' para finalizar): ")
                    if nota.lower() == "fin":
                        break
                    notas.append(float(nota))
                self.agregar_alumno(materia_seleccionada, alumno, notas)
            elif opcion == 5:
                continue
            elif opcion == 6:
                print("Saliendo del programa...")
                return
            else:
                print("Opción inválida.")

# Diccionario de profesores y sus materias
profesores = {
    "pablo giribaldi": ["Programación I", "Base de Datos"],
    "narciso pérez": ["Sistemas y Organizaciones", "Elementos de Matemática y Lógica"],
    "david": ["Aproximación al Mundo del Trabajo"],
    "antonio sciangula": ["Competencias Comunicacionales I"]
}








