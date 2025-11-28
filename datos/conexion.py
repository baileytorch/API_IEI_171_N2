from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from auxiliares import user, password, server, port, database

DATABASE_URL = f'mysql+mysqlconnector://{user}:{password}@{server}:{port}/{database}'
motor_db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=motor_db)
sesion = Session()
