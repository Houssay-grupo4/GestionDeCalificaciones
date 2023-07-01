
print("********** BIENVENIDO AL SISTEMA DE GESTION DE ESTUDIANTES **********")
roles = ['PROFESOR', 'PRECEPTOR', 'ALUMNO', 'DIRECTIVO', 'ADMINISTRADOR']

usuarios_Profesor = {
    'NARCISO PÉREZ': '1111',
    'PABLO GIRIBALDI': '2222',
    'ANTONIO SCIANGULA': '3333',
    'DAVID': '4444'
}
usuario_Preceptor = {
    'SABINO': '1111',
    'DAVID': '4444',
}

usuarios_Alumno = {
    'MAYKA RAMIREZ': '1111',
    'CHIARA SECO': '2222',
    'PAZ SANTANGELO':'3333',
    'ALEJANDRO SANTANGELO': '4444',
}
usuario_Directivo ={
    'CRISTINA': '1111',
    'MIRTA' : '2222',
}
usuario_Administrador = {

    'CHIARA SECO': '2222',
    'PAZ SANTANGELO':'3333',
    'ALEJANDRO SANTANGELO': '4444',
}

usuarios = {
    'PROFESOR': usuarios_Profesor,
    'ALUMNO': usuarios_Alumno,
    'PRECEPTOR': usuario_Preceptor,
    'DIRECTIVO' : usuario_Directivo,
    'ADMINISTRADOR' : usuario_Administrador,
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

while opcion_rol not in range(1, len(roles) + 1) or nombre not in usuarios[rol_elegido] or usuarios[rol_elegido][nombre] != contraseña:
    nombre = input('\nIngrese su nombre: ').upper()
    contraseña = input('Ingrese su contraseña: ')

    if nombre in usuarios[rol_elegido] and usuarios[rol_elegido][nombre] == contraseña:
        break
    else:
        print('Nombre de usuario o contraseña incorrectos. Por favor, ingrese nuevamente su usuario y contraseña.')

if nombre in usuarios[rol_elegido] and usuarios[rol_elegido][nombre] == contraseña:
    print(f'\n******************* BIENVENIDO {nombre} COMO {rol_elegido}*******************')
    
    if rol_elegido == 'PRECEPTOR':
        import Usuario_preceptor
        preceptor = Usuario_Preceptor.Preceptor(nombre, contraseña)
        preceptor.menu_opciones_preceptor()
    elif rol_elegido == 'PROFESOR':
        import Usuario_Profesor
        profesor = Usuario_Profesor.Profesor()
        profesor.menu_opciones_profesor()
    elif rol_elegido == 'ALUMNO':
        import Usuario_Alumno
        alumno = Usuario_Alumno.Alumno()
        alumno.menu_opciones_alumno()
        pass
    elif rol_elegido == 'DIRECTIVO':
        import Usuario_Directivo
        directivo = Usuario_Directivo.Directivo()
        directivo.iniciar_sesion()
        directivo.menu_opciones_directivo()
        pass
    elif rol_elegido == 'ADMINISTRADOR':
        import Usuario_Administrador
        administrador = Usuario_Administrador(nombre, contraseña)
        administrador.menu_opciones_administrador()
        pass
        
       