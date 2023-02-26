#def suma(a, b):
 #   print(b)

#suma(2, 3)

def suma(numero_1, numero_2):
    #resultado = numero_1 + numero_2
    #print(resultado)
    #return resultado
    return numero_1 + numero_2
    #return guarda el resultado en la nueva variable


#resultado_suma = suma(1, 2)
#print(resultado_suma)

def resta(a, b):
    return a - b


def multiplicacion (c, d):
    return c * d

def division (e, f):
    return e / f

#print(division(2, 4))

#print('¿Qué operación desea realizar?')
#opcion = input()
#opcion = input('Indicar operacion matemática: ')
#print(opcion)
#print ('La operación que solicito es ' + opcion)

#Crear una funcion que dependiendo del tipo de operacion que yo le indique me retorne el resultado:

#if opcion == 'suma':
#    print(suma(4, 2))
#elif opcion == 'resta':
#    print(resta(4, 2))
#elif opcion == 'multiplicacion':
#    print (multiplicacion(4, 2))
#else:
#    print (division(4, 2))

def concatenar():
    return 213 + 'string'

def calcularResultadoPorOperacion(operacion, valor_1, valor_2):
    #print(type(valor_1), type(valor_2))
    if operacion == 'suma':
        return f'El resultado de la {operacion} es {suma(valor_1, valor_2) }' 
    elif operacion == 'resta':
        return f'El resultado de la {operacion} es {resta(valor_1, valor_2) }' 
    else:
        return 'La operación no existe'

operación = input ('Ingrese el tipo de operación: ')
valor_1 = int(input ('Ingrese el primer número: '))
valor_2 = int(input ('Ingrese el segundo número: '))

resultado = calcularResultadoPorOperacion(operación, valor_1, valor_2)
#print (f'El resultado de la operación es: {resultado} ')
#print ('El resultado de la operación es {}'.format(resultado) )
print (resultado)