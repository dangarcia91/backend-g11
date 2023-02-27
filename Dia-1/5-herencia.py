class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre= nombre
        self.apellido = apellido
    
    def saludar(self):
        return 'Buenos días!'
    
class Beneficio():
    def __init__(self, detalle) -> None:
        self.detalle = detalle

    def mostrar_beneficios(self):
        return {
            'datalle' : self.detalle
        }

class Alumno(Persona):
    def __init__(self, nombre, apellido, grado) -> None:
        self.grado = grado
        super().__init__(nombre, apellido)

    def saludar(self):
        # polimorfismo > poli (muchas) morfa (formas) > dependiendo de donde se mande a llamar al método tendrá un comportamiento u otro, en este cso estamos modificando el comportamiento del método de la clase padre "saludar"
        saludo_padre = super().saludar()
        print(saludo_padre + 'Hola soy un alumno')
    
    def dar_vueltas(self):
        print('Dando vueltas...')

class Docente(Persona, Beneficio):
    def __init__(self, nombre, apellido, seguro_social, detalle) -> None:
        self.seguro_social = seguro_social
        # En el caso de usar herencia multiple el uso del comodin "super" queda obsoleto. ya que no se puede indicar a cual de las dos clases estamos haciendo referencia. Para ello se utiliz el nombre de la clase directamente, y para ello se indica el metodo a utilizar
        # Se la pesa el "self" para indicar también lo que sería la misma instancia para evitar cruce de información
        Persona().__init__(nombre, apellido)
        Beneficio.__init__(self, detalle)
    
    def dar_vueltas(self):
        print('Evaluando...')

eduardo = Alumno('eduardo', 'de Rivero', 'quinto')
paolo = Docente('paolo', 'soncco', '1589658', 'Pizaa 15% dscto')

eduardo.saludar()
print(paolo.saludar())

print(paolo.mostrar_beneficios())
print(eduardo.nombre)