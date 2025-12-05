from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Geo(Base):
    __tablename__ = 'geos'
    __table_args__ = {'comment': 'Geolocalizaciones asociadas a direcciones.'}
    id = Column(Integer, primary_key=True,
                comment='Identificador único tabla geos.')
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    __table_args__ = {
        'comment': 'Direcciones de usuarios, tienen asociada una geolocalización.'}
    id = Column(Integer, primary_key=True,
                comment='Identificador único tabla addresses.')
    street = Column(String(100), nullable=False)
    suite = Column(String(20), nullable=False)
    city = Column(String(50), nullable=False)
    zipcode = Column(String(25), nullable=True)
    geoId = Column(Integer, ForeignKey('geos.id'), nullable=True)


class Company(Base):
    __tablename__ = 'companies'
    __table_args__ = {'comment': 'Compañías asociadas a usuarios.'}
    id = Column(Integer, primary_key=True,
                comment='Identificador único tabla companies.')
    name = Column(String(100), nullable=False)
    catchPhrase = Column(String(255), nullable=True)
    bs = Column(String(255), nullable=True)


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {
        'comment': 'Usuarios, pueden hacer publicaciones una vez registrados.'}
    id = Column(Integer, primary_key=True,
                comment='Identificador único tabla users.')
    name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(25), nullable=True)
    website = Column(String(255), nullable=True)
    addressId = Column(Integer, ForeignKey('addresses.id'), nullable=True)
    companyId = Column(Integer, ForeignKey('companies.id'), nullable=True)


class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = {'comment': 'Publicaciones de usuarios registrados.'}
    id = Column(Integer, primary_key=True,
                comment='Identificador único tabla posts.')
    title = Column(String(200), nullable=False)
    body = Column(String(255), nullable=False)
    userId = Column(Integer, ForeignKey('users.id'), nullable=False)


class Comment(Base):
    __tablename__ = 'comments'
    __table_args__ = {'comment': 'Comentarios asociados a publicaciones.'}
    id = Column(Integer, primary_key=True,
                comment='Identificador único tabla comments.')
    name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    body = Column(String(255), nullable=False)
    postId = Column(Integer, ForeignKey('posts.id'))


class Usuario(Base):
    __tablename__ = 'usuarios'
    __table_args__ = {'comment': 'Usuarios de sistema.'}
    id = Column(
        Integer,
        primary_key=True,
        comment='Identificador único tabla usuarios.')
    nombre = Column(
        String(100),
        nullable=False)
    usuario = Column(
        String(50),
        nullable=False)
    email = Column(
        String(255),
        nullable=False)
    contrasena_hash = Column(
        String(255),
        nullable=False,
        comment='Contraseña + Salt.')
    contrasena_salt = Column(
        String(255),
        nullable=False,
        comment='Salt única de la contraseña.')
