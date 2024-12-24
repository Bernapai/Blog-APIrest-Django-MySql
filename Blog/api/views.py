from django.shortcuts import render
from django.views import View
from .models import Usuario, Post, Comentario

# Create your views here.
class UsuarioView (View) :

    def get (self, request, id_usuario = 0):
        if id_usuario > 0:
            usuario = Usuario.objects.get(id=id_usuario)
        else:
            usuarios = Usuario.objects.all()

    
    def post (self, request):
        pass

    def delete (self, request):
        pass

    def put (self, request):
        pass


    
class PostView (View) :

    def get (self, request, ):
        posts = Post.objects.all()

    
    def post (self, request):
        pass

    def delete (self, request):
        pass

    def put (self, request):
        pass


class ComentarioView (View) :

    def get (self, request):
        comentarios = Comentario.objects.all()

    
    def post (self, request):
        pass

    def delete (self, request):
        pass

    def put (self, request):
        pass

    