from django.urls import path
from .views import UsuarioView, PostView, ComentarioView

urlpatterns = [
     path('usuario/', UsuarioView.as_view(), name='usuarios_list'),
]