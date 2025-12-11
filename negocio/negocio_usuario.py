import bcrypt
import getpass
from modelos import Usuario
from datos import insertar_objeto, obtener_usuario_nombre


def registrar_usuario():
    ingreso_nombre = input('Ingrese Nombre Completo: ')
    ingreso_nombre_usuario = input('Ingrese Nombre Usuario: ')
    ingreso_email = input('Ingrese Correo Electrónico: ')
    ingreso_contrasena = getpass.getpass('Ingrese Contraseña: ')

    if ingreso_nombre != '' and ingreso_nombre_usuario != '' and ingreso_email != '' and ingreso_contrasena != '':
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(ingreso_contrasena.encode('utf-8'), salt)
        nuevo_usuario = Usuario(
            nombre=ingreso_nombre,
            usuario=ingreso_nombre_usuario,
            email=ingreso_email,
            contrasena_hash=hashed,
            contrasena_salt=salt)

        try:
            id_usuario = insertar_objeto(nuevo_usuario)
            return id_usuario
        except Exception as error:
            print(f'Error al guardar al usuario: {error}')


def iniciar_sesion():
    while True:
        ingreso_nombre_usuario = input('Ingrese Nombre Usuario: ')
        ingreso_contrasena = getpass.getpass('Ingrese Contraseña: ')

        usuario = obtener_usuario_nombre(ingreso_nombre_usuario)
        if usuario:
            if bcrypt.checkpw(ingreso_contrasena.encode('utf-8'), usuario.contrasena_hash.encode('utf-8')):
                print('Acceso Concedido!')
                return True
            else:
                print('Contraseña Incorrecta, Intente nuevamente.')
                return False
        else:
            print('Usuario NO encontrado, regístrese para ingresar.')
