roles = ['profesor', 'preceptor', 'alumno', 'directivo', 'administrador']


print('Seleccione el rol que cumple dentro del instituto :')
print()
for i, rol in enumerate(roles):
    print(f'{i + 1}. {rol}')
print()
opcion_rol = int(input('Ingrese el número de opción seleccionada: '))
rol_elegido = roles[opcion_rol - 1]

nombre = input('Ingrese su nombre: ')
contraseña = input('Ingrese su contraseña: ')


usuarios = {
    'NARCISO PÉREZ': '1111',
    'PABLO GIRIBALDI': '2222',
    'ANTONIO SCIANGULA': '3333',
    'DAVID': '4444'
}


if nombre in usuarios and usuarios[nombre] == contraseña:
    print(f'Bienvenido {nombre} como {rol_elegido}')

  
    profesor = Profesor()
    profesor.menu_opciones_profesor(nombre)
else:
    print('Nombre de usuario o contraseña incorrectos')





#profesor = Profesor()
#profesor.menu_opciones_profesor("PABLO GIRIBALDI")