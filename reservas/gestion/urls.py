from django.urls import path
from .views import PruebaView, CategoriaView

# urlpatterns > OMBRE OBLIGATORIO para definir nuestras rutas

urlpatterns = [
    path('prueba', PruebaView.as_view()),
    path('otra_pruena', PruebaView.as_view()),
    path('categoria', CategoriaView.as_view()),
]