from negocio import registrar_usuario, iniciar_sesion
from interfaces_usuario import menu_inicial

# obtener_data_usuarios_api(url_usuarios)
# listado_usuarios_db()
# crear_user_api(url_usuarios)
# eliminar_user_api(url_usuarios)
# obtener_data_publicaciones(url_publicaciones)
# listado_publicaciones()
# registrar_usuario()


def app():
    while True:
        menu_inicial()

        opcion_inicial = input('Seleccione su opción [0-2]: ')
        if opcion_inicial == '1':
            registrar_usuario()
        elif opcion_inicial == '2':
            inicio_sesion = iniciar_sesion()
            if inicio_sesion == True:
                print('Iniciando Sistema...')
        elif opcion_inicial == '0':
            print('Saliendo...')
            break
        else:
            print('Opción Incorrecta, vuelva a intentar...')


app()
