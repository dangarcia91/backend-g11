from flask_restful import Resource, request
from werkzeug.utils import secure_filename
from os import path

from uuid import uuid4
from db import conexion
from models.producto_model import Producto
from dtos.producto_dto import ProductoDto, MostrarProductoDto

class ProductosController(Resource):
    def post(self):
        data = request.form.to_dict()
        # TODO: validar que tengamos esa llave en el formulario llamada 'imagen'
        # TODO: validar que solo sean imágenes
        mimetype_valido = 'image/'
        imagen = request.files.get('imagen')
        # TODO: agregar un uuid al nombre de la imagen
        # TODO: no recibir imagenes que pesen más de 10Mb
        #                   B   KB      MB
        CONTENIDO_MAXIMO = 10 * 1024 * 2024
        try:
            if image is None:
                raise Exception ("Se necesita una imagen para poder crear el producto")
            
            if mimetype_valido not in imagen.mimetype:
                raise Exception('El tipo de archivo no es válido')
            if imagen.content_length > CONTENIDO_MAXIMO:
                raise Exception('El archivo es muy pesado')
            
            # 
            dto = ProductoDto()
            nombre_imagen = secure_filename(uuid4().hex +'_'+ imagen.filename)
            data['imagen'] = 'imagenes/' + nombre_imagen
            data_serializada = dto.load(data)

            nuevo_producto = Producto(**data_serializada)
            conexion.session.add(nuevo_producto)

            #imagen.save(path.join('imagenes', data['imagen']))
            imagen.save(path.join('imagenes', nombre_imagen))
            
            conexion.session.commit()
            return {
                'message': 'Producto creado exitosamente'
            }
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }
        
    def get(self):
        resultado = conexion.session.query(Producto).all()
        dto = MostrarProductoDto()
        data = dto.dump(resultado, many=True)
        return {
            'content': data
        }

