from rest_framework import generics
from .models import Usuario, Post, Comentario
from .serializers import UsuarioSerializer, PostSerializer, ComentarioSerializer

# Vista para listar y crear usuarios
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all() 
    serializer_class = UsuarioSerializer  
# Vista para obtener, actualizar y eliminar usuarios
class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer

# Vista para listar y crear posts
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()  
    serializer_class = PostSerializer  

# Vista para obtener, actualizar y eliminar posts
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()  
    serializer_class = PostSerializer 

# Vista para listar y crear comentarios
class ComentarioListCreateView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all() 
    serializer_class = ComentarioSerializer 

# Vista para obtener, actualizar y eliminar comentarios
class ComentarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()  
    serializer_class = ComentarioSerializer 


    