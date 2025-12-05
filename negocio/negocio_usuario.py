import bcrypt
import getpass
from modelos import Usuario
from datos import insertar_objeto


def registrar_usuario():
    ingreso_nombre = input('Ingrese Nombre Completo: ')
    ingreso_nombre_usuario = input('Ingrese Nombre Usuario: ')
    ingreso_email = input('Ingrese Correo Electrónico: ')
    ingreso_contrasena = getpass.getpass('Ingrese Contraseña: ')

    if ingreso_contrasena != '':
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
    ingreso_nombre_usuario = input('Ingrese Nombre Usuario: ')
    ingreso_contrasena = getpass.getpass('Ingrese Contraseña: ')


    if bcrypt.checkpw(passwd, hashed):
        return True
    else:
        return False
