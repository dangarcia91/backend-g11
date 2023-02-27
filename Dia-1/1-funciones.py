def saludar(nombre):
    saludo = 'Hola {}'.format(nombre)
    print(saludo)

saludar('Eduardo')

def saludar_varios(*args):
    #cuando nosotros colocamos en un parámetro el '*' significa que no hay límite de ese parámetro, este parámetro debe ir al último
    #todos los valores que le pasemos a este parámetro se almacenan en una tupla
    # NOTA: las tuplas, a diferencia de los arreglos , no se pueden modificar, osea una vez creadaos sus valores no pueden cambiar

    #print(args)
    for nombre in args:
        saludo = 'Hola{}'.format(nombre)
        #print(saludo)

saludar_varios('Roxana', 'Juana', 'Martin', 'Roberto')
saludar_varios('Pedro', 'Luis')
saludar_varios()
saludar_varios('Eduardo', 20, True, 10.5)

def informacion_usuario(**kwargs):
    # kwargs > keyboard argument o se le pasan parametros por llaves
    print(kwargs)
    # .get('llave') > devolverá el valor si es que exite la llave, sino existe entonces devolverá None o el segundo parametro que le colocamos(opcional)
    print(kwargs.get('estatura', 'No HAAAAAY'))
    try:
        print(kwargs['estatura'])
    except:
        print('No existe la llave estatura')

informacion_usuario(nombre='Eduardo', edad= 30, esta_civil='soltero', estatura= 1.88)
informacion_usuario(nombre='Pamela', apellido='Juarez', nacionalidad='Clombiana', fecha_nacimiento='31/06/199')

# recibir dos valores y hacer la division (dividendo / divisor)
def dividir(dividendo, divisor):
    # si la division da un error entonces retornar un mensaje que diga 'Division incorrecta'
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        #Aquí ingresará cuando la división sea entre cero
        return 'No puede haber division entre cero'
    except TypeError:
        #Aquí ingresará si la divisón tiene algun caracter
        return 'No se puede dividir letras'
    except:
        #Aquí ingresará si no cumple ninguno de los dos errores anteriores
        return 'Error desconocido'

valor = dividir(10, 5)
print(valor)

valor = dividir(10, 0)
print(valor)

valor = dividir('a', 'h')
print(valor)

try:
    valor = dividir(5,)
    print (valor)
except TypeError:
    print('Estuvo mal llamar asi a la función')