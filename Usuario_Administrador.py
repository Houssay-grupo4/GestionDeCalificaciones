
import sys 
class Administrador:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def menu_opciones_administrador(self):
        while True:
            print("\n***** Sus opciones como Administrador son *****")
            print("1. Ingresar al sistema")
            print("2. Salir del sistema")
            opcion = input("Ingrese el número de opción: ")

            if opcion == "1":
                #self.ingresar_al_sistema()
                print("EL SISTEMA ACTUALMENTE SE ENCUENTRA EN USO, INTENTE INGRESAR MAS TARDE ")
                sys.exit()
            elif opcion == "2":
                print("Saliendo del sistema...")
                sys.exit()
            else:
                print("Opción inválida. Por favor, ingrese nuevamente.")

    def ingresar_al_sistema(self):
        usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")

        if usuario in usuarios and usuarios[usuario] == contraseña:
            print(f"Bienvenido {usuario} al sistema.")
        else:
            print("Nombre de usuario o contraseña incorrectos.")

usuarios = {
    'CHIARA SECO': '2222',
    'PAZ SANTANGELO': '3333',
    'ALEJANDRO SANTANGELO': '4444',
}

administrador = Administrador("admin", "admin123")
administrador.menu_opciones_administrador()