from rest_framework.serializers import ModelSerializer
from .models import Usuario, Mascota

class RegistroUsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class MascotasSerializer(ModelSerializer):
    class Meta:
            model = Mascota
            fields = '__all__'
    # recuperamos la ruta real de la imagen en Cloudinary
    def to_representation(self, instance):
        print(instance.foto.url)
        representacion = super().to_representation(instance)
        representacion['foto'] = instance.foto.url
        return representacion