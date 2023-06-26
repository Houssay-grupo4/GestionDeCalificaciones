from Matriz_Notas import Matriz_Notas

class Profesor:

    
    def inicioSesion_profesor(self, apellido_profesor):
        # asignacion de issue
        print("")
        materias = {
            "NARCISO PÉREZ": {
                1: "Elementos de Matemáticas y Lógica",
                2: "Sistemas y Organizaciones"
            },
            "PABLO GIRIBALDI": {
                1: "Programación 1",
                2: "Base de Datos"
            },
            "ANTONIO SCIANGULA": {
                1: "Competencias Comunicacionales"
            },
            "DAVID": {
                1: "Aproximación al Mundo del Trabajo"
            }
        }

        if apellido_profesor in materias:
            print("Seleccione una de las siguientes materias:")
            for opcion, materia in materias[apellido_profesor].items():
                print(f"{opcion}. {materia}")
            opcion_materia = int(input("Ingrese la opción seleccionada: "))
            if opcion_materia in materias[apellido_profesor]:
                return materias[apellido_profesor][opcion_materia]

        return None


    def menu_opciones_profesor(self, nombre):
        volver_al_menu = True
        matrices = {}

        while volver_al_menu:
            materia = self.inicioSesion_profesor(nombre)
            if materia is None:
                volver_al_menu = False
                continue

            matriz_notas = matrices.get(materia)
            opcion = 0

            while opcion not in [1, 2, 3, 4, 5]:
                print(f"\n**************** {materia} ****************")
                print("Seleccione una de las siguientes opciones:")
                print("1. Ingresar alumnos y sus respectivas notas")
                print("2. Buscar Alumno")
                print("3. Editar Alumno")
                print("4. Ver todas las notas")
                print("5. Seleccionar otra materia")

                opcion = int(input("Ingrese el número de opción seleccionada: "))

                if opcion == 1:
                    print(f"\n****************************** {materia} *******************************")
                    print("\n**************** INGRESAR ALUMNOS Y SUS RESPECTIVAS NOTAS ****************")
                    if matriz_notas is None:
                        num_alumnos = int(input("\nIngrese la cantidad de alumnos: "))
                        num_notas = int(input("Ingrese la cantidad de notas del año: "))

                        matriz_notas = Matriz_Notas(materia, num_alumnos, num_notas)
                        matrices[materia] = matriz_notas

                    matriz_notas.ingresar_nombres()
                    matriz_notas.generar_notas_aleatorias()
                    matriz_notas.calcular_promedio()
                    matriz_notas.obtener_condicion()

                    print("\n>>>>>>>>>>>> ¡ALUMNOS Y NOTAS GUARDADOS CON ÉXITO! <<<<<<<<<<<<<")
                    opcion = 0

                elif opcion == 2:
                    print(f"\n***************** {materia} ****************")
                    print("\n**************** BUSCAR ALUMNO ****************")
                    nombre_alumno_buscar = input("\nIngrese el nombre del alumno a buscar: ")
                    matriz_notas.buscar_alumno(nombre_alumno_buscar)
                    opcion = 0

                elif opcion == 3:
                    print(f"\n**************** {materia} ****************")
                    print("\n**************** EDITAR ALUMNO ****************")
                    nombre_alumno_editar = input("\nIngrese el nombre del alumno a editar: ")
                    matriz_notas.editar_datos_alumno(nombre_alumno_editar)
                    opcion = 0

                elif opcion == 4:
                    print("\n**************** MOSTRAR TABLA DE ALUMNOS ****************")
                    if matriz_notas is not None:
                        matriz_notas.imprimir_matriz(materia)
                    else:
                        print("\nNo se ha ingresado alumnos y notas para esta materia aún.")
                    opcion = 0

                elif opcion == 5:
                    opcion = 0  # Reiniciar la opción para mostrar el menú de selección de materia nuevamente
                    break  # Salir del bucle actual y regresar al menú de selección de materia

            respuesta = input("\n¿Desea volver al menú principal? (s/n): ")
            if respuesta.lower() != "s":
                volver_al_menu = False

