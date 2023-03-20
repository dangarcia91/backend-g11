from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import conexion

class Producto(conexion.Model):
      id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
      nombre = Column(type_=types.Text, nullable=False)
      precio = Column(type_= types.Float)
      imagen = Column(type_=types.Text)
      categoriaId = Column(ForeignKey(column='categorias.id'), type_=types.Integer, nullable=False, name='categoria_id')
      categoria = relationship('Categoria', backref= 'productos')
      created_at = Column(type_=types.DateTime, default=datetime.utcnow(), name='createdAt')

      __tablename__ = 'productos'