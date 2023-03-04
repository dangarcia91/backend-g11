from base_de_datos import conexion
from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey

class Seccion(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nonbre = Column(type_=types.Text, nullable=False)
    alumnos = Column(type_=types.Integer, default=10)

    #Si una columna será utilizada como llave foránea entonces tenemos que utilizar la clase ForeignKey, en ella usaremos el parámetro 'column' en el cual indicaremos tabla queremos referenciar
    nivelId = Column(ForeignKey(column='niveles.id'), type_=types.Integer, nullable=False, name='nivel_id')

    maestroId = Column(ForeignKey(column='maestros.id'), type_=types.Integer, nullable=False, name='maestro_id')



    __tablename__ = 'secciones'