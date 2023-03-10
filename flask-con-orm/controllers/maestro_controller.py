# TODO Implementar para crear y listar a todos los maestros, utilizar o crear los DTOs 

from flask_restful import Resource, request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.maestro_model import Maestro
from dtos.maestro_dto import MaestroDto

class MaestroController(Resource):
    # GET, POST, PUT
    def get(self):
        query: Query = conexion.session.query(Maestro)
        resultado = query.all()
        dto = MaestroDto()
        maestros = dto.dump(resultado, many=True)
        return {
            'content': maestros
        }
    def post(self):
        data = request.json
        try:
            dto = MaestroDto()
            data_validada = dto.load(data)
            nuevo_maestro = Maestro(nombre=data_validada.get('nombre'), apellidos=data_validada.get('apellidos'), correo=data_validada.get('correo'), direccion=data_validada.get('direccion'))
            conexion.session.add(nuevo_maestro)
            conexion.session.commit()

            return {
                'message': 'Maestro creado, exitosamente'
            }, 201
        except Exception as error:
            return {
                'message': 'Error al crear al maestro',
                'content': error.args
            }
    