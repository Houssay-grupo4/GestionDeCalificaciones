import random

class Matriz_Notas:
    def __init__(self, materia, num_alumnos, num_notas):
        self.materia = materia
        self.num_alumnos = num_alumnos
        self.num_notas = num_notas
        self.alumnos = []
        self.matriz = [[0] * num_notas for _ in range(num_alumnos)]
        self.columna_promedio = [0] * num_alumnos
        self.columna_condicion = [""] * num_alumnos

    def ingresar_nombres(self):
        for i in range(self.num_alumnos):
            nombre = input(f"\nIngrese el nombre del alumno N° {i + 1}: ")
            self.alumnos.append(nombre)

    def ingresar_nota(self, alumno, nota, valor):
        if alumno < 1 or alumno > self.num_alumnos:
            print(f"El número de alumno debe estar entre 1 y {self.num_alumnos}")
            return
        if nota < 1 or nota > self.num_notas:
            print(f"El número de nota debe estar entre 1 y {self.num_notas}")
            return
        self.matriz[alumno - 1][nota - 1] = valor

    def generar_notas_aleatorias(self):
        for i in range(self.num_alumnos):
            for j in range(self.num_notas):
                nota = random.uniform(0, 10)  # Generar nota aleatoria en el rango de 0 a 10
                self.matriz[i][j] = nota

    def calcular_promedio(self):
        for i in range(self.num_alumnos):
            suma = sum(self.matriz[i])
            promedio = suma / self.num_notas
            self.columna_promedio[i] = promedio

    def obtener_condicion(self):
        for i in range(self.num_alumnos):
            if self.columna_promedio[i] < 4.00:
                self.columna_condicion[i] = "Libre"
            elif self.columna_promedio[i] >= 4.00 and self.columna_promedio[i] <= 6.00:
                self.columna_condicion[i] = "Regular"
            else:
                self.columna_condicion[i] = "Promoción"

    def imprimir_matriz(self, materia):
        print(f"\n********************************* {materia} *********************************")
        print("   \t", end="")
        for i in range(self.num_notas):
            print(f"       Nota {i + 1}\t", end="")
        print("     Promedio \t       Condición  ")
        for i in range(self.num_alumnos):
            print(f"{self.alumnos[i]:<8}\t", end="")
            for j in range(self.num_notas):
                print(f"{self.matriz[i][j]:<10.2f}\t", end="")
            print(f"{self.columna_promedio[i]:<10.2f}\t{self.columna_condicion[i]:<10}")

    def buscar_alumno(self, nombre_alumno):
        encontrado = False
        for i in range(self.num_alumnos):
           if self.alumnos[i] == nombre_alumno:
              encontrado = True
              notas = self.matriz[i]
              promedio = self.columna_promedio[i]
              condicion = self.columna_condicion[i]
              print(f"\nNotas de {nombre_alumno}:\t")
              print("{:<8s}".format(""), end="")  # Espacio en blanco para la primera columna
              for j in range(self.num_notas):
                  print("\tNota {:d}".format(j + 1), end="\t")
              print("\tPromedio\tCondición")
              print("{:<8s}".format(nombre_alumno), end="\t")
              for nota in notas:
                  print("{:<10.2f}".format(nota), end="\t")
              print("{:<10.2f}\t{:<10}".format(promedio, condicion))
              break

           if not encontrado:
              print(f"No se encontró al alumno {nombre_alumno}.")

    def editar_datos_alumno(self, nombre_alumno):
         encontrado = False
         for i in range(self.num_alumnos):
             if self.alumnos[i] == nombre_alumno:
                 encontrado = True
                 print(f"\nEditando datos de {nombre_alumno}:")
                 opcion = input("\n¿Qué deseas editar?\n1. Nombre del alumno\n2. Nota\n3. Ambos\nIngrese el número de opción: ")

                 if opcion == "1" or opcion == "3":
                     nuevo_nombre = input("\nIngrese el nuevo nombre del alumno: ")
                     self.alumnos[i] = nuevo_nombre

                 if opcion == "2" or opcion == "3":
                     print(f"\nNotas de {nombre_alumno}:")
                     for j, nota in enumerate(self.matriz[i]):
                         print(f"{j + 1}. Nota {j + 1}: {nota}")
                
                     num_nota = int(input("\nIngrese el número de la nota a editar: "))
                     if num_nota < 1 or num_nota > self.num_notas:
                         print(f"El número de nota debe estar entre 1 y {self.num_notas}")
                     else:
                         nuevo_valor = float(input("Ingrese el nuevo valor de la nota: "))
                         self.matriz[i][num_nota - 1] = nuevo_valor
                         
                 print("\n¡Cambios guardado con éxito!")

                 break

         if not encontrado:
             print(f"No se encontró al alumno {nombre_alumno}.")

    



# Ejemplo de uso:
# materia = input("Ingrese la materia:")
# num_alumnos = int(input("Ingrese la cantidad de alumnos: "))
# num_notas = int(input("Ingrese la cantidad de notas del año: "))

# matriz_notas = Matriz_Notas(materia, num_alumnos, num_notas)
# matriz_notas.ingresar_nombres()

# matriz_notas.imprimir_matriz(materia)

# nombre_alumno_buscar = input("\nIngrese el nombre del alumno a buscar: ")
# matriz_notas.buscar_alumno(nombre_alumno_buscar)

# nombre_alumno_editar = input("\nIngrese el nombre del alumno a editar: ")
# matriz_notas.editar_datos_alumno(nombre_alumno_editar)