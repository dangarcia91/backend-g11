from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Bienvenidos a mi primera API con Flask"

@app.route("/alumno")
def alumno():
    return {
        'nombre': 'Eduardo',
        'edad': 30,
        'promedio': 18
    }

lista_alumnos = [
        {
        'nombre': 'Eduardo',
        'edad': 30,
        'promedio': 18
        },
        {
        'nombre': 'Guillermo',
        'edad': 25,
        'promedio': 18
        },
    ]


@app.route("/alumnos", methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS',])
# este parámetro recibe una lista, si no recibe ninguno es "get"
def alumnos():
    print(request.method)
    if request.method == 'GET':
        return lista_alumnos
    elif request.method == 'POST':
        # métodos para obtener el body (request.json) ó (request.get_json)
        lista_alumnos.append(request.json)
        #print(request.json)
        #print(request.get_json())
        return lista_alumnos

@app.route("/alumno/<nombre>")
def buscar_alumno(nombre):
    for alumno in lista_alumnos:
        if alumno['nombre'] == nombre:
            return alumno
    return {
        'message': 'El alumno no existe'
    }
    #return f'El alumno se llama: {nombre}'

@app.route("/html")
def html():
    edad = 10
    #return "<button>Dame click</button>"
    return render_template('index.html', edad=edad)

@app.route("/form-data", methods=['POST'])
def form_data():
    print(request.form['nombre'])
    return 'Form data recibido exitosamente'

@app.route("/files", methods=['POST'])
def files():
    file_str = request.files['foto'].read().decode('utfo')
    f = open('archivo.txt', "m")
    f.write(file_str)
    return 'Archivo recibido exitosamente'

# debug => Si realizamos algún camibio podremos verlo en tiempo real(se reiniciará el servidor)
app.run(debug=True)