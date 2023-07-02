class Directivo:
    def __init__(self):
        self.nombre = ""
        self.contraseña = ""

    def menu_opciones_directivo(self):
        print("\nSUS OPCIONES COMO DIRECTIVO SON:")
        print("1. Acceder como PROFESOR")
        print("2. Acceder como ALUMNO")
        print("3. Acceder como PRECEPTOR")
        print("4. Salir")

        opcion = int(input("Ingrese el número de opción seleccionada: "))

        if opcion == 1:
            import Usuario_Profesor
            profesor = Usuario_Profesor.Profesor()
            profesor.menu_opciones_profesor()
            
                
        elif opcion == 2:
            import Usuario_Alumno
            alumno = Usuario_Alumno.Alumno()
            alumno.menu_opciones_alumno()
                
        elif opcion == 3:
            import Usuario_Preceptor
            preceptor = Usuario_Preceptor.Preceptor()
            preceptor.menu_opciones_preceptor()
                
        elif opcion == 4:
            print("Saliendo...")
            
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            self.menu_opciones_directivo()









