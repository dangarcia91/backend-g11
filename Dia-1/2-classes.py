class Persona:
    # Cuando una variable se define dentro de una clase para a llamarse ATRIBUTO
    estatura = 1.80
    peso = 80
    signo_zodiacal = 'LEO'

    #def sumar(self, numero1, numero2):
    def sumar(self, *args):
        # self es como el this en el caso de js, c#, c++
        # cuando una función se define dentro de una clase pasa a llamarse METODO
        # Recibir un numero ilimitado de numeros para realizar su sumatoria
        #return numero1 + numero2
        total = 0
        for numeros in args:
            total = total + numeros
        return total

    
    def salud(self, nombre):
        return 'Hola{}'.format(nombre)
        
# cuando sacamos una 'copia' de la clase para uilizarla = una instancia
persona1 = Persona()
persona2 = Persona()

#Modifico los atributos de esa persona en particular
persona1.peso = 70
persona2.peso = 50

#todas las modificaciones que hacemos es independiente de la instancia

print(persona1.peso)
print(persona2.peso)

resultado1 = persona1.sumar(10,5,41,526,489,63)
resultado2 = persona2.sumar(5,8,65,985,492,520,700)

print(resultado1)
print(resultado2)