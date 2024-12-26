from django.urls import path
from .views import UsuarioListCreateView, UsuarioRetrieveUpdateDestroyView, PostListCreateView, PostRetrieveUpdateDestroyView, ComentarioListCreateView, ComentarioRetrieveUpdateDestroyView

urlpatterns = [
    path('usuario/', UsuarioListCreateView.as_view(), name='usuarios_list'),
    path('usuario/<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='manipulate-usuario'),  
    
    path('post/', PostListCreateView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='manipulate-post'),  
    
    path('comentario/', ComentarioListCreateView.as_view(), name='comentarios_list'),
    path('comentario/<int:pk>/', ComentarioRetrieveUpdateDestroyView.as_view(), name='manipulate-comentario') 
]