from rest_framework import generics
from .models import  Post, Comentario
from .serializers import  PostSerializer, ComentarioSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated



# Vista para listar y crear usuarios
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all() 
    serializer_class = UserSerializer  

# Vista para obtener, actualizar y eliminar usuarios
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()  
    serializer_class = UserSerializer

# Vista para listar y crear posts
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()  
    serializer_class = PostSerializer 
    permission_classes = [IsAuthenticated] 

# Vista para obtener, actualizar y eliminar posts
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()  
    serializer_class = PostSerializer 
    permission_classes = [IsAuthenticated]

# Vista para listar y crear comentarios
class ComentarioListCreateView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all() 
    serializer_class = ComentarioSerializer 
    permission_classes = [IsAuthenticated]

# Vista para obtener, actualizar y eliminar comentarios
class ComentarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()  
    serializer_class = ComentarioSerializer 
    permission_classes = [IsAuthenticated]

# Vista para login de usuarios
class LoginView(TokenObtainPairView):
    pass  # No es necesario agregar código adicional, ya que la clase base maneja todo