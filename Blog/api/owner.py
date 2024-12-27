from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Permiso personalizado que solo permite que el propietario del objeto acceda a él.
    """

    def has_object_permission(self, request, view, obj):
        # Permite la lectura para cualquier usuario (GET)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permite la escritura (PUT, PATCH, DELETE) solo si el usuario es el propietario
        return obj.autor == request.user