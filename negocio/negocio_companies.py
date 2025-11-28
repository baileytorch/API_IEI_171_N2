from modelos import Company
from datos import insertar_objeto, obtener_company_name


def crear_compania(nombre, slogan, negocio):
    compania = Company(
        name=nombre,
        catchPhrase=slogan,
        bs=negocio
    )
    cia = buscar_compania_nombre(nombre)
    if not cia:
        try:
            id_compania = insertar_objeto(compania)
            return id_compania
        except Exception as error:
            print(f'Error al guardar la geolocalización: {error}')
    else:
        print('Compañía ya existe, no será agregada.')


def buscar_compania_nombre(nombre):
    if nombre != '':
        compania = obtener_company_name(nombre)
        if compania != None:
            return compania
