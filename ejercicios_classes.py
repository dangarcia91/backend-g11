from pprint import pprint
#Crear una Classe Operaciones con sus respectivos métodos
# (sumar, restar, multiplicar  dividir) . Esta clase tiene que recibir dos parámetros

class Operaciones:
    def __init__(self, num1, num2) -> None:
        self.a = num1
        self.b = num2


    def Sumar (self):
        return self.a + self.b + self.c
    
    def restar(self):
        return self.a - self.b
    
    def multiplicar(self):
        return self.a * self.b
    
    def dividir(self):
        return self.__redondear(self.a / self.b)
    
    def __redondear(self, numero):
        return round(numero, 2)
    
operacion = Operaciones(5, 3)

#print(operacion.dividir())

# Crear una clase Usuario que reciba los datos de un usuario
# (nombre, edad, dni, estatura, estado civil) y crear un método para convertir los datos en un diccionario

class Usuario:
    def __init__(self, nombre, edad, dni, estatura, estado_civil) -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.estatura = estatura
        self.estado_civil = estado_civil

    def convertirDiccionario (self):
            return {
                'nombre': self.nombre,
                'edad': self.edad,
                'dni': self.dni,
                'estaura': self.estatura,
                'estado_civil': self.estado_civil
            }

datos_usuario = Usuario('Daniel', 31, 47029543, 1.70, 'soltero')
pprint(datos_usuario.convertirDiccionario())

