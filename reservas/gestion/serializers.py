from rest_framework import serializers
from .models import Categoria, Producto
from math import ceil

class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoConCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        # detph > Sirve para indicar que nio solamente nos queremos quedar en este modelo sino que mediante la FK queremos acceder a "n" niveles
        depth = 1

def paginationSerializer(totalItems, page, perPage):
    itemsPerPage =perPage if totalItems >= perPage else totalItems
    totalPages = ceil(totalItems/ itemsPerPage) if itemsPerPage > 0 else None
    prevPage = page - 1 if page > 1 and page <= totalPages else None
    nextPage = page + 1 if totalPages > 1 and page < totalPages else None

    return {
        'temsPerPage': itemsPerPage,
        'totalPages': totalPages,
        'prevPage': prevPage,
        'nextPage': nextPage
    }