
import sys
from notas_diccionario import materias

class Preceptor:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre = "David"
        self.materias = materias
        self.materia_seleccionada = None
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

    def seleccionar_materia(self):
        print("Seleccione una materia:")
        for opcion, materia in enumerate(self.materias, start=1):
            print(f"{opcion}. {materia}")
        opcion_materia = int(input("Ingrese el número de opción seleccionada: "))

        if opcion_materia in range(1, len(self.materias) + 1):
            self.materia_seleccionada = list(self.materias.keys())[opcion_materia - 1]
            print(f"Ha seleccionado la materia: {self.materia_seleccionada}")
        else:
            print("Opción inválida.")

    def ver_notas(self):
        if self.materia_seleccionada:
            print(f"Notas de la materia: {self.materia_seleccionada}")
            alumnos = self.materias[self.materia_seleccionada]

            for alumno in alumnos:
                nombre = list(alumno.keys())[0]
                notas = alumno["notas"]
                promedio = sum(notas) / len(notas)
                print(f"Alumno: {nombre}")
                print(f"Notas: {notas}")
                print(f"Promedio: {promedio}")
                print()
        else:
            print("No ha seleccionado ninguna materia.")

    def menu_opciones_preceptor(self):
        opcion = 0

        while opcion != 2:
            print("\nSeleccione una opción:")
            print("1. Seleccionar materia y ver notas")
            print("2. Salir")

            opcion = int(input("Ingrese el número de opción seleccionada: "))

            if opcion == 1:
                self.seleccionar_materia()
                self.ver_notas()
            elif opcion == 2:
                print("Saliendo del programa...")
            else:
                print("Opción inválida.")

def inicio_usuario():
    roles = ['PRECEPTOR']

    usuarios_preceptor = {
        'DAVID': '4444',
        'SABINO': '1111',
    }

    nombre = 'DAVID'  # Nombre del usuario validado
    contraseña = usuarios_preceptor[nombre]  # Contraseña correspondiente al usuario

    preceptor = Preceptor(nombre, contraseña)
    preceptor.menu_opciones_preceptor()

inicio_usuario()
