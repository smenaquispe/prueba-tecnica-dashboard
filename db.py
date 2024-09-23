import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from dotenv import load_dotenv
from setup_tables import setup_tables

# Cargar las variables de entorno
load_dotenv()

def init_db():
    # Obtener configuraciones desde variables de entorno
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '3306')
    DB_NAME = os.getenv('DB_NAME', 'dashboard_db')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')

    # Conexión a la base de datos usando variables de entorno
    DATABASE_URL = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = create_engine(DATABASE_URL)

    # Probar la conexión a la base de datos
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()

        Base.metadata.create_all(engine)

        print("¡Conexión exitosa a la base de datos!")
        connection.close()
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        exit()

    # Crear una sesión
    Session = sessionmaker(bind=engine)
    # Esta sesión es la que se utilizará para hacer las consultas
    session = Session()

    # inicamos la creación de las tablas y registros
    # en esta caso solo tabla Empleado
    setup_tables(session=session)

    return session