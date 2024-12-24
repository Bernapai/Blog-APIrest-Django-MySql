from django.db import models


# Create your models here.
class Usuario (models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    fecha_registro = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nombre

class Post (models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='post', null=True, blank=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contenido = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre