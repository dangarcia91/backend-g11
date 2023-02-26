# Ordenar ciudades por la cantidad de habitantes
from pprint import pprint

ciudades = [
    {
      'nombre': 'Tumbes',
      'habitante' : 500000
    },
    {
      'nombre': 'Arequipa',
      'habitante' : 800000
    },
    {
      'nombre': 'Loreto',
      'habitante' : 10000
    }
]

#def ordenarCIudades(lista_ciudades):
  #habitantes_ultima_ciudad = 0
  #for ciudad in lista_ciudades:
  #   if ciudad['habitante'] < habitantes_ultima_ciudad:
    #      continue
      # else:
      #    print(ciudad['habitante']) 
      #habitantes_ultima_ciudad = ciudad['habitante']

#ordenarCIudades(ciudades)

#lista_numeros = [1, 5, 2, 4, 6, 9, 8]
#lista_numeros.sort(reverse=True)
#print(lista_numeros)

def habitante(ciudades):
    return ciudades['habitante']
ciudades.sort(key=habitante)
#pprint(ciudades)

ciudades.append({'nombre': 'CUsco', 'habitante': '20000'})
ciudades.pop(0)
#ciudades.remove({'nombre': 'Cusco', 'habitante': '20000'})
index = 0
for ciudad in ciudades:
    if ciudad['nombre'] == 'Cusco':
        ciudades.remove(ciudades[index])
    index = index + 1
pprint(ciudades)

lista = ['Arequipa', 'Cusco', 'Tumbes']
# lista.remove('Arequipa)
# print(lista)

for x, y in enumerate(lista):
    print (x, y)