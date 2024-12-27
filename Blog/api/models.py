from django.db import models
from django.contrib.auth.models import User  # Importar el modelo User de Django


# Create your models here.
# El modelo Post ahora utiliza el modelo User para autor
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='post', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con User
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# El modelo Comentario ahora utiliza el modelo User para autor
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con User
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre