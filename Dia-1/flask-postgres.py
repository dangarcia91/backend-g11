from flask import Flask, request
from psycopg2 import connect

app = Flask(__name__)
# me conecto a la bd
conexion = connect(host='localhost', database= 'pruebas', user='postgres', password='data23')

@app.route('/', methods = ['GET'])
def inicial():
    return {
        'message': 'Bienvenido a mi API'
    }

@app.route('/alumnos', methods = ['GET', 'POST'])
def alumnos ():
    if request.method == 'GET':
       
        # Crea un cursor que es el respomsable de hacer lecturas y escrituras a la bd
        cursor = conexion.cursor()
        
        # Ejecuto la query
        cursor.execute('SELECT * FROM alumnos;')

        # extraigo la informacion de la ejecución de la query
        resultado = cursor.fetchall()

        print(resultado)
        alumnos_resultado = []
        for alumno in resultado:
            info_alumno = {
                'id': alumno[0],
                'nombre': alumno[1],
                'apellido': alumno[2],
                'sexo': alumno[3],
                'fecha_creacion': alumno[4],
                'matriculado': alumno[5],
            }

            alumnos_resultado.append(info_alumno)
        return {
            'message': alumnos_resultado
        }
    elif request.method == 'POST':
        data = request.json
        print(data)
        cursor = conexion.cursor()
        cursro.execute("INSERT INTO ALUMNOS (nombre, apellido, matriculado) VALUES (%s, %s. %s)", (
            data.get('nombre'), data.get('apellido'), data.get('matriculado')
        ))
        return {
            'message': 'Yo soy el POST'
        }

if __name__ == '__main__':
    # debug > indicar que cada vez que guardemos un archivo del proyecto el servidor se reinicie automaticamente
    app.run(debug = True)
