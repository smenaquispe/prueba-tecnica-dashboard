from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Modelo de la tabla empleados
class Empleado(Base):
    __tablename__ = 'empleados'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    ciudad = Column(String(100), nullable=False)
    salario = Column(DECIMAL(10, 2), nullable=False)