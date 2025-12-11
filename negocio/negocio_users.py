from prettytable import PrettyTable
import requests
from servicios import get_users_api, post_user_api, put_user_api, delete_user_api
from modelos import User
from datos import insertar_objeto, obtener_listado_objetos, obtener_user_name
from negocio import crear_geolocalizacion, crear_direccion, crear_compania


def obtener_users_api():
    users = get_users_api()
    if users:
        for user in users:
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

            crear_usuario_db(
                user['name'],
                user['username'],
                user['email'],
                user['phone'],
                user['website'],
                id_direccion,
                id_compania
            )
    else:
        print(
            f"Problemas al procesar su solicitud...")


def crear_user_api():
    name = input('Ingrese su nombre: ')
    username = input('Ingrese nombre usuario: ')
    email = input('Ingrese correo: ')
    phone = input('Ingrese celular: ')
    website = input('Ingrese página web: ')
    user = {
        'name': name,
        'username': username,
        'email': email,
        'phone': phone,
        'website': website
    }
    post_user_api(user)


def modificar_user_api(url):
    id_user = input('Ingrese ID usuario: ')
    try:
        id_user = int(id_user)
    except:
        print('Ingrese un número entero...')
    name = input('Ingrese su nombre: ')
    username = input('Ingrese nombre usuario: ')
    email = input('Ingrese correo: ')
    phone = input('Ingrese celular: ')
    website = input('Ingrese página web: ')
    user = {
        'name': name,
        'username': username,
        'email': email,
        'phone': phone,
        'website': website
    }
    put_user_api(id_user, user)


def eliminar_user_api(url):
    id_user = input('Ingrese ID usuario: ')
    try:
        id_user = int(id_user)
    except:
        print('Ingrese un número entero...')
    delete_user_api(id_user)


def buscar_user_name_db(nombre):
    if nombre != '':
        user = obtener_user_name(nombre)
        if user != None:
            return user


def listado_usuarios_db():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = [
        'N°', 'Nombre', 'Usuario', 'Correo', 'Teléfono', 'Sitio Web']
    listado_usuarios = obtener_listado_objetos(User)

    if listado_usuarios:
        for usuario in listado_usuarios:
            tabla_usuarios.add_row(
                [usuario.id, usuario.name, usuario.username, usuario.email, usuario.phone, usuario.website])
        print(tabla_usuarios)


def crear_usuario_db(nombre, nombre_usuario, correo, telefono, sitio_web, id_direccion, id_compania):
    user = buscar_user_name_db(nombre)
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
