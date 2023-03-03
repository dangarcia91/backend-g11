from base_de_datos import conexion 
from sqlalchemy import Column, types
#Las tablas se van a comportar como si fueran clases y cada columna será un atributo en la clase
class Nivel(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    numero = Column(type_=types.Integer, nullable=False, unique=True)
    descripcion = Column(type_=types.Text)


    #Como se llamará la tabla en la base de datos
    __tablename__ = 'niveles'