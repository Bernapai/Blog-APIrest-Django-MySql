from django.db import models


# Create your models here.
class usuario (models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    fecha_registro = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nombre

class post (models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='post', null=True, blank=True)
    autor = models.ForeignKey(usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class comentario (models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contenido = models.TextField()
    autor = models.ForeignKey(usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre