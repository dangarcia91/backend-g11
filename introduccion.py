numero = 10

if numero > 11:
    print('Es mayor que 11')
#tiene que haber identación
string = "soy un string"
booleano_true = True
booleano_false = False
flotantes = 3.1416
diccionarios = {
    'nombre': 'Eduardo'
}
listas = [1,2,3, 'string', 3.14]
tuplas = ("texto_1", "text_2", "text")
# En una tupla se puede almacenar distintos tipos de datos

#print(type(booleano_false))

x = 5
x = 'cinco'
X = 'numero'
y = '5'
y = int(y)
y = str(y)
y = float(y)
#print (y)

# FORMAS iNCORRECTAS DE NOMBRAR UNA VARIABLE
# numero-cinco = 5
#5numero = 5
#numero cinco = 5

# FORMAS iNCORRECTAS DE NOMBRAR UNA VARIABLE
numero_cinco = 5
NumeroCinco = 5
_numeroCinco = 5

# Asignar múltiples variables
a, b, c = 2, 5, 'string'
#print(a, b, c)

#const myFunction = () =>

def myFunction():
    variable_1 = "texto de ejemplo"
    print(variable_1)

#   OPERADORES
# 5 == 5
# 4 != 5
# 1 > 0
1 < 2
5 >= 5
6 >= 6

# or
# and
# not

edad = 18

#if edad < 18:
#    print('Eres menor de edad')
#elif edad == 18:
#    print('acabas de convertirte en mayor edad edad')
#else:
#    print('Eres mayor de edad')

estado_civil = 'D'

#if estado_civil == 'C':
    #print('El usuario está casado')
#elif estado_civil == 'V':
    #print('El usuario está viudo')
#elif estado_civil == 'D':
    #print('El usuario está divorciado')
#else:
    #print('El usuario está soltero')

#Lista_nombres = ['Eduardo', 'Antonio', 'Luis', 'Mary']

#for nombre in Lista_nombres:
#    print('nombre')

lista_numeros = [23, 24, 25, 26, 27]

for num in lista_numeros:
    if num == 25:
        #break
        continue
    #print(num)

#print(lista_numeros[2])

cadena_texto = 'Hola, soy alumno del G11 backend'

#for letra in cadena_texto:
#    print (letra)

print (cadena_texto[0])
