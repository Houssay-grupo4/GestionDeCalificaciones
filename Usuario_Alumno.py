from notas_diccionario import materias

class Alumno:
    def __init__(self):
        self.materias = materias

    def menu_opciones_alumno(self):
        nombre_usuario = input("Ingrese su nombre: ")

        while True:
            print("\nSeleccione una opción:")
            print("1. Seleccionar materia y ver tus notas")
            print("2. Salir")
            opcion = input("Ingrese el número de opción seleccionada: ")

            if opcion == "1":
                print("Materias disponibles:")
                for i, materia in enumerate(self.materias.keys()):
                    print(f"{i+1}. {materia}")
                materia_elegida = input("Ingrese el número de materia seleccionada: ")
                if materia_elegida.isnumeric() and int(materia_elegida) in range(1, len(self.materias)+1):
                    materia_elegida = list(self.materias.keys())[int(materia_elegida)-1]
                    self.verificar_alumno(materia_elegida, nombre_usuario)
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
            elif opcion == "2":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def verificar_alumno(self, materia_elegida, nombre_usuario):
        if nombre_usuario is not None:
            if materia_elegida in self.materias:
                alumnos = self.materias[materia_elegida]
                for alumno in alumnos:
                    if alumno.lower() == nombre_usuario.lower():
                        notas = alumnos[alumno].get("notas")
                        if notas:
                            promedio = sum(notas) / len(notas)
                            print(f"Notas de la materia: {materia_elegida}")
                            print(f"Alumno: {alumno.capitalize()}")
                            print(f"Notas: {notas}")
                            print(f"Promedio: {promedio}")
                            return
                print("El alumno no tiene notas registradas para esta materia.")
            else:
                print("Materia inválida. Por favor, seleccione una materia válida.")
        else:
            print("Nombre de usuario no especificado.")
