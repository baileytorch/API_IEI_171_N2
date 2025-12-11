from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config


DATABASE_URL = f'mysql+mysqlconnector://{config('user')}:{config('password')}@{config('server')}:{config('port')}/{config('database')}'
motor_db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=motor_db)
sesion = Session()
