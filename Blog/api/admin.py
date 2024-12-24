from django.contrib import admin
from .models import Post , Usuario, Comentario

# Register your models here.
admin.site.register(Post)
admin.site.register(Usuario)
admin.site.register(Comentario)
