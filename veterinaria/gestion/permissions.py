from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from .models import Usuario

class SoloClientes(BasePermission):
    message = 'Solo los clientes pueden realizar esta petición'
    
    def has_permission(self, request: Request, view):
        # request.user > toda la información del usuario autenticado
        usuario : Usuario = request.user

        # return True if usuario.tipoUsuario == 'CLIENTE' else False
        if usuario.tipoUsuario == 'CLIENTE':
            # Si retornamos True indica que el usuario tiene los permisos correspondientes
            return True
        else:
            return False