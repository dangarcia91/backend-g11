from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from os import environ
from db import conexion
from flask_restful import Api

from utils.enviar_correo import enviar_correo_adjuntos
from controllers.usuario_controller import RegistroController
from controllers.categoria_controller import ImagenesCOntroller, CategoriasController
from controllers.producto_controller import ProductosController

load_dotenv()

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['UPLOAD_FOLDER'] = '/imagenes'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1000 * 1000

conexion.init_app(app)

api = Api(app)

Migrate(app, conexion)

@app.route('/prueba')
def enviar_correo_prueba():
    # correo al cual va a llegar la información
    enviar_correo_adjuntos('ederiveroman@gmail.com', 'Correo con imagenes')

    return {
        'message': 'Correo enviado exitosamente'
    }

api.add_resource(RegistroController, '/registro')
api.add_resource(ImagenesCOntroller, '/imagenes', '/imagenes/<nombre>')
api.add_resource(CategoriasController, '/categorias')
api.add_resource(ProductosController, '/productos')

if __name__ == '__main__':
    app.run(debug=True)
    