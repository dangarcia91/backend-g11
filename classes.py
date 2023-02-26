class Vehiculo:
    #color = "rojo"
    #placa = "y21-534"
    #marca = "Honda"
    def __init__(self, color, placa, marca) -> None:
        self.color = color
        self.placa = placa
        self.marca = marca


    def verificarEstado(self, fabricacion):
        return f'El vehículo de color {self.color} fue fabricado en el año de: {fabricacion}' 
    
    def concatenarCaracteristicas (self):
        return f'EL vehículo con placa {self.placa} y de color {self.color} es de marca {self.marca}'

vehiculo = Vehiculo("rojo", "y21-534", "Honda")

#print(vehiculo.verificarEstado(1999))
#print(vehiculo.concatenarCaracteristicas())

# podemos acceder, no solo a variables, sino a métodos

class Alumno:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, edad: {self.edad}'
    
    def mostrarEdad (self):
        return self.edad
    
    def mostrarNombre(self):
        return self.nombre
    
x = Alumno ('Eduardo', 30)

print(x.mostrarNombre())