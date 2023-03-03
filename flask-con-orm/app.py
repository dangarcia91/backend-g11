from flask import Flask
from base_de_datos import conexion
from dotenv import load_dotenv
from os import environ

load_dotenv() # es el encargado de leer el archivo .env si es que existe y agregar las variables en ese archivo como si fueran variables de entorno.

app = Flask(__name__)
# dialecto://usuario:password@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

# Si quiero crear mi conexión en otro archivo e inicializar la configuración de mi conexión, tengo que utilizar el método init_app y es acá donde le pasaré el parámetro de mi instancia de la clase Flask
conexion.init_app(app)



if __name__ == '__main__':
    app.run(debug=True)

