import requests
from auxiliares import url_comments,url_users

def get_comments_api():
    respuesta = requests.get(url_comments)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data...")
        return respuesta.json()
    elif respuesta.status_code == 204:
        print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")

def get_users_api():
    respuesta = requests.get(url_users)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data Users...")
        return respuesta.json()
    elif respuesta.status_code == 204:
        print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")


def post_user_api(json_user):
    respuesta = requests.post(url_users, data=json_user)
    if respuesta.status_code == 201:
        print("Solicitud correcta, User creado...")
        print(respuesta.text)
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")


def put_user_api(id_user, json_user):
    url = f'{url_users}/{id_user}'
    respuesta = requests.put(url, data=json_user)
    if respuesta.status_code == 200:
        print("Solicitud correcta, User modificado...")
        print(respuesta.text)
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")


def delete_user_api(id_user):
    url = f'{url_users}/{id_user}'
    respuesta = requests.delete(url)
    if respuesta.status_code == 200:
        print("Solicitud correcta, User eliminado...")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")
