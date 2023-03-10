from flask import Flask, request
from psycopg2 import connect
from flask_cors import CORS

app = Flask(__name__)
#le estamos diciendo que puede acceder cualquier origen, cualquier método y enviar cualquier header
CORS(app, methods = ['GET', 'POST', 'PUT', 'DELETE'], origins = ['http://localhost:5555', 'http://127.0.0.1:5555'])


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
        cursor.execute("INSERT INTO ALUMNOS (nombre, apellido, matriculado) VALUES (%s, %s, %s)", (
            data.get('nombre'), data.get('apellido'), data.get('matriculado')
        ))
        #Indicamos a la base de datos que guarde los cambios (insert) de manera permanente
        conexion.commit()

        return {
            'message': 'Alumno ingresado exitosamente'
        }

@app.route('/alumno/<id>', methods = ['GET', 'PUT', 'DELETE'])
def gestion_alumno(id):
    if request.method == 'GET':
        
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM alumnos WHERE id=%s", (id,))
        alumno = cursor.fetchone()
        # si el alumno no existe, indicar en el mensaje que el alumno no existe, caso contrario devolver el alumno
        print(alumno)
        if alumno is None:
            return {
            'message': 'el alumno no existe'
            }
        else:
            return {
            'content': {
                'id': alumno[0],
                'nombre': alumno[1],
                'apellido': alumno[2],
                'sexo': alumno[3],
                'fecha_creacion': alumno[4],
                'matriculado': alumno[5],
            }
            }

    elif request.method == 'PUT':
        # TODO: recibir la información del body y esta modificar la data del alumno, primero validar si el alumno existe, si no existe no hacer ninguna modificación, si existe hacer la modificación.
        data = request.json
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM alumnos where id={id}")
        resultado = cursor.fetchone()
        if resultado is None:
            return {}
        else: 
            cursor.execute("UPDATE alumnos SET (nombre, apellido, matriculado) VALUES (%s, %s, %s)", (
            data.get('nombre'), data.get('apellido'), data.get('matriculado')
        ))
        conexion.commit()
    
    elif request.method == 'DELETE':
        #TODO: REcibir el id por la url y validar si el alumno existe, si existe, eliminarlo (hacer un delete) caso contrario indicar que el alumno no existe
        data = request.json
        cursor = conexion.cursor()
        resultado = cursor.fetchone()
        if resultado is not None:
            cursor.execute("DELETE FROM alumnos where id={id}")
        else:
            return {
                'message': 'El alumno no existe'
            }  



if __name__ == '__main__':
    # debug > indicar que cada vez que guardemos un archivo del proyecto el servidor se reinicie automaticamente
    app.run(debug = True)
