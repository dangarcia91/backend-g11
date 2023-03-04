from flask_restful import Resource, request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.nivel_model import Nivel
from dtos.nivel_dto import NivelDto

class NivelController(Resource):
    # GET, POST, PUT
    def get(self):
        query: Query = conexion.session.query(Nivel)
        # SELECT * FROM niveles:
        resultado = query.all()


        dto = NivelDto()
        # DUMP > es un metodo por el cual le paso las intancias que quiero convertir a tipos de datos genéricos. Si se le pasa más de una instancia (una lista de instancias) se le tiene que adicionar el parámetro many=True para indicar que lo tendrá que iterar
        niveles = dto.dump(resultado, many=True)
        

        #niveles = []
        #for nivel in resultado:
        #    niveles.append(
        #    {
        #        'id': nivel.id,
        #        'numero': nivel.numero,
        #        'descripcion': nivel.descripcion
        #    })
        return {
            'content': niveles
        }
    def post(self):
        data = request.json
        dto = NivelDto()
        # load > le pasamos un diccionario y lo convertirá y validará si toda la inforamción es correcta, si no lo es, emitirá un error y si la información está bien me devolverá un diccionario con la data correcta
        try:
            data_validada = dto.load(data)
            print(data_validada)

            nuevo_nivel = Nivel(numero=data_validada.get('numero'), descripcion=data_validada.get('descripcion'))
          
            # con el método add indicamos que queremos guardar ese nuevo registro 
            conexion.session.add(nuevo_nivel)
            # con el método commit queremos guardar de manera permanente esa información en la base de datos
            conexion.session.commit()

            return {
                'message': 'Nivel creado, exitosamente'
            }, 201
        except Exception as error:
            return {
                'message': 'Error al crear el nivel',
                'content': error.args
            }
        
class UnNivelController(Resource):
    def get(self, id):
        query: Query = conexion.session.query(Nivel)
        nivel_encontrado = query.filter_by(id= id).first()
        #TODO Implemenetar si no existe ese nivel, retomar un mensaje que diga que no existe ese nivel
        dto = NivelDto()
        resultado = dto.dump(nivel_encontrado)

        return {
            'content': resultado
        }