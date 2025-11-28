from prettytable import PrettyTable
from modelos import Geo
from datos import insertar_objeto, obtener_listado_objetos


def listado_geolocalizaciones():
    tabla_geolocalizaciones = PrettyTable()
    tabla_geolocalizaciones.field_names = [
        'N°', 'Latitud', 'Longitud']
    listado_geolocalizaciones = obtener_listado_objetos(Geo)

    if listado_geolocalizaciones:
        for geolocalizacion in listado_geolocalizaciones:
            tabla_geolocalizaciones.add_row(
                [geolocalizacion.id, geolocalizacion.lat, geolocalizacion.lng])
        print(tabla_geolocalizaciones)


def crear_geolocalizacion(latitud, longitud):
    geo = Geo(
        lat=latitud,
        lng=longitud
    )
    try:
        id_geo = insertar_objeto(geo)
        return id_geo
    except Exception as error:
        print(f'Error al guardar la geolocalización: {error}')
