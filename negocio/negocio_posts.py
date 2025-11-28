from prettytable import PrettyTable
from modelos import Post
from datos import insertar_objeto, obtener_listado_objetos
import requests


def obtener_data_publicaciones(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data...")
        publicaciones = respuesta.json()
        for publicacion in publicaciones:
            crear_publicacion(
                publicacion['title'],
                publicacion['body'],
                publicacion['userId']
            )

    elif respuesta.status_code == 204:
        print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")


def listado_publicaciones():
    tabla_publicaciones = PrettyTable()
    tabla_publicaciones.field_names = [
        'N°', 'Título', 'Contenido']
    listado_publicaciones = obtener_listado_objetos(Post)

    if listado_publicaciones:
        for publicacion in listado_publicaciones:
            tabla_publicaciones.add_row(
                [publicacion.id, publicacion.title, publicacion.body])
        print(tabla_publicaciones)


def crear_publicacion(titulo, contenido, id_usuario):
    publicacion = Post(
        title=titulo,
        body=contenido,
        userId=id_usuario
    )
    try:
        id_publicacion = insertar_objeto(publicacion)
        return id_publicacion
    except Exception as error:
        print(f'Error al guardar la geolocalización: {error}')
