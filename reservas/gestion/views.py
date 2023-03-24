from rest_framework.views import APIView
from rest_framework.response import Response

class PruebaView(APIView):
    def get(self, request):
        data = [ {
            'nombre': 'diversion',
            'id': 1
        }, {
            'nombre': 'entretenimiento',
            'id': 2
        }]

        #return {
        #    'content': data
        #}
        return Response(data=data)
    
    def post(self, request):
        
        return Response(data= {
            'message': 'Se recibió la prueba'
        })
