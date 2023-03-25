from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.TextField(null=False)
    habilitado = models.BooleanField(default=True)
    
    class Meta:
        # sirve para modificar alguna configuración de la tabla en nuestra bd
        db_table = 'categorias'

class Producto(models.Model):
    nombre = models.TextField(null=False)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)
    # registra automáticamente la hora y fecha del servidor cuando se cree un nuevo registro
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    # es el campo que se actualizará cada vez que modifiquemos algun dato del registro con la fecha actual
    updateAt = models.DateTimeField(auto_now=True, db_column='updated_at')

    # relaciones en la que una categoría tendrá muchas productos, pero un producto pertenecerá a una sola cateogría
    # on_delete > es la accion que tomara al momento de hacer la eliminación de una categoria y si esta tiene productos
    #CASCADE > elimina la cateogira y luego elimina en forma consecutiva a todos los productos de esa categoria
    # PROTECT > evita la eliminación de la categoria siempre y cuando esta tenga productos y lanzará un error de tipo IntegrityError
    # RESTRICT > evita la eliminación al igual que el PROTECT pero lanza un error de tipo RestrictedError
    # SET_NULL > elimina la categoria y a todos sus productos los cambia el valor de la categoria_id a NULL
    # SET_DEFAULT > elimina la cetegoria y de acuerdo al valor que le colocamos en default lo cambiara  a ese valor
    # DO_NOTHING > No realiza ninguna acción, elimina la categoría y no hace ningún cambio en los productos, no se debe utilizar esta ocpión ya que genera mala integridad de los datos.
    categoria = models.ForeignKey(to=Categoria, on_delete=models.CASCADE, db_column='categoria_id', related_name='productos')

    class Meta:
        db_table = 'productos'
        # nombre : De la A a la Z
        # -nombre: De la Z a la A
        ordering = ['-nombre', 'precio']
        # no se puede repetir la unicidad, o sea que dos registros tengan los mismos valores de dos columnas
        unique_together = ['nombre', 'precio']