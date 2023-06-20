import Usuario_Profesor

roles = ['PROFESOR', 'PRECEPTOR', 'ALUMNO', 'DIRECTIVO', 'ADMINISTRADOR']

usuarios = {
    'NARCISO PÉREZ': '1111',
    'PABLO GIRIBALDI': '2222',
    'ANTONIO SCIANGULA': '3333',
    'DAVID': '4444'
}

opcion_rol = 0
nombre = ""
contraseña = ""

print('\nSeleccione el rol que cumple dentro del instituto:')
print()
for i, rol in enumerate(roles):
        print(f'{i + 1}. {rol}')
        print()
opcion_rol = int(input('Ingrese el número de opción seleccionada: '))
rol_elegido = roles[opcion_rol - 1]

while opcion_rol not in range(1, len(roles) + 1) or nombre not in usuarios or usuarios[nombre] != contraseña:


    nombre = input('\nIngrese su nombre: ').upper()
    contraseña = input('Ingrese su contraseña: ')

    if nombre in usuarios and usuarios[nombre] == contraseña:
        break
    else:
        print('Nombre de usuario o contraseña incorrectos')

if nombre in usuarios and usuarios[nombre] == contraseña:
    print(f'\n******************* BIENVENIDO {nombre} COMO {rol_elegido}*******************')
    profesor = Usuario_Profesor.Profesor()
    profesor.menu_opciones_profesor(nombre)