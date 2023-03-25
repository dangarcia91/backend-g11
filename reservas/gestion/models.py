from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.TextField(null=False)
    habilitado = models.BooleanField(default=True)
    
    class Meta:
        # sirve para modificar alguna configuración de la tabla en nuestra bd
        db_table = 'categorias'

class Producto(model.Model):
    nombre = models.TextField(null=False)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)