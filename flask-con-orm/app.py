# primero se important las linbrerías
from flask import Flask
from base_de_datos import conexion
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate
from flask_restful import Api
# se importan los archivos dentro del proyecto
from models.nivel_model import Nivel
from models.maestro_model import Maestro
from models.seccion_model import Seccion
from controllers.nivel_controller import NivelController, UnNivelController
from controllers.maestro_controller import MaestroController, UnMaestroController



load_dotenv() # es el encargado de leer el archivo .env si es que existe y agregar las variables en ese archivo como si fueran variables de entorno.

app = Flask(__name__)
# dialecto://usuario:password@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')


flask_api = Api(app=app)

# Si quiero crear mi conexión en otro archivo e inicializar la configuración de mi conexión, tengo que utilizar el método init_app y es acá donde le pasaré el parámetro de mi instancia de la clase Flask
conexion.init_app(app)

# ahora realizo la inicialización de mi clase Migrate
# se le pasa la aplicación como primer parámetro y la conexión (instancia de SQL Migrate, como segundo parámetro)
Migrate(app=app, db=conexion)

#defino las rutas de mi API
flask_api.add_resource(NivelController, '/nivel')
flask_api.add_resource(UnNivelController, '/nivel/<id>')
flask_api.add_resource(MaestroController, '/maestro')

if __name__ == '__main__':
    app.run(debug=True)

