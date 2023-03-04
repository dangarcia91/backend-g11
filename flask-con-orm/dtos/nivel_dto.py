from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.nivel_model import Nivel

class NivelDto(SQLAlchemyAutoSchema):
    class Meta:
        # model > para indicar qué modelo tiene que utilizar para poder hacer el maepo y validaciones de los atributos
        model = Nivel
