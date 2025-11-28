from datos.conexion import sesion
from sqlalchemy import func
from modelos import Company, User


def obtener_listado_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if len(listado_objetos) > 0:
        return listado_objetos


def obtener_user_name(valor):
    user_identificado = sesion.query(User).filter(
        User.name.like(f'%{valor}%')).first()
    if user_identificado != None and isinstance(user_identificado, User):
        return user_identificado


def obtener_company_name(valor):
    company_identificada = sesion.query(Company).filter(
        Company.name.like(f'%{valor}%')).first()
    if company_identificada != None and isinstance(company_identificada, Company):
        return company_identificada
