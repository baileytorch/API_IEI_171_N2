from prettytable import PrettyTable
import requests
import json
from modelos import User
from datos import insertar_objeto, obtener_listado_objetos, obtener_user_name
from negocio import crear_geolocalizacion, crear_direccion, crear_compania


def obtener_data_usuarios(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data Users...")
        usuarios = respuesta.json()
        for user in usuarios:
            id_geo = crear_geolocalizacion(
                user['address']['geo']['lat'],
                user['address']['geo']['lng']
            )

            id_direccion = crear_direccion(
                user['address']['street'],
                user['address']['suite'],
                user['address']['city'],
                user['address']['zipcode'],
                id_geo
            )

            id_compania = crear_compania(
                user['company']['name'],
                user['company']['catchPhrase'],
                user['company']['bs']
            )

            crear_usuario(
                user['name'],
                user['username'],
                user['email'],
                user['phone'],
                user['website'],
                id_direccion,
                id_compania
            )

    elif respuesta.status_code == 204:
        print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")


def buscar_user_name(nombre):
    if nombre != '':
        user = obtener_user_name(nombre)
        if user != None:
            return user


def listado_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = [
        'N°', 'Nombre', 'Usuario', 'Correo', 'Teléfono', 'Sitio Web']
    listado_usuarios = obtener_listado_objetos(User)

    if listado_usuarios:
        for usuario in listado_usuarios:
            tabla_usuarios.add_row(
                [usuario.id, usuario.name, usuario.username, usuario.email, usuario.phone, usuario.website])
        print(tabla_usuarios)


def crear_usuario(nombre, nombre_usuario, correo, telefono, sitio_web, id_direccion, id_compania):
    user = buscar_user_name(nombre)
    if not user:
        usuario = User(
            name=nombre,
            username=nombre_usuario,
            email=correo,
            phone=telefono,
            website=sitio_web,
            addressId=id_direccion,
            companyId=id_compania
        )
        try:
            id_usuario = insertar_objeto(usuario)
            return id_usuario
        except Exception as error:
            print(f'Error al guardar al usuario: {error}')
    else:
        print('Usuario ya existe, no será agregado.')
